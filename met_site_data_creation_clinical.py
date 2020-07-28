""""
 met_site_data_creation_clinical.py

 By Chris Fong - MSKCC 2019

    This script will create a binary table of met sites for each patient. Then, the script will compute if a distant LN
    metastasis occurred for that patient, given their cancer type according to IMPACT data. The output will be a binary
    table of affected met sites, for each SAMPLE.
    If a patient has multiple dx from IMPACT, more than 1 row will exist for that patient, and should be removed.
"""
import sys
sys.path.insert(0, '../DARWIN_ETL/')
sys.path.insert(0, '../DARWIN_ETL/diagnosis')
import os
import pandas as pd
import constants_o_sites as const
import constants_darwin as c_dar
from utils_darwin_etl import set_debug_console
from darwin_summary_diagnosis import DarwinSummaryDiagnosis
from organ_mapping_analysis import OrganMappingAnalysisRND
from organ_mapping_rdn_processing import MetastaticSpreadMappingRND


# Console settings
set_debug_console()

fname_save_anno = 'metatrop_met_site_annotations_clinical.csv'

col_icd_billing = 'ICD-9/10 Dx Code'
col_met_site = 'METASTATIC_SITE'
col_primary_site = 'PRIMARY_SITE'

## Load cbioportal clinical data file --------------
# Load ID names
fname = 'mskimpact_clinical_data.tsv'
path = c_dar.pathname
pathfilename1 = os.path.join(path, fname)
df_samples1 = pd.read_csv(pathfilename1, header=0, low_memory=False, sep='\t')
# For genie, fix ids
col_id = 'SAMPLE_ID'
col_id2 = 'DMP_ID'
col_sex = 'SEX'
col_rep = {'Patient ID': col_id2,
           'Sample ID': col_id,
           'Sex': col_sex,
           'Cancer Type': 'CANCER_TYPE',
           'Primary Tumor Site': 'PRIMARY_SITE',
           'Metastatic Site': 'METASTATIC_SITE'}
df_samples1 = df_samples1.rename(columns=col_rep)
df_samples = df_samples1[list(col_rep.values())]

# Load met sites directly from diagnosis
obj_dx = DarwinSummaryDiagnosis(pathname=c_dar.pathname, fname_darwin_dx_clean=c_dar.fname_darwin_dx_clean)
df_dx = obj_dx.return_df()
df_dx_mets1 = df_dx[df_dx['IS_MET_ICD_BILLING'] == True]
list_col_index = ['DMP_ID', 'AGE_AT_EVENT', col_icd_billing, 'DX_DESCRIPTION']
df_dx_mets1 = df_dx_mets1[list_col_index]
# Add column for sex
df_dx_mets = df_dx_mets1.merge(right=df_samples[[col_id2, col_sex]].drop_duplicates(), how='left', on='DMP_ID')

# TODO: Clinical sample data should not have duplicate cancer type and primary site locations.

### Process data
# Load RDN mapping
obj_met_map_rdn = MetastaticSpreadMappingRND(path=const.pathname,
                                             fname_all_sites=const.fname_mapping_rdn_all_sites,
                                             fname_hematogenous=const.fname_mapping_rdn_hematogenous,
                                             fname_localext=const.fname_mapping_rdn_localext,
                                             fname_lymphatic=const.fname_mapping_rdn_lymphatic,
                                             fname_site_map=const.fname_mapping_rdn_site_map,
                                             fname_billing_map=const.fname_mapping_rdn_billing_map,
                                             fname_billing_code_dict=const.fname_mapping_rdn_to_billing_codes)
# Obtain Renzo's mapping
obj_mapping = OrganMappingAnalysisRND(obj_met_map=obj_met_map_rdn)

# Annotate diagnosis table of ICD billings with renzo's mapping of metastatic sites
df_met_sites_dx = obj_mapping.annotate_icd_billing_met_dx(df_dx_mets=df_dx_mets, col_icd_billing=col_icd_billing, col_sex=col_sex)


df_met_rdn_anno = obj_mapping.create_sample_to_icd_billing_met_mapping(df_dx=df_dx_mets,
                                                                       col_icd_billing=col_icd_billing,
                                                                       col_sex=col_sex,
                                                                       df_samples=df_samples,
                                                                       col_primary_site=col_primary_site,
                                                                       col_met_site=col_met_site,
                                                                       label_dist_ln=True)

t = df_met_rdn_anno.groupby(['DMP_ID', 'CANCER_TYPE'])['PRIMARY_SITE_RDN_MAP'].nunique()
t1 = t[t>1].reset_index()['DMP_ID']

t3 = df_met_rdn_anno[df_met_rdn_anno['DMP_ID'].isin(t1)]
t3.head(100)




# Save RDN annotations
df_met_rdn_anno.to_csv(fname_save_anno, index=False)
t.head(100)

tmp = 0
