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
import sys
sys.path.insert(0, 'mappings')
sys.path.insert(0, 'analysis')
import constants_o_sites as const
from organ_mapping_rdn_processing import MetastaticSpreadMappingRND


# Console settings
set_debug_console()

# Filename for output
fname_save_anno = 'mskimpact_clinical_data_organ_site_anno.tsv'

## Load cbioportal clinical data file --------------
# Load ID names
fname = 'mskimpact_clinical_data.tsv'
path = c_dar.pathname
pathfilename1 = os.path.join(path, fname)
df_samples1 = pd.read_csv(pathfilename1, header=0, low_memory=False, sep='\t')

# For genie, fix ids
col_id = 'SAMPLE_ID'
col_id2 = 'DMP_ID'
col_ct = 'CANCER_TYPE'
col_sex = 'SEX'
col_prim_site = 'PRIMARY_SITE'
col_met_site = 'METASTATIC_SITE'
col_sample_type = 'SAMPLE_TYPE'
col_rep = {'Patient ID': col_id2,
           'Sample ID': col_id,
           'Sex': col_sex,
           'Cancer Type': col_ct,
           'Primary Tumor Site': col_prim_site,
           'Metastatic Site': col_met_site,
           'Sample Type': col_sample_type}
df_samples1 = df_samples1.rename(columns=col_rep)
df_samples = df_samples1[list(col_rep.values())]
# df_metatrop_met = df_samples[df_samples[col_sample_type] == 'Metastasis']
# df_metatrop_prim = df_samples[df_samples[col_sample_type] != 'Metastasis']
df_metatrop_met = df_samples

# Load RDN mapping
obj_met_map_rdn = MetastaticSpreadMappingRND(path=const.pathname,
                                             fname_all_sites=const.fname_mapping_rdn_all_sites,
                                             fname_hematogenous=const.fname_mapping_rdn_hematogenous,
                                             fname_localext=const.fname_mapping_rdn_localext,
                                             fname_lymphatic=const.fname_mapping_rdn_lymphatic,
                                             fname_site_map=const.fname_mapping_rdn_site_map,
                                             fname_billing_map=const.fname_mapping_rdn_billing_map,
                                             fname_billing_code_dict=const.fname_mapping_rdn_to_billing_codes)

# Load annoations object
obj_mapping = OrganMappingAnalysisRND(obj_met_map=obj_met_map_rdn)

# Annotate IMPACT sample site data
df_met_sites_impact = obj_mapping.annotate_mapping_impact_met_samples(df_samples=df_metatrop_met,
                                                                      col_primary_site=col_prim_site,
                                                                      col_met_site=col_met_site,
                                                                      label_dist_ln=True)

# Save RDN annotations
pathfilename_save = os.path.join(path, fname_save_anno)
df_met_sites_impact.to_csv(pathfilename_save, index=False, sep='\t')
