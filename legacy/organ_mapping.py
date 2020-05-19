""""
organ_mapping.py

By Chris Fong - MSKCC 2018

This class will take in a pandas series of presumably ICDO/ICD9 DXs and return a pandas series of the same length
containing an aggregated term corresponding to the organ site
"""
import pandas as pd
import os
from organ_mapping_impact_to_oncotree import _mapping_impact_met_site_to_oncotree
from organ_mapping_keyword_to_oncotree import _mapping_site_keyword_to_oncotree
from organ_mapping_icd_o_manual import _mapping_seer_icd_o_code_to_oncotree
from organ_mapping_icd_billing_manual import _mapping_seer_icd_9_10_code_to_oncotree, _mapping_icd_9_10_to_oncotree, _mapping_mets_icd_9_10_to_oncotree


class OrganMapping(object):
    def __init__(self):
        # Mappings for impact samples (legacy)
        self.map_dict_by_impact_site = None
        self.map_dict_dx_by_icd9_code = None
        self.map_dict_dx_by_keyword = None

        # Mappings for patient dx
        self.map_dict_by_seer_icd_o = None
        self.map_dict_by_seer_icd_10 = None
        self.map_dict_met_dx_by_icd10_code = None

        # Generate mappings for Oncotree organ sites
        self._init_organ_mapping()

    def _init_organ_mapping(self):
        # Generate mappings for organ sites from IMPACT (cbio) annotations (Mapping by Francisco)
        self.map_dict_by_impact_site = _mapping_impact_met_site_to_oncotree()
        # Generate mapping of common keywords to oncotree
        self.map_dict_dx_by_keyword = _mapping_site_keyword_to_oncotree()
        # Generate mappings for organ sites from ICD9 (Direct mapping of ICD10 to Oncotree (Legacy)) # TODO: This can be removed
        self.map_dict_dx_by_icd9_code = _mapping_icd_9_10_to_oncotree()

        # Generate mappings for Oncotree organ sites from ICD-O SEER Categories
        self.map_dict_by_seer_icd_o = _mapping_seer_icd_o_code_to_oncotree()
        # Generate mappings for Oncotree organ sites from ICD-9/10 SEER Categories
        self.map_dict_by_seer_icd_10 = _mapping_seer_icd_9_10_code_to_oncotree()
        # Generate mappings for Oncotree organ sites from ICD-9/10 MET codes
        self.map_dict_met_dx_by_icd10_code = _mapping_mets_icd_9_10_to_oncotree()

        return None

    def wrapper_map_dx_to_oncotree_tissue_types(self, df):
        # Create oncotree mapping column
        df = df.assign(DX_ORGAN_SITE=None)

        # Process ICD-O codes first
        df = self._map_dx_to_oncotree_tissue_types(df, process=0)

        # Process ICD-9/10 met codes
        df = self._map_dx_to_oncotree_tissue_types(df, process=1)

        # Process remaining ICD-9/10 malignant (and benign?) codes
        df = self._map_dx_to_oncotree_tissue_types(df, process=2)

        # Remove the unannotated organ sites
        df['DX_ORGAN_SITE'] = df['DX_ORGAN_SITE'].fillna('UNMAPPED')

        return df

    def _map_dx_to_oncotree_tissue_types(self, df, process):
        if process == 0:
            # Map ICD-O dx primary codes using SEER Categories
            cols_icdo = ['CATEGORY1', 'CATEGORY2', 'CATEGORY3', 'CATEGORY4', 'TM_SITE_CD']
            df_icdo = df.loc[df['TM_HIST_CD'].notnull(), cols_icdo]
            dict_mapping = self.map_dict_by_seer_icd_o
        elif process == 1:
            # Map ICD-9/10 met dx codes to oncotree organ types
            cols_icdo = ['ICD-9/10 Dx Code']
            df_icdo = df.loc[df['IS_MET_ICD_BILLING'] == 1, cols_icdo]
            dict_mapping = self.map_dict_met_dx_by_icd10_code
        elif process == 2:
            # Map ICD-9/10 dx malignant (and benign?) codes using SEER Categories
            cols_icdo = ['CATEGORY1', 'CATEGORY2', 'CATEGORY3', 'CATEGORY4', 'ICD-9/10 Dx Code']
            logic_icd10_1 = df['Diagnosis Description'] != 'In situ, benign or unknown behavior neoplasm'
            logic_icd10_2 = df['ICD-9/10 Dx Code'].notnull()
            logic_icd10_3 = df['IS_MET_ICD_BILLING'] == False
            df_icdo = df.loc[logic_icd10_1 & logic_icd10_2 & logic_icd10_3, cols_icdo]
            dict_mapping = self.map_dict_by_seer_icd_10

        # Get list of keys
        organ_site_list = []

        # For all organ dictionaries, rename site of biopsy
        for j in range(df_icdo.shape[1]):
            current_series = df_icdo.iloc[:, j]

            for i in range(len(dict_mapping)):
                organ_site = list(dict_mapping[i].keys())[0]
                organ_site_list.append(organ_site)
                contains_key = '|'.join(list(dict_mapping[i].values())[0])
                logic_map = current_series.str.contains(contains_key).fillna(False)
                # Keep track of appended organ mappings
                if i == 0:
                    logic_map_all = logic_map
                else:
                    logic_map_all = logic_map_all | logic_map

                current_series.loc[logic_map] = organ_site

            # Place back into dataframe
            df.loc[current_series[logic_map_all].index, 'DX_ORGAN_SITE'] = current_series[logic_map_all]

        return df

    def map_impact_sites_to_organs(self, series):
        # This function will map clinical sample metastatic tumor sites to an aggregated site name
        series = series[series.notnull()]

        # Make sure site names are uppercase
        series_normalized = series.copy()
        series_normalized = series_normalized.str.upper()

        # Remove parentheses from series
        series_normalized = series_normalized.str.replace(r'\(|\)', '')

        # TODO: redo regex pattern to not give warning
        # Get list of keys
        organ_site_list = []

        # For all organ dictionaries, rename site of biopsy
        for i in range(len(self.map_dict_by_impact_site)):
            organ_site = list(self.map_dict_by_impact_site[i].keys())[0]
            organ_site_list.append(organ_site)
            contains_key = '|'.join(list(self.map_dict_by_impact_site[i].values())[0])
            logic_map = series_normalized.str.contains(contains_key).fillna(False)
            series_normalized.loc[logic_map] = list(self.map_dict_by_impact_site[i].keys())[0]
            if i == 0:
                logic_map_all = logic_map
            else:
                logic_map_all = logic_map_all | logic_map

        # Remove the unannotated organ sites
        series_normalized[~series_normalized.isin(organ_site_list)] = ''

        return series_normalized

    def map_dx_to_organs(self, series):
        # This function is used primarily in the darwin diagnosis class to map dx ICD9/10 code descriptions to
        # an oncotree organ site

        # Make sure site names are uppercase
        series_normalized = series.copy()
        series_normalized = series_normalized.str.upper()

        # Get list of keys
        organ_site_list = []

        # For all organ dictionaries, rename site of biopsy
        for i in range(len(self.map_dict_dx_by_icd9_code)):
            organ_site = list(self.map_dict_dx_by_icd9_code[i].keys())[0]
            organ_site_list.append(organ_site)
            contains_key = '|'.join(list(self.map_dict_dx_by_icd9_code[i].values())[0])
            logic_map = series_normalized.str.contains(contains_key).fillna(False)
            series_normalized.loc[logic_map] = organ_site

        # Remove the unannotated organ sites
        series_normalized[~series_normalized.isin(organ_site_list)] = ''

        return series_normalized

    def map_keywords_to_organs(self, series):
        # This function is used for standardizing a pandas series of text entries containing organ keywords
        # to oncotree organ sites

        # Make sure site names are uppercase
        series = series.str.upper()
        series_normalized = series.copy()

        # Get list of keys
        organ_site_list = []

        for i in range(len(self.map_dict_dx_by_keyword)):
            organ_site = list(self.map_dict_dx_by_keyword[i].keys())[0]
            organ_site_list.append(organ_site)
            contains_key = '|'.join(list(self.map_dict_dx_by_keyword[i].values())[0])
            logic_map = series.str.contains(contains_key).fillna(False)
            series_normalized.loc[logic_map] = list(self.map_dict_dx_by_keyword[i].keys())[0]
            series_normalized.loc[logic_map] = organ_site

        # Remove the unannotated organ sites
        series_normalized[~series_normalized.isin(organ_site_list)] = ''

        return series_normalized

    def add_met_organ_site_annotation(self, pathname, fname, save=True):
        # With impact data samples file, create oncotree normalized met site annotations (Legacy)
        # TODO: Remove when fully deprecated
        # Make data frame a member variable
        pathfilename = os.path.join(pathname, fname)
        df = pd.read_csv(pathfilename, header=0, delimiter='\t')

        series_met = df['METASTATIC_SITE'].str.upper()
        # Relabel the metastatic sites
        series_met_normalized = self.map_keywords_to_organs(series=series_met)
        # Find labels for not applicable and change
        series_met_normalized[series_met == 'NOT APPLICABLE'] = '-'
        # Map the remaining with impact mapping
        series_remaining = series_met[series_met_normalized == '']
        series_remaining_normalized = self.map_impact_sites_to_organs(series=series_remaining)

        # Take series_remaining and map to oncotree based
        series_remaining_normalized[series_remaining_normalized == ''] = 'OTHER'

        # Place series remaining back into full series
        series_met_normalized[series_remaining_normalized.index] = series_remaining_normalized

        # Place normalized met site column back into the dataframe
        df = df.assign(METASTATIC_SITE_ONCOTREE_NORM=series_met_normalized)
        df['METASTATIC_SITE_ONCOTREE_NORM'] = df['METASTATIC_SITE_ONCOTREE_NORM'].str.lower()

        if save:
            prefix = fname.rsplit('.')[0]
            fname_new = prefix + '_oncotree_sites.txt'
            pathfilename = os.path.join(pathname, fname_new)
            df.to_csv(pathfilename, sep='\t')
