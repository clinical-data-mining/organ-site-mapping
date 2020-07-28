""""
organ_mapping_icd_billing_to_rdn.py

By Chris Fong - MSKCC 2020

 This script contains functions that will create a map between ICD billing codes for secondary malignant neoplasm
 to organ sites defined by Renzo DiNatale
"""
import sys
import pandas as pd
import argparse


def create_icd_billing_to_rdn_mapping(fname_save=None):
    # Create mapping from ICD10 codes to met sites
    icd_met_dict = _mapping_icd_9_10_to_rdn_notation()
    # Convert list of dictionary of lists to dataframe
    icd_met_mapping = _process_met_map_dictionary(icd_met_dict=icd_met_dict)

    if fname_save is not None:
        icd_met_mapping.to_csv(fname_save, index=False, sep=',')

    return icd_met_mapping


def _process_met_map_dictionary(icd_met_dict):
    # unpack dictionary
    col_site = 'METASTATIC_SITE_RDN_MAP'
    col_icd_billing = 'ICD_BILLING_CODE'
    t = [pd.DataFrame(l) for l in icd_met_dict]
    df = pd.concat(t, sort=True, ignore_index=True)

    # Melt all values
    df_melt = pd.melt(frame=df, value_vars=df.columns, var_name=col_site, value_name=col_icd_billing)

    # Remove null values
    icd_met_mapping = df_melt[df_melt[col_icd_billing].notnull()].reset_index(drop=True)

    return icd_met_mapping


def _mapping_icd_9_10_to_rdn_notation():
    # Creates list of dictionaries that will map ICD9/10 codes to an organ based on Renzo Dinatale

    # Initialize list for mapping from met sample biopsy site to organ
    map_list = []

    # abdomen_abdominalwall

    # abdomen_biliary
    pat_list = ['197.8', 'C78.89', 'C78.80']
    mapping = {'abdomen_biliary': pat_list}
    map_list.append(mapping)

    # abdomen_foregut
    pat_list = []
    mapping = {'abdomen_foregut': pat_list}
    map_list.append(mapping)

    # abdomen_midgut
    pat_list = ['197.4', 'C78.4']
    mapping = {'abdomen_midgut': pat_list}
    map_list.append(mapping)

    # abdomen_hindgut
    pat_list = []
    mapping = {'abdomen_hindgut': pat_list}
    map_list.append(mapping)

    # abdomen_liver
    pat_list = ['197.7', 'C78.7', 'C7B.02', '209.72']
    mapping = {'abdomen_liver': pat_list}
    map_list.append(mapping)

    # abdomen_node
    pat_list = ['196.2', 'C77.2']
    mapping = {'abdomen_node': pat_list}
    map_list.append(mapping)

    # abdomen_peritoneum.serosa
    pat_list = ['197.6', 'C78.6', 'C7B.04']
    mapping = {'abdomen_peritoneum.serosa': pat_list}
    map_list.append(mapping)

    # abdomen_skin
    pat_list = []
    mapping = {'abdomen_skin': pat_list}
    map_list.append(mapping)

    # abdomen_softTissue
    pat_list = []
    mapping = {'abdomen_softTissue': pat_list}
    map_list.append(mapping)

    # abdomen_spleen
    pat_list = []
    mapping = {'abdomen_spleen': pat_list}
    map_list.append(mapping)

    # abdomen_unknown
    pat_list = []
    mapping = {'abdomen_unknown': pat_list}
    map_list.append(mapping)

    # axilla_node
    pat_list = ['C77.3', '196.3']
    mapping = {'axilla_node': pat_list}
    map_list.append(mapping)

    # back_bone.spine
    pat_list = []
    mapping = {'back_bone.spine': pat_list}
    map_list.append(mapping)

    # back_softTissue
    pat_list = []
    mapping = {'back_softTissue': pat_list}
    map_list.append(mapping)

    # chest_bone
    pat_list = []
    mapping = {'chest_bone': pat_list}
    map_list.append(mapping)

    # chest_breast
    pat_list = ['C79.81', '198.81']
    mapping = {'chest_breast': pat_list}
    map_list.append(mapping)

    # chest_chestwall

    # chest_lung
    pat_list = ['197.0', 'C78.00', 'C78.01', 'C78.02']
    mapping = {'chest_lung': pat_list}
    map_list.append(mapping)

    # chest_pleura.serosa
    pat_list = ['197.2', 'C78.2']
    mapping = {'chest_pleura.serosa': pat_list}
    map_list.append(mapping)

    # chest_unknown
    pat_list = ['C78.3']
    mapping = {'chest_unknown': pat_list}
    map_list.append(mapping)

    # head_bone
    pat_list = []
    mapping = {'head_bone': pat_list}
    map_list.append(mapping)

    # head_cns
    pat_list = ['C79.31', '198.3', '198.4']
    mapping = {'head_cns': pat_list}
    map_list.append(mapping)

    # head_exocrineGland

    # head_eye
    pat_list = []
    mapping = {'head_eye': pat_list}
    map_list.append(mapping)

    # head_oral
    pat_list = []
    mapping = {'head_oral': pat_list}
    map_list.append(mapping)

    # head_sinonasal
    pat_list = []
    mapping = {'head_sinonasal': pat_list}
    map_list.append(mapping)

    # head_skin
    pat_list = []
    mapping = {'head_skin': pat_list}
    map_list.append(mapping)

    # head_softTissue
    pat_list = []
    mapping = {'head_softTissue': pat_list}
    map_list.append(mapping)

    # head_unknown
    pat_list = []
    mapping = {'head_unknown': pat_list}
    map_list.append(mapping)

    # intransitMet_node

    # lowerExtremity_bone
    pat_list = []
    mapping = {'lowerExtremity_bone': pat_list}
    map_list.append(mapping)

    # lowerExtremity_node
    pat_list = ['196.5', 'C77.4']
    mapping = {'lowerExtremity_node': pat_list}
    map_list.append(mapping)

    # lowerExtremity_skin
    pat_list = []
    mapping = {'lowerExtremity_skin': pat_list}
    map_list.append(mapping)

    # lowerExtremity_softTissue
    pat_list = []
    mapping = {'lowerExtremity_softTissue': pat_list}
    map_list.append(mapping)

    # mediastinum_foregut
    pat_list = ['C78.1', '197.1']
    mapping = {'mediastinum_foregut': pat_list}
    map_list.append(mapping)

    # mediastinum_heart
    pat_list = []
    mapping = {'mediastinum_heart': pat_list}
    map_list.append(mapping)

    # mediastinum_node
    pat_list = ['196.1', 'C77.1']
    mapping = {'mediastinum_node': pat_list}
    map_list.append(mapping)

    # mediastinum_pericardium.serosa
    pat_list = []
    mapping = {'mediastinum_pericardium.serosa': pat_list}
    map_list.append(mapping)

    # mediastinum_thymus
    pat_list = []
    mapping = {'mediastinum_thymus': pat_list}
    map_list.append(mapping)

    # mediastinum_trachea
    pat_list = []
    mapping = {'mediastinum_trachea': pat_list}
    map_list.append(mapping)

    # meninges
    pat_list = ['C79.32']
    mapping = {'meninges': pat_list}
    map_list.append(mapping)

    # neck_unknown
    pat_list = []
    mapping = {'neck_unknown': pat_list}
    map_list.append(mapping)

    # neck_node
    pat_list = ['C77.0', '196.0']
    mapping = {'neck_node': pat_list}
    map_list.append(mapping)

    # neck_respiratoryTract
    pat_list = ['C78.3', 'C78.30', 'C78.39', '197.3']
    mapping = {'neck_respiratoryTract': pat_list}
    map_list.append(mapping)

    # neck_pharynx
    pat_list = []
    mapping = {'neck_pharynx': pat_list}
    map_list.append(mapping)

    # neck_thyroid
    pat_list = []
    mapping = {'neck_thyroid': pat_list}
    map_list.append(mapping)

    # pelvis_bladder
    pat_list = ['C79.11']
    mapping = {'pelvis_bladder': pat_list}
    map_list.append(mapping)

    # pelvis_bone
    pat_list = []
    mapping = {'pelvis_bone': pat_list}
    map_list.append(mapping)

    # pelvis_cervix
    pat_list = []
    mapping = {'pelvis_cervix': pat_list}
    map_list.append(mapping)

    # pelvis_femaleGenital
    pat_list = ['C79.82', '198.82']
    mapping = {'pelvis_femaleGenital': pat_list}
    map_list.append(mapping)

    # pelvis_hindgut
    pat_list = ['197.5', 'C78.5']
    mapping = {'pelvis_hindgut': pat_list}
    map_list.append(mapping)

    # pelvis_maleGenital
    pat_list = ['C79.82', '198.82']
    mapping = {'pelvis_maleGenital': pat_list}
    map_list.append(mapping)

    # pelvis_node
    pat_list = ['C77.5', '196.6']
    mapping = {'pelvis_node': pat_list}
    map_list.append(mapping)

    # pelvis_unknown
    pat_list = []
    mapping = {'pelvis_unknown': pat_list}
    map_list.append(mapping)

    # pelvis_ovary
    pat_list = ['C79.60', 'C79.61', 'C79.62', '198.6']
    mapping = {'pelvis_ovary': pat_list}
    map_list.append(mapping)

    # pelvis_prostate
    pat_list = []
    mapping = {'pelvis_prostate': pat_list}
    map_list.append(mapping)

    # pelvis_urinaryTract
    pat_list = ['198.1', 'C79.10', 'C79.19']
    mapping = {'pelvis_urinaryTract': pat_list}
    map_list.append(mapping)

    # pelvis_uterus
    pat_list = []
    mapping = {'pelvis_uterus': pat_list}
    map_list.append(mapping)

    # perineum_femaleGenital
    pat_list = []
    mapping = {'perineum_femaleGenital': pat_list}
    map_list.append(mapping)

    # perineum_maleGenital
    pat_list = []
    mapping = {'perineum_maleGenital': pat_list}
    map_list.append(mapping)

    # perineum_skin
    pat_list = []
    mapping = {'perineum_skin': pat_list}
    map_list.append(mapping)

    # perineum_testis
    pat_list = []
    mapping = {'perineum_testis': pat_list}
    map_list.append(mapping)

    # perineum_unknown

    # retroperitoneum_adrenal
    pat_list = ['C79.70', 'C79.71', 'C79.72', '198.7']
    mapping = {'retroperitoneum_adrenal': pat_list}
    map_list.append(mapping)

    # retroperitoneum_bloodVessel

    # retroperitoneum_kidney
    pat_list = ['198.0', 'C79.01', 'C79.02']
    mapping = {'retroperitoneum_kidney': pat_list}
    map_list.append(mapping)

    # retroperitoneum_node

    # retroperitoneum_pancreas
    pat_list = []
    mapping = {'retroperitoneum_pancreas': pat_list}
    map_list.append(mapping)

    # retroperitoneum_softTissue
    pat_list = []
    mapping = {'retroperitoneum_softTissue': pat_list}
    map_list.append(mapping)

    # retroperitoneum_unknown

    # retroperitoneum_urinaryTract
    pat_list = ['C79.00']
    mapping = {'retroperitoneum_urinaryTract': pat_list}
    map_list.append(mapping)

    # undeterminate_bloodVessel

    # undeterminate_bone
    pat_list = ['C7B.03', 'C79.51', 'C79.52', '198.5']
    mapping = {'undeterminate_bone': pat_list}
    map_list.append(mapping)

    # undeterminate_nerve
    pat_list = ['C79.40', 'C79.49']
    mapping = {'undeterminate_nerve': pat_list}
    map_list.append(mapping)

    # undeterminate_node
    pat_list = ['196.8', '196.9', 'C77.8', 'C77.9', 'C7B.01']
    mapping = {'undeterminate_node': pat_list}
    map_list.append(mapping)

    # undeterminate_skin
    pat_list = ['198.2', 'C79.2']
    mapping = {'undeterminate_skin': pat_list}
    map_list.append(mapping)

    # undeterminate_softTissue
    pat_list = []
    mapping = {'undeterminate_softTissue': pat_list}
    map_list.append(mapping)

    # undeterminate_unknown
    pat_list = ['C7B.00', 'C7B.09', 'C79.89', 'C79.9', '198.89', 'C7B.8', 'C7B.1']
    mapping = {'undeterminate_unknown': pat_list}
    map_list.append(mapping)

    # upperExtremity_bone
    pat_list = []
    mapping = {'upperExtremity_bone': pat_list}
    map_list.append(mapping)

    # upperExtremity_skin
    pat_list = []
    mapping = {'upperExtremity_skin': pat_list}
    map_list.append(mapping)

    # upperExtremity_softTissue
    pat_list = []
    mapping = {'upperExtremity_softTissue': pat_list}
    map_list.append(mapping)

    return map_list


def create_cli_parser():
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "-o",
        nargs="*",
        type=str,  # any type/callable can be used here
        default='output.csv',
    )
    CLI.add_argument('-help', action='help', default=argparse.SUPPRESS,
                     help='-o <Output filename>')

    return CLI


def main(argv):
    # Parse command line
    CLI = create_cli_parser()
    # parse the command line
    args = CLI.parse_args(argv)

    if type(args.o) == list:
        outputfile = args.o[0]
    else:
        outputfile = args.o

    if not outputfile:
        print('for help: python get_xnat_dicom.py -h')
        sys.exit(2)
    else:
        print(outputfile)

    # ------------------------------------------------------------------------------------------


    complete = create_icd_billing_to_rdn_mapping(fname_save=outputfile)

    sys.exit(0)

if __name__ == "__main__":
    # Debug example:
    # argv = [
    #     '-o', 'map_icd_codes_to_rdn_sites.csv'
    # ]
    # main(argv)

    # Command line example:
    # python organ_mapping_icd_billing_to_rdn.py -o "map_icd_codes_to_rdn_sites.csv"

    # print(sys.argv[1:])
    main(sys.argv[1:])
