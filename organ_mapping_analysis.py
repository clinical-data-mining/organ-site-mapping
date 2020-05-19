"""
organ_mapping_analysis.py

This object utilizes Renzo's (RDN) organ site mapping for the IMPACT cohort and it's mapping to ICD9/10 met site codes
to perform analysis on which dx are local, regional, and distant.
Also performs mapping for Hematogenous metastatic dissemination
"""
import pandas as pd


class OrganMappingAnalysisRND(object):
    def __init__(self, obj_met_map):
        # Member variables for inputs
        # Data objects
        self._obj_met_map = obj_met_map
        self._obj_summary = None

        # Column names for mappings
        self._col_rdn_met_map = None
        self._col_rdn_prim_map = None
        self._col_oncotree_map = None
        self._col_billing_map = None

        # Load column names
        self._define_rdn_columns()

    def _define_rdn_columns(self):
        self._col_rdn_met_map = 'METASTATIC_SITE_RDN_MAP'
        self._col_rdn_prim_map = 'PRIMARY_SITE_RDN_MAP'
        self._col_oncotree_map = 'ONCOTREE_MAPPING'
        self._col_billing_map = 'ICD_BILLING_MAPPING'
        self._col_rdn_billing_met_map = 'METASTATIC_SITE_BILLING_RDN'
        self._col_rdn_onco_met_map = 'METASTATIC_SITE_ONCOTREE_RDN'
        # self._col_rdn_billing_prim_map = 'PRIMARY_SITE_BILLING_RDN'
        # self._col_rdn_onco_prim_map = 'PRIMARY_SITE_ONCOTREE_RDN'

    def _merge_with_rn_mappings(self, df):
        # Unpack mapping
        df_map_lymph = self._obj_met_map.df_map_lymph
        df_map_localext = self._obj_met_map.df_map_localext
        df_map_hematogenous = self._obj_met_map.df_map_hematogenous
        df_map_oncotree = self._obj_met_map.df_map_oncotree
        df_map_billing = self._obj_met_map.df_map_icd_mapping

        # ---------------------------------------------------------------------------
        # Lymph node mapping
        right_on = ['PRIMARY_ORGAN_SITE', 'clean_site']
        df_sites1 = df.merge(right=df_map_lymph, how='left',
                             left_on=[self._col_rdn_prim_map, self._col_rdn_met_map],
                             right_on=right_on)
        df_sites1 = df_sites1.drop(columns=right_on)

        # Local extension mapping
        df_sites2 = df_sites1.merge(right=df_map_localext, how='left',
                                    left_on=[self._col_rdn_prim_map, self._col_rdn_met_map],
                                    right_on=right_on)
        df_sites2 = df_sites2.drop(columns=right_on)

        # Hematogenous mapping
        df_sites3 = df_sites2.merge(right=df_map_hematogenous, how='left',
                                    left_on=self._col_rdn_met_map,
                                    right_on='clean_site')
        df_sites3 = df_sites3.drop(columns='clean_site')
        df_sites3 = df_sites3.rename(columns={'grouping': 'hematogenous_grouping'})

        # # Oncotree mapping from RDN primary sites
        # df_sites4 = df_sites3.merge(right=df_map_oncotree, how='left',
        #                             left_on=self._col_rdn_prim_map,
        #                             right_on=self._col_oncotree_map)
        # df_sites4 = df_sites4.drop(columns=['clean_site', self._col_oncotree_map])
        # df_sites4 = df_sites4.rename(columns={'tissue_oncotree': self._col_rdn_onco_prim_map})

        # Oncotree mapping from RDN metastatic sites
        df_sites5 = df_sites3.merge(right=df_map_oncotree, how='left',
                                    left_on=self._col_rdn_met_map,
                                    right_on=self._col_oncotree_map)
        df_sites5 = df_sites5.drop(columns=['clean_site', self._col_oncotree_map])
        df_sites5 = df_sites5.rename(columns={'tissue_oncotree': self._col_rdn_onco_met_map})

        # # Billing mapping from RDN primary sites
        # df_sites6 = df_sites5.merge(right=df_map_billing, how='left',
        #                             left_on=self._col_rdn_prim_map,
        #                             right_on=self._col_billing_map)
        # df_sites6 = df_sites6.drop(columns=['clean_site', self._col_billing_map])
        # df_sites6 = df_sites6.rename(columns={'tissue_icd_billing': self._col_rdn_billing_prim_map})

        # Billing mapping from RDN metastatic sites
        df_sites7 = df_sites5.merge(right=df_map_billing, how='left',
                                    left_on=self._col_rdn_met_map,
                                    right_on=self._col_billing_map)
        df_sites7 = df_sites7.drop(columns=['clean_site', self._col_billing_map])
        df_sites7 = df_sites7.rename(columns={'tissue_icd_billing': self._col_rdn_billing_met_map})

        return df_sites7

    def annotate_icd_billing_met_dx(self, df_dx_mets, col_icd_billing, col_sex):
        # Function that will map primary site and metastatic sample site for all metastatic impact sample

        # Call ICD billing to RDN mapping
        icd_met_spread_mapping = self._obj_met_map.df_icd_code_mapping

        col_icd_bill_2 = icd_met_spread_mapping.columns[1]

        # Create RDN mapping with icd9/10 met dx
        df_dx_mets1 = df_dx_mets.merge(right=icd_met_spread_mapping,
                                       how='left',
                                       left_on=col_icd_billing,
                                       right_on=col_icd_bill_2)

        # REMOVE cases where mets go to female genitals in male patients
        logic_rjt1a = (df_dx_mets1[col_sex] == 'Male')
        logic_rjt1b = (df_dx_mets1[self._col_rdn_met_map] == 'pelvis_femaleGenital')
        logic_rjt1 = logic_rjt1a & logic_rjt1b

        logic_rjt2a = (df_dx_mets1[col_sex] == 'Female')
        logic_rjt2b = (df_dx_mets1[self._col_rdn_met_map] == 'pelvis_maleGenital')
        logic_rjt2 = logic_rjt2a & logic_rjt2b

        df_dx_mets2 = df_dx_mets1[~(logic_rjt1 | logic_rjt2)]

        # If gender column is null, remove duplicates that were generate
        log_sex_null = df_dx_mets2[col_sex].isnull() & (logic_rjt1b | logic_rjt2b)
        df_dx_mets2.loc[log_sex_null, 'METASTATIC_SITE_RDN_MAP'] = pd.np.NaN
        df_dx_mets2 = df_dx_mets2.drop_duplicates()

        # Drop one of the billing code columns
        df_dx_mets2 = df_dx_mets2.drop(columns=[col_icd_bill_2])

        return df_dx_mets2

    def annotate_mapping_impact_met_samples(self, df_samples, col_primary_site, col_met_site, label_dist_ln=False):
        # Annotate clinical sample summary file with primary and metastatic mapping (RDN)
        df_sites = self.annotate_clinical_sample_for_mapping(df_samples=df_samples, col_primary_site=col_primary_site, col_met_site=col_met_site)

        # Merge primary and metastatics RDN annotated data with network mappings
        df_sites3 = self._merge_with_rn_mappings(df=df_sites)

        # Reclassify sites to be LN based on Renzo's mapping
        if label_dist_ln:
            logic_dist_ln = df_sites3['LYMPH_SPREAD'] == 'DISTANT'
            df_sites3.loc[logic_dist_ln, self._col_rdn_billing_met_map] = 'DIST_LYMPH'
            df_sites3.loc[logic_dist_ln, self._col_rdn_onco_met_map] = 'Distant Lymphatic'

        return df_sites3

    def annotate_clinical_sample_for_mapping(self, df_samples, col_primary_site, col_met_site):
        # Renzos organ map annotation
        # Make IMPACT tumor sites upper case
        df_samples = df_samples.assign(PRIMARY_SITE_UPPER=df_samples[col_primary_site].str.upper())
        df_samples = df_samples.assign(METASTATIC_SITE_UPPER=df_samples[col_met_site].str.upper())
        col_met_upper = 'METASTATIC_SITE_UPPER'
        col_prim_upper = 'PRIMARY_SITE_UPPER'

        # Mapping df
        df_map_all = self._obj_met_map.df_map_all_sites

        # Merge mapping to clinical sample file sample site location
        # Primary tumor locations
        df_samples_mapped = df_samples.merge(right=df_map_all, how='left',
                                             left_on=col_prim_upper, right_on='raw_site')
        rename_map_p = {'clean_site': self._col_rdn_prim_map,
                        'clean_site_main': self._col_rdn_prim_map + '_MAIN',
                        'clean_site_secondary': self._col_rdn_prim_map + '_SECONDARY',
                        'origin': 'origin_primary'}
        df_samples_mapped = df_samples_mapped.rename(columns=rename_map_p)
        df_samples_mapped = df_samples_mapped.drop(columns='raw_site')

        # Merge mapping for met tumor locations
        df_samples_mapped = df_samples_mapped.merge(right=df_map_all, how='left',
                                                    left_on=col_met_upper, right_on='raw_site')
        rename_map_m = {'clean_site': self._col_rdn_met_map,
                        'clean_site_main': self._col_rdn_met_map + '_MAIN',
                        'clean_site_secondary': self._col_rdn_met_map + '_SECONDARY',
                        'origin': 'origin_primary'}
        df_samples_mapped = df_samples_mapped.rename(columns=rename_map_m)
        df_samples_mapped = df_samples_mapped.drop(columns=['raw_site', col_prim_upper, col_met_upper])

        return df_samples_mapped

    def create_sample_to_icd_billing_met_mapping(self, df_dx, col_icd_billing, col_sex, df_samples, col_primary_site, col_met_site, label_dist_ln):
        # Create a mapping between the cancer types provided in cbio portal for IMPACT samples
        # and the metastatic sites provided from ICD billing codes (Darwin)
        col_sample_id = 'SAMPLE_ID'
        col_patient_id = 'DMP_ID'
        col_ct = 'CANCER_TYPE'
        cols_impact_data = [col_sample_id, col_patient_id, col_ct, col_sex, col_primary_site, col_met_site]
        df_samples = df_samples[cols_impact_data]
        # Create RDN primary site annotations on clinical sample file
        df_samples_dx_map1 = self.annotate_clinical_sample_for_mapping(df_samples=df_samples,
                                                                       col_primary_site=col_primary_site,
                                                                       col_met_site=col_met_site)
        # Take rows and columns that are needed for mapping
        cols = [col_sample_id, col_patient_id, col_ct, col_primary_site, col_met_site, col_sex, self._col_rdn_prim_map]
        df_samples_dx_map = df_samples_dx_map1[cols]

        # Create RDN metastatic site annotations on ICD billing code table
        df_dx_mets1 = self.annotate_icd_billing_met_dx(df_dx_mets=df_dx, col_icd_billing=col_icd_billing, col_sex=col_sex)
        # Remove sex column
        df_dx_mets1 = df_dx_mets1.drop(columns=[col_sex])

        # Merge met dx info with site data with sample summary
        df_sites_with_dx = df_samples_dx_map.merge(right=df_dx_mets1, how='inner', on=col_patient_id)

        # REMOVE cases where mets go to female genitals in male patients
        logic_rjt1a = (df_sites_with_dx[col_sex] == 'Male')
        logic_rjt1b = (df_sites_with_dx[self._col_rdn_met_map] == 'pelvis_femaleGenital')
        logic_rjt1 = logic_rjt1a & logic_rjt1b

        logic_rjt2a = (df_sites_with_dx[col_sex] == 'Female')
        logic_rjt2b = (df_sites_with_dx[self._col_rdn_met_map] == 'pelvis_maleGenital')
        logic_rjt2 = logic_rjt2a & logic_rjt2b

        df_sites_with_dx2 = df_sites_with_dx[~(logic_rjt1 | logic_rjt2)]

        # Merge primary and metastatic RDN annotated data with network mappings
        df_sites_with_dx5 = self._merge_with_rn_mappings(df=df_sites_with_dx2)

        # Reclassify sites to be LN based on Renzo's mapping
        if label_dist_ln:
            logic_dist_ln = df_sites_with_dx5['LYMPH_SPREAD'] == 'DISTANT'
            df_sites_with_dx5.loc[logic_dist_ln, self._col_rdn_billing_met_map] = 'DIST_LYMPH'
            df_sites_with_dx5.loc[logic_dist_ln, self._col_rdn_onco_met_map] = 'Distant Lymphatic'

        return df_sites_with_dx5

    def mapping_ln(self, save_df=True):
        # TODO (fongc2): Refactor this section.  Currently not functional.
        df_sites_with_dx5 = self._df_mapping_met_icd10_dx

        # Get lymphatic spread
        is_lymph1 = df_sites_with_dx5['LYMPH_SPREAD'].notnull()
        df_sites_with_dx_dist = df_sites_with_dx5[is_lymph1]

        # Group by cancer types
        grp_by = ['CANCER_TYPE', 'CLEAN_SITE', 'LYMPH_SPREAD']
        df_sites_with_dx_grp_lymph = df_sites_with_dx_dist.groupby(grp_by)['DMP_ID'].nunique().reset_index()
        df_sites_with_dx_grp_lymph = df_sites_with_dx_grp_lymph.rename(columns={'DMP_ID': 'MET_COUNTS'})

        # Get patient totals for each cancer type
        df_sites_with_dx_grp_lymph_total = df_sites_with_dx_dist.groupby(['CANCER_TYPE'])[
            'DMP_ID'].nunique().reset_index()
        df_sites_with_dx_grp_lymph_total = df_sites_with_dx_grp_lymph_total.rename(
            columns={'DMP_ID': 'MET_COUNTS_TOTAL'})

        # Merge the grouped frames
        df_sites_with_dx_grp_lymph = df_sites_with_dx_grp_lymph.merge(right=df_sites_with_dx_grp_lymph_total,
                                                                      how='inner', on='CANCER_TYPE')
        # Compute pct of met site dx for each cancer type
        pct_met = df_sites_with_dx_grp_lymph['MET_COUNTS'] / df_sites_with_dx_grp_lymph['MET_COUNTS_TOTAL']
        df_sites_with_dx_grp_lymph = df_sites_with_dx_grp_lymph.assign(MET_PCT=pct_met)

        # Filter out unknown
        df_sites_with_dx_grp_lymph2 = df_sites_with_dx_grp_lymph[df_sites_with_dx_grp_lymph['CLEAN_SITE'] != 'undeterminate_unknown']

        # Save data
        if save_df:
            df_sites_with_dx_grp_lymph2.to_csv('dx_met_site_network_lymph.csv', index=False)

        return df_sites_with_dx_grp_lymph2

    def mapping_local_ext(self, save_df=True):
        # TODO (fongc2): Refactor this section.  Currently not functional.
        df_dx_mapped = self._df_mapping_met_icd10_dx

        # Get mets that are NOT a local extension and not a lymph node
        logic_not_lymph_or_other = (df_dx_mapped['IS_OTHER_MET'] == 0) & \
                                   (df_dx_mapped['IS_OTHER_NON_SPECIFIC_MET'] == 0) & \
                                   (df_dx_mapped['IS_LYMPH_MET'] == 0)
        logic_not_local = df_dx_mapped['LOCAL_EXTENSION'].isnull()
        df_dx_mapped.loc[logic_not_local & logic_not_lymph_or_other, 'LOCAL_EXTENSION'] = 'NOT LOCAL'

        # Drop columns
        cols_drop = ['origin', 'hematogenous_grouping', 'ICD-9/10 Dx Code']
        df_sites_with_dx_not_local = df_dx_mapped.drop(columns=cols_drop)

        # Compute met counts for each organ mapping site within each cancer type
        grp_by = ['CANCER_TYPE', 'CLEAN_SITE', 'LOCAL_EXTENSION']
        df_sites_with_dx_not_local_grp = df_sites_with_dx_not_local.groupby(grp_by)['DMP_ID'].nunique().reset_index()
        df_sites_with_dx_not_local_grp = df_sites_with_dx_not_local_grp.rename(columns={'DMP_ID': 'MET_COUNTS'})

        # Compute total number of met dx for each cancer type
        df_sites_with_dx_grp_not_local_total = df_sites_with_dx_not_local.groupby(['CANCER_TYPE'])['DMP_ID'].nunique().reset_index()
        df_sites_with_dx_grp_not_local_total = df_sites_with_dx_grp_not_local_total.rename(columns={'DMP_ID': 'MET_COUNTS_TOTAL'})
        # Merge total met dx counts
        df_sites_with_dx_not_local_grp = df_sites_with_dx_not_local_grp.merge(right=df_sites_with_dx_grp_not_local_total, how='inner', on='CANCER_TYPE')

        # Compute percentage
        pct_met = df_sites_with_dx_not_local_grp['MET_COUNTS'] / df_sites_with_dx_not_local_grp['MET_COUNTS_TOTAL']
        df_sites_with_dx_not_local_grp = df_sites_with_dx_not_local_grp.assign(MET_PCT=pct_met)

        # Save data
        if save_df:
            df_sites_with_dx_not_local_grp.to_csv('dx_met_site_network_localExt.csv', index=False)

        return df_sites_with_dx_not_local_grp

    def create_mapping_summary_rdn_oncotree(self):
        # TODO (fongc2): Refactor this section.  Currently not functional.
        df_dx_mapped = self._df_mapping_met_icd10_dx

        cols_grp = ['CANCER_TYPE', 'CLEAN_SITE']
        cols_dmp = ['DMP_ID']

        # Melt oncotree met sites
        cols_met = list(df_dx_mapped.columns[df_dx_mapped.columns.str.contains('_MET')])
        cols_met_new = [x.replace('IS_', '').replace('_MET', '') for x in cols_met]
        cols_met_dict = dict(zip(cols_met, cols_met_new))
        df_dx_mapped = df_dx_mapped.rename(columns=cols_met_dict)
        cols_other = set(df_dx_mapped.columns) - set(cols_met_new)

        df_dx_melt = pd.melt(frame=df_dx_mapped, id_vars=cols_dmp+cols_grp,
                             value_vars=cols_met_new, var_name='DX_ORGAN_SITE')
        df_dx_melt = df_dx_melt[df_dx_melt['value'] == 1]

        df = df_dx_melt.groupby(['CANCER_TYPE', 'DX_ORGAN_SITE', 'CLEAN_SITE'])['DMP_ID'].nunique().reset_index()

        return df

    def create_binary_met_sites_impact(self, df):
        ### Create binary table of RDN annotated data
        # Pivot data
        df_to_piv1 = df[['DMP_ID', 'SAMPLE_ID', 'METASTATIC_SITE_BILLING_RDN']]

        df_met_piv = pd.pivot_table(data=df_to_piv1, index='SAMPLE_ID', values='DMP_ID',
                                    columns='METASTATIC_SITE_BILLING_RDN', aggfunc='count', fill_value=0)
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

        return df_met_piv_m
