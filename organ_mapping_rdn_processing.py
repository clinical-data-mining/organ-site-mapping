""""
organ_mapping_rnd_processing.py

By Chris Fong - MSKCC 2020

This script will create an object that will load all required file from Renzo DiNatale
"""
import pandas as pd
import os


class MetastaticSpreadMappingRND(object):
    def __init__(self, path, fname_all_sites, fname_hematogenous, fname_localext, fname_lymphatic, fname_site_map, fname_billing_map, fname_billing_code_dict):
        self.pathname = path
        self.fname_all_sites = fname_all_sites
        self.fname_hematogenous = fname_hematogenous
        self.fname_localext = fname_localext
        self.fname_lymphatic = fname_lymphatic
        self.fname_site_map = fname_site_map
        self.fname_billing_map = fname_billing_map
        self.fname_billing_code_dict = fname_billing_code_dict

        self.df_map_all_sites = None
        self.df_map_hematogenous = None
        self.df_map_localext = None
        self.df_map_lymph = None
        self.df_map_oncotree = None
        self.df_map_icd_mapping = None
        self.df_icd_code_mapping = None

        # TODO: define these common column names outside of this class
        self._value_name_localExt = 'LOCAL_EXTENSION'
        self._value_name_lymph_spread = 'LYMPH_SPREAD'
        self._value_name_oncotree_map = 'ONCOTREE_MAPPING'
        self._value_name_billing_map = 'ICD_BILLING_MAPPING'

        self._process_tables()

    def _process_tables(self):
        # Load diagnosis table
        print('Loading mapping tables')
        # All site mapping
        pathfilename = os.path.join(self.pathname, self.fname_all_sites)
        df_map_all_sites = pd.read_csv(pathfilename, header=0)
        df_map_all_sites = self._clean_mapping_sites(df=df_map_all_sites)
        self.df_map_all_sites = df_map_all_sites

        # Site hematogenous
        pathfilename = os.path.join(self.pathname, self.fname_hematogenous)
        df_map_hematogenous = pd.read_csv(pathfilename, header=0)
        df_map_hematogenous = df_map_hematogenous.drop(columns='Unnamed: 0')
        self.df_map_hematogenous = df_map_hematogenous

        # Site local extension
        pathfilename = os.path.join(self.pathname, self.fname_localext)
        df_map_localext = pd.read_csv(pathfilename, header=0)
        df_map_localext = df_map_localext.rename(columns={'Unnamed: 0': 'PRIMARY_ORGAN_SITE'})
        df_map_localext = self._melt_mapping_tables(df=df_map_localext, value_name=self._value_name_localExt)
        self.df_map_localext = df_map_localext

        # Lymphatic mapping
        pathfilename = os.path.join(self.pathname, self.fname_lymphatic)
        df_map_lymph = pd.read_csv(pathfilename, header=0)
        df_map_lymph = df_map_lymph.rename(columns={'Unnamed: 0': 'PRIMARY_ORGAN_SITE'})
        df_map_lymph = self._melt_mapping_tables(df=df_map_lymph, value_name=self._value_name_lymph_spread)
        self.df_map_lymph = df_map_lymph

        # Site oncotree site mapping
        pathfilename = os.path.join(self.pathname, self.fname_site_map)
        df_oncotree_map = pd.read_csv(pathfilename, header=0)
        df_oncotree_map = df_oncotree_map.drop(columns=['notes'])
        df_oncotree_map = self._melt_mapping_tables(df=df_oncotree_map, value_name=self._value_name_oncotree_map)
        # Replace
        df_oncotree_map[self._value_name_oncotree_map] = df_oncotree_map[self._value_name_oncotree_map].replace(['abdomen_foregut (Stomach)', 'mediastinum_foregut (Esophagus)'],
                                                                                          ['abdomen_foregut', 'mediastinum_foregut'])
        df_oncotree_map1 = df_oncotree_map[df_oncotree_map[self._value_name_oncotree_map].notnull()]
        self.df_map_oncotree = df_oncotree_map1

        # ICD billing site mapping
        pathfilename = os.path.join(self.pathname, self.fname_billing_map)
        df_billing_map = pd.read_csv(pathfilename, header=0)
        df_billing_map = self._melt_mapping_tables(df=df_billing_map, value_name=self._value_name_billing_map)
        # Replace
        df_billing_map[self._value_name_billing_map] = df_billing_map[self._value_name_billing_map].replace(
            ['abdomen_foregut (Stomach)', 'mediastinum_foregut (Esophagus)'],
            ['abdomen_foregut', 'mediastinum_foregut'])
        df_billing_map1 = df_billing_map[df_billing_map[self._value_name_billing_map].notnull()]
        self.df_map_icd_mapping = df_billing_map1

        # Create mapping from ICD10 codes to rdn met sites
        pathfilename = os.path.join(self.pathname, self.fname_billing_code_dict)
        icd_met_dict = pd.read_csv(pathfilename, header=0)
        self.df_icd_code_mapping = icd_met_dict

    def _clean_mapping_sites(self, df):
        # Clean the site mapping
        df['raw_site'] = df['raw_site'].str.upper()
        # Strip text to remove blanks
        df['raw_site'] = df['raw_site'].str.strip()
        df = df.drop_duplicates().reset_index(drop=True)
        clean_site_columns = df['clean_site'].str.split('_', expand=True)
        clean_site_columns = clean_site_columns.rename(columns={0: 'clean_site_main', 1: 'clean_site_secondary'})
        df_map_all = pd.concat([df, clean_site_columns], axis=1, sort=False)

        return df_map_all

    def _melt_mapping_tables(self, df, value_name):
        id_vars = df.columns[0]
        value_vars = df.columns[1:]
        var_name = 'clean_site'
        df_melt = df.melt(id_vars=id_vars, value_vars=value_vars, value_name=value_name, var_name=var_name)

        return df_melt
