""""
 met_site_data_creation_impact.py

 By Chris Fong - MSKCC 2019

This script will leveerage RDN's metastatic mapping from IMPACT patient cancer types to distant, lymphatic, regional
metastatic disease

This script will ONLY cover metastatic samples from IMPACT cohort. ALL metastatic disease sites are not covered

"""
import os
import pandas as pd
import constants_darwin as c_dar
from utils_darwin_etl import set_debug_console
from organ_mapping_analysis import OrganMappingAnalysisRND


# Console settings
set_debug_console()

# Filename for output
fname_save_anno = 'metatrop_met_site_annotations_impact.csv'
fname_save_binary = 'metatrop_met_site_annotations_impact_binary.csv'

## Load Data --------------
# Load IDs from GENIE table
fname = c_dar.fname_sample_summary_cbio
path = c_dar.pathname
pathfilename1 = os.path.join(path, fname)
df_samples = pd.read_csv(pathfilename1, header=0, low_memory=False, sep='\t')
# For genie, fix ids
col_rep = {'Patient ID': 'DMP_ID',
           'Sample ID': 'SAMPLE_ID',
           'Sex': 'SEX',
           'Cancer Type': 'CANCER_TYPE',
           'Sample Type': 'SAMPLE_TYPE',
           'Primary Tumor Site': 'PRIMARY_SITE',
           'Metastatic Site': 'METASTATIC_SITE'}
df_metatrop = df_samples.rename(columns=col_rep)


df_metatrop_met = df_metatrop[df_metatrop['SAMPLE_TYPE'] == 'Metastasis']
col_ct = 'CANCER_TYPE'
df_metatrop_ids = df_metatrop_met[['SAMPLE_ID', 'DMP_ID', col_ct]]

fname = 'oncotree_to_icd_billing_oncotree_organ_mapping.csv'
path = '/Users/fongc2/Documents/github/MSK/DARWIN_ETL/data/mapping_renzo'
pathfilename1 = os.path.join(path, fname)
df_oncotree_to_oncotree = pd.read_csv(pathfilename1, header=0, low_memory=False, sep=',')

# Obtain Renzo's mapping
obj_mapping = OrganMappingAnalysisRND(const_dar=c_dar)
df_met_sites_impact = obj_mapping.annotate_mapping_impact_met_samples(df_samples=df_metatrop_met, col_primary_site='PRIMARY_SITE', col_met_site='METASTATIC_SITE')
cols_sites_impact = ['SAMPLE_ID', 'DMP_ID', 'METASTATIC_SITE', 'PRIMARY_SITE_MAPPED', 'METASTATIC_SITE_MAPPED',
                     'LYMPH_SPREAD', 'LOCAL_EXTENSION', 'hematogenous_grouping', 'METASTATIC_SITE_ONCOTREE_RDN']
df_met_sites_impact1 = df_met_sites_impact[cols_sites_impact]


# Merge map with mapping to oncotree normalized mets sites
df_met_sites_impact2 = df_met_sites_impact1.merge(right=df_oncotree_to_oncotree, how='left',
                                                  left_on='METASTATIC_SITE_ONCOTREE_RDN',
                                                  right_on='tissue_oncotree')
# Drop columns
df_met_sites_impact2 = df_met_sites_impact2.drop(columns=['METASTATIC_SITE_ONCOTREE_RDN', 'tissue_oncotree'])
df_met_sites_impact2 = df_met_sites_impact2.rename(columns={'METASTATIC_SITE_ONCOTREE':'METASTATIC_SITE_ONCOTREE_NORM'})

df_met_sites_impact2['METASTATIC_SITE_ONCOTREE_NORM'] = df_met_sites_impact2['METASTATIC_SITE_ONCOTREE_NORM'].fillna('OTHER')

## Process and merge data
# Merge Renzo's annotations to the metatrop data
df_met_rdn_anno = df_met_sites_impact2

# Reclassify sites to be LN based on Renzo's mapping
df_met_rdn_anno.loc[df_met_rdn_anno['LYMPH_SPREAD'].notnull(), 'METASTATIC_SITE_ONCOTREE_NORM'] = 'LYMPH'
df_met_rdn_anno = df_met_rdn_anno[~df_met_rdn_anno['METASTATIC_SITE_ONCOTREE_NORM'].isin(['', 'UNKNOWN'])]
df_met_rdn_anno.loc[df_met_rdn_anno['LYMPH_SPREAD'] == 'DISTANT', 'METASTATIC_SITE_ONCOTREE_NORM'] = 'DIST_LYMPH'

# Save RDN annotations
df_met_rdn_anno.to_csv(fname_save_anno, index=False)

### ##############################
### Create binary table of RDN annotated data
# Pivot data
df_to_piv1 = df_met_rdn_anno[['DMP_ID', 'SAMPLE_ID', 'METASTATIC_SITE_ONCOTREE_NORM']]

df_met_piv = pd.pivot_table(data=df_to_piv1, index=['SAMPLE_ID'], values='DMP_ID',
                            columns='METASTATIC_SITE_ONCOTREE_NORM', aggfunc='count', fill_value=0)
df_met_piv = df_met_piv.reset_index()

# Rename columns
cols_met = [x for x in df_met_piv.columns if x is not 'SAMPLE_ID']
cols_met_new = ['HAS_MET_' + x.replace(' ', '_').replace('/', '_') for x in cols_met]
dict_cols_met = dict(zip(cols_met, cols_met_new))
df_met_piv = df_met_piv.rename(columns=dict_cols_met)

# Merge cancer types,
df_met_piv_f = df_metatrop_ids.merge(right=df_met_piv, how='right', on='SAMPLE_ID')
df_met_piv_f = df_met_piv_f.drop(columns=['SAMPLE_ID'])
df_met_piv_f1 = df_met_piv_f[df_met_piv_f[col_ct].notnull()]

# Compute met sites for each cancer type of a patient
df_met_piv_g = df_met_piv_f1.groupby(['DMP_ID', col_ct])[cols_met_new].sum().reset_index()
# Merge again with sample ids, such that met sites are duplicated for sample types within a cancer type
df_met_piv_m = df_metatrop_ids.merge(right=df_met_piv_g, how='right', on=['DMP_ID', col_ct])
df_met_piv_m = df_met_piv_m.drop(columns=col_ct)

# MAke binary/int
df_met_piv_m[cols_met_new] = (df_met_piv_m[cols_met_new] > 0).astype(int)

# Fill NAs with 0
df_met_piv_m[cols_met_new] = df_met_piv_m[cols_met_new].fillna(0)
df_met_piv_m = df_met_piv_m.assign(SOURCE_MET_DATA='IMPACT')

# Save file
df_met_piv_m.to_csv(fname_save_binary, index=False)


tmp = 0
