


def _mapping_mets_icd_9_10_to_oncotree():
    # Creates list of dictionaries that will map ICD9/10 codes to an organ

    # Initialize list for mapping from met sample biopsy site to organ
    map_list = []

    # MEDIASTINUM
    pat_list = ['197.1', 'C78.1']
    mapping = {'MEDIASTINUM': pat_list}
    map_list.append(mapping)

    # Other, specified
    pat_list = ['198.89', 'C79.89', 'C7B.09', 'C7B.8', 'C7B.1']
    mapping = {'OTHER': pat_list}
    map_list.append(mapping)

    # Other, non-specific
    pat_list = ['C79.9', 'C7B.00']
    mapping = {'OTHER NON SPECIFIC': pat_list}
    map_list.append(mapping)

    # Genital
    pat_list = ['198.82', 'C79.82']
    mapping = {'GENITAL NON SPECIFIC': pat_list}
    map_list.append(mapping)

    # Adrenal gland map
    pat_list = ['198.7', 'C79.70', 'C79.71', 'C79.72']
    mapping = {'ADRENAL GLAND': pat_list}
    map_list.append(mapping)

    # # Ampulla of vater
    # pat_list = []
    # mapping = {'AMPULLA OF VATER': pat_list}
    # map_list.append(mapping)

    # BILIARY TRACT
    pat_list = ['197.8', 'C78.89', 'C78.80']
    mapping = {'BILIARY TRACT': pat_list}
    map_list.append(mapping)

    # BLADDER OR URINARY TRACT
    pat_list = ['198.1', 'C79.10', 'C79.11', 'C79.19']
    mapping = {'BLADDER OR URINARY TRACT': pat_list}
    map_list.append(mapping)

    # # BLOOD
    # pat_list = []
    # mapping = {'MYELOID': pat_list}
    # map_list.append(mapping)

    # BONE
    pat_list = ['198.5', 'C79.51', 'C79.52', 'C7B.03']
    mapping = {'BONE': pat_list}
    map_list.append(mapping)

    # BOWEL
    pat_list = ['197.4', '197.5', 'C78.4', 'C78.5', 'C78.89']
    mapping = {'BOWEL': pat_list}
    map_list.append(mapping)

    # Breast map
    pat_list = ['198.81', 'C79.81']
    mapping = {'BREAST': pat_list}
    map_list.append(mapping)

    # CNS/Brain map
    pat_list = ['198.3', '198.4', 'C79.31', 'C79.32']
    mapping = {'CNS/BRAIN': pat_list}
    map_list.append(mapping)

    # # Cervix map
    # pat_list = []
    # mapping = {'CERVIX': pat_list}
    # map_list.append(mapping)

    # # Esophagus/Stomach map
    # pat_list_esoph = []
    # pat_list_stomach = []
    # pat_list = pat_list_esoph + pat_list_stomach
    # mapping = {'ESOPHAGUS OR STOMACH': pat_list}
    # map_list.append(mapping)

    # # Eye map
    # pat_list = []
    # mapping = {'EYE': pat_list}
    # map_list.append(mapping)

    # Head and Neck
    pat_list = ['197.3', 'C78.3']
    mapping = {'HEAD AND NECK': pat_list}
    map_list.append(mapping)

    # Kidney
    pat_list = ['198.0', 'C79.00', 'C79.01', 'C79.02']
    mapping = {'KIDNEY': pat_list}
    map_list.append(mapping)

    # Liver
    pat_list = ['197.7', 'C78.7', 'C7B.02']
    mapping = {'LIVER': pat_list}
    map_list.append(mapping)

    # Lung
    pat_list = ['197.0', 'C78.00', 'C78.01', 'C78.02']
    mapping = {'LUNG': pat_list}
    map_list.append(mapping)

    # Lymph nodes
    pat_list = ['196.0', '196.1', '196.2', '196.3', '196.5', '196.6', '196.8', '196.9',
                'C77.0', 'C77.1', 'C77.2', 'C77.3', 'C77.4', 'C77.5', 'C77.8', 'C77.9',
                'C7B.01']
    mapping = {'LYMPH': pat_list}
    map_list.append(mapping)

    # OVARY OR FALLOPIAN TUBE
    pat_list = ['198.6', 'C79.60', 'C79.61', 'C79.62']
    mapping = {'OVARY OR FALLOPIAN TUBE': pat_list}
    map_list.append(mapping)

    # # Pancreas
    # pat_list = []
    # mapping = {'PANCREAS': pat_list}
    # map_list.append(mapping)
    #
    # # PENIS
    # pat_list = []
    # mapping = {'PENIS': pat_list}
    # map_list.append(mapping)

    # Peripheral Nervous System
    pat_list = ['C79.40', 'C79.49']
    mapping = {'PERIPHERAL NERVOUS SYSTEM': pat_list}
    map_list.append(mapping)

    # PERITONEUM
    pat_list = ['197.6', 'C78.6', 'C7B.04']
    mapping = {'PERITONEUM': pat_list}
    map_list.append(mapping)

    # PLEURA
    pat_list = ['197.2', 'C78.2']
    mapping = {'PLEURA': pat_list}
    map_list.append(mapping)

    # # PROSTATE
    # pat_list = []
    # mapping = {'PROSTATE': pat_list}
    # map_list.append(mapping)

    # SKIN
    pat_list = ['198.2', 'C79.2']
    mapping = {'SKIN': pat_list}
    map_list.append(mapping)

    # # SOFT TISSUE
    # pat_list = []
    # mapping = {'SOFT TISSUE': pat_list}
    # map_list.append(mapping)
    #
    # # TESTIS
    # pat_list = []
    # mapping = {'TESTIS': pat_list}
    # map_list.append(mapping)
    #
    # # THYMUS
    # pat_list = []
    # mapping = {'THYMUS': pat_list}
    # map_list.append(mapping)

    # # THYROID
    # pat_list = []
    # mapping = {'THYROID': pat_list}
    # map_list.append(mapping)
    #
    # # UTERUS
    # pat_list = []
    # mapping = {'UTERUS': pat_list}
    # map_list.append(mapping)
    #
    # # VULVA OR VAGINA
    # pat_list = []
    # mapping = {'VULVA OR VAGINA': pat_list}
    # map_list.append(mapping)

    return map_list


def _mapping_seer_icd_9_10_code_to_oncotree():
    # Creates list of dictionaries that will map keywords to the oncotree organ
    # Derived from https://seer.cancer.gov/codrecode/1969_d04162012/index.html
    # Initialize list for mapping from met sample biopsy site to organ
    map_list = []

    # Other
    pat_list = ['Trachea, Mediastinum and Other Respiratory Organs', 'Other Digestive Organs',
                'Other Male Genital Organs', 'Other Endocrine including Thymus',
                'Mesothelioma', 'Kaposi Sarcoma', 'Miscellaneous',
                'Other Female Genital Organs']
    mapping = {'OTHER': pat_list}
    map_list.append(mapping)

    # Adrenal gland map
    pat_list = ['C74', '194.0']
    mapping = {'ADRENAL GLAND': pat_list}
    map_list.append(mapping)

    # Ampulla of vater
    pat_list = ['AMPULLA']
    mapping = {'AMPULLA OF VATER': pat_list}
    map_list.append(mapping)

    # BLADDER OR URINARY TRACT
    pat_list = ['Urinary Bladder', 'Ureter', 'Other Urinary Organs']
    mapping = {'BLADDER OR URINARY TRACT': pat_list}
    map_list.append(mapping)

    # BILIARY TRACT
    pat_list = ['Intrahepatic Bile Duct', 'Gallbladder', 'Other Biliary']
    mapping = {'BILIARY TRACT': pat_list}
    map_list.append(mapping)

    # BONE
    pat_list = ['Bones and Joints']
    mapping = {'BONE': pat_list}
    map_list.append(mapping)

    # BOWEL
    pat_list = ['Small Intestine', 'Colon and Rectum',
                'C21.0', 'C21.1', 'C21.2', 'C21.8',
                '154.0', '154.1', '154.2', '154.3', '154.8']
    mapping = {'BOWEL': pat_list}
    map_list.append(mapping)

    # Head and Neck
    pat_list = ['Oral Cavity and Pharynx', 'Larynx', 'Nose, Nasal Cavity and Middle Ear']
    mapping = {'HEAD AND NECK': pat_list}
    map_list.append(mapping)

    # Breast map
    pat_list = ['Breast']
    mapping = {'BREAST': pat_list}
    map_list.append(mapping)

    # CNS/Brain map
    pat_list = ['Brain and Other Nervous System']
    mapping = {'CNS/BRAIN': pat_list}
    map_list.append(mapping)

    # Cervix map
    pat_list = ['Cervix Uteri']
    mapping = {'CERVIX': pat_list}
    map_list.append(mapping)

    # Esophagus/Stomach map
    pat_list_esoph = ['Esophagus']
    pat_list_stomach = ['Stomach']
    pat_list = pat_list_esoph + pat_list_stomach
    mapping = {'ESOPHAGUS OR STOMACH': pat_list}
    map_list.append(mapping)

    # Eye map
    pat_list = ['Eye and Orbit']
    mapping = {'EYE': pat_list}
    map_list.append(mapping)

    # Kidney
    pat_list = ['Kidney and Renal Pelvis']
    mapping = {'KIDNEY': pat_list}
    map_list.append(mapping)

    # Liver
    pat_list = ['Liver']
    mapping = {'LIVER': pat_list}
    map_list.append(mapping)

    # Lung
    pat_list = ['Lung and Bronchus']
    mapping = {'LUNG': pat_list}
    map_list.append(mapping)

    # Lymph nodes
    pat_list = ['Lymphoma']
    mapping = {'LYMPH': pat_list}
    map_list.append(mapping)

    # Myeloma
    pat_list = ['Myeloma', 'Leukemia']
    mapping = {'LYMPH': pat_list}
    map_list.append(mapping)

    # OVARY OR FALLOPIAN TUBE
    pat_list = ['Ovary', '183.2', 'C57.00']
    mapping = {'OVARY OR FALLOPIAN TUBE': pat_list}
    map_list.append(mapping)

    # Pancreas
    pat_list = ['Pancreas']
    mapping = {'PANCREAS': pat_list}
    map_list.append(mapping)

    # PENIS
    pat_list = ['Penis']
    mapping = {'PENIS': pat_list}
    map_list.append(mapping)

    # Peripheral Nervous System
    pat_list = ['C47', '171']
    mapping = {'PERIPHERAL NERVOUS SYSTEM': pat_list}
    map_list.append(mapping)

    # PERITONEUM
    pat_list = ['Retroperitoneum', 'Peritoneum, Omentum and Mesentery']
    mapping = {'PERITONEUM': pat_list}
    map_list.append(mapping)

    # PLEURA
    pat_list = ['Pleura']
    mapping = {'PLEURA': pat_list}
    map_list.append(mapping)

    # PROSTATE
    pat_list = ['Prostate']
    mapping = {'PROSTATE': pat_list}
    map_list.append(mapping)

    # SKIN
    pat_list = ['Skin']
    mapping = {'SKIN': pat_list}
    map_list.append(mapping)

    # Soft Tissue
    pat_list = ['Soft Tissue including Heart']
    mapping = {'SOFT TISSUE': pat_list}
    map_list.append(mapping)

    # TESTIS
    pat_list = ['Testis']
    mapping = {'TESTIS': pat_list}
    map_list.append(mapping)

    # THYMUS
    pat_list = ['193', 'C73']
    mapping = {'THYMUS': pat_list}
    map_list.append(mapping)

    # THYROID
    pat_list = ['Thyroid']
    mapping = {'THYROID': pat_list}
    map_list.append(mapping)

    # UTERUS
    pat_list = ['Corpus Uteri', 'Uterus, NOS']
    mapping = {'UTERUS': pat_list}
    map_list.append(mapping)

    # VULVA OR VAGINA
    pat_list = ['Vulva', 'Vagina']
    mapping = {'VULVA OR VAGINA': pat_list}
    map_list.append(mapping)

    return map_list




def _mapping_icd_9_10_to_oncotree():
    # Creates list of dictionaries that will map ICD9/10 codes to an organ # TODO: (Legacy) This can be deleted

    # Initialize list for mapping from met sample biopsy site to organ
    map_list = []

    # Other
    pat_list = ['C26', 'C78.1', 'C78.89', 'C79.82', 'C79.89', 'C79.9', 'C80', 'C7A.00', 'C7B.8', 'D36.9',
                '197.1', '197.8', '198.89', '199', '229.9', '209.29', '209.79', 'C7B.00', 'D35.2', '237.4', '235.5',
                '239.0', '238.8', 'D49.0', 'C45.7', 'C45.9', 'D37.6', 'D37.8', 'D37.9', 'D40.8', 'D40.9', '198.82',
                'C7B.1']
    mapping = {'OTHER': pat_list}
    map_list.append(mapping)

    # Adrenal gland map
    pat_list = ['C79.7', 'C74', 'D35.0', 'D44.1', '194.0', '198.7', '227.0', '237.2']
    mapping = {'ADRENAL GLAND': pat_list}
    map_list.append(mapping)

    # Ampulla of vater
    pat_list = ['156.2', 'C24.1']
    mapping = {'AMPULLA OF VATER': pat_list}
    map_list.append(mapping)

    # BILIARY TRACT
    pat_list = ['C23', 'C22.1', 'C24.0', 'C24.8', 'C24.9', 'D13.5', '156', '230.8', 'D01.5']
    mapping = {'BILIARY TRACT': pat_list}
    map_list.append(mapping)

    # BLADDER OR URINARY TRACT
    pat_list = ['C79.1', 'C66', 'C67', 'D49.4', 'D41', 'D30', '188', '189.2', '189.3', '189.4', '189.8', '189.9',
                '233.3', '233.7', '233.9', '198.1', '239.4', '236.9']
    mapping = {'BLADDER OR URINARY TRACT': pat_list}
    map_list.append(mapping)

    # BLOOD
    pat_list = ['C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96.5', 'C96.6', 'D46', 'D47.1', 'D47.2', 'D47.3',
                'C7B.09', '203', '204', '205', '206', '207', '208', '238.71', '238.75']
    mapping = {'BLOOD': pat_list}
    map_list.append(mapping)

    # BONE
    pat_list = ['C40', 'C41', 'C79.5', 'C7B.03', 'D16', 'D48.0', 'D49.2', '170', '198.5',
                '213', '209.73', '238.0', '239.2']
    mapping = {'BONE': pat_list}
    map_list.append(mapping)

    # BOWEL
    pat_list = ['197.4', '197.5', '152', '153', '154', '230.3', '230.4', '230.5', '230.6', '230.7', '211.3',
                '211.4', '211.3', 'C18', 'C19', 'C20', 'C21', 'C49.A', 'C78.4', 'C78.5', 'D12', 'D13.3',
                'C78.80', 'D37.4', 'D37.5']
    mapping = {'BOWEL': pat_list}
    map_list.append(mapping)

    # Breast map
    pat_list = ['174.', '175.', '217', '198.81', '233.0', '238.3', '239.3', 'C44.501', 'C44.511', 'C44.521',
                'C44.591', 'C50', 'C79.81', 'D05.', 'D24.', 'D48.6', 'D49.3']
    mapping = {'BREAST': pat_list}
    map_list.append(mapping)

    # CNS/Brain map
    pat_list = ['C70', 'C71', 'C72', 'C79.3', 'C79.4', 'D33', 'D42', 'D43', 'D49.6', 'D49.7', '191', '192',
                '225', '237.5', '237.7', '237.9', '239.6', '239.7']
    mapping = {'CNS/BRAIN': pat_list}
    map_list.append(mapping)

    # Cervix map
    pat_list = ['180', 'C53', '233.1', 'D26.0', 'D06']
    mapping = {'CERVIX': pat_list}
    map_list.append(mapping)

    # Esophagus/Stomach map
    pat_list_esoph = ['C15', '150', '211.0', '230.1', 'D13.0', 'D00.1']
    pat_list_stomach = ['C16', '151', '211.1', '230.2', 'D13.1', 'D00.2', 'D37.1', 'D37.2']
    pat_list = pat_list_esoph + pat_list_stomach
    mapping = {'ESOPHAGUS OR STOMACH': pat_list}
    map_list.append(mapping)

    # Eye map
    pat_list = ['C69', 'D31', 'D03.1', 'D09.2', '190', '224', '234.0', '239.81']
    mapping = {'EYE': pat_list}
    map_list.append(mapping)

    # Head and Neck
    pat_list = ['197.3', '210', '230.0', '239.1', 'C00', 'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08',
                'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C30', 'C31',
                'C76.0', 'C78.30', 'C78.39', 'D10', 'D11', 'D37.0', 'D49.2']
    mapping = {'HEAD AND NECK': pat_list}
    map_list.append(mapping)

    # Kidney
    pat_list = ['C64', 'C79.0', 'D17.71', 'D30.0', 'D41.0', 'D49.51', '189.0', '189.1', '198.0',
                '209.24', '209.64', '223.0']
    mapping = {'KIDNEY': pat_list}
    map_list.append(mapping)

    # Liver
    pat_list = ['155', '197.7', '209.72', '211.5', '235.3', '230.8', 'C22', 'C78.7', 'C7B.02', 'D01.5', 'D13.4']
    mapping = {'LIVER': pat_list}
    map_list.append(mapping)

    # Lung
    pat_list = ['C34', 'C78.0', 'D02.2', 'D14.3', 'D38.1', '162', '197.0', '209.21', '209.61', '212.3', '235.7']
    mapping = {'LUNG': pat_list}
    map_list.append(mapping)

    # Lymph nodes
    pat_list = ['196', '200', '201', '202', '209.71', '229.0', 'C77', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C88',
                'C7B.01']
    mapping = {'LYMPH': pat_list}
    map_list.append(mapping)

    # OVARY OR FALLOPIAN TUBE
    pat_list = ['C79.6', '183']
    mapping = {'OVARY OR FALLOPIAN TUBE': pat_list}
    map_list.append(mapping)

    # Pancreas
    pat_list = ['157', 'C25', 'D13.6']
    mapping = {'PANCREAS': pat_list}
    map_list.append(mapping)

    # PENIS
    pat_list = ['187', 'C60']
    mapping = {'PENIS': pat_list}
    map_list.append(mapping)

    # Peripheral Nervous System
    pat_list = ['C47']
    mapping = {'PERIPHERAL NERVOUS SYSTEM': pat_list}
    map_list.append(mapping)

    # PERITONEUM
    pat_list = ['197.6', 'C78.6', 'C45.1']
    mapping = {'PERITONEUM': pat_list}
    map_list.append(mapping)

    # PLEURA
    pat_list = ['C78.2', '197.2', 'C45.0']
    mapping = {'PLEURA': pat_list}
    map_list.append(mapping)

    # PROSTATE
    pat_list = ['C61', '185', '222.2', 'D40.0']
    mapping = {'PROSTATE': pat_list}
    map_list.append(mapping)

    # SKIN
    pat_list = ['C79.2', '216', '232', 'D22', '238.2', 'C43', 'C44', 'C4A']
    mapping = {'SKIN': pat_list}
    map_list.append(mapping)

    # SOFT TISSUE
    pat_list = ['171', 'C49', '176']
    mapping = {'SOFT TISSUE': pat_list}
    map_list.append(mapping)

    # TESTIS
    pat_list = ['186', 'C62', 'D40.1']
    mapping = {'TESTIS': pat_list}
    map_list.append(mapping)

    # THYMUS
    pat_list = ['193', 'C37']
    mapping = {'THYMUS': pat_list}
    map_list.append(mapping)

    # THYROID
    pat_list = ['C73']
    mapping = {'THYROID': pat_list}
    map_list.append(mapping)

    # UTERUS
    pat_list = ['C54', 'D25', 'D26', '182', '218', '219']
    mapping = {'UTERUS': pat_list}
    map_list.append(mapping)

    # VULVA OR VAGINA
    pat_list = ['184']
    mapping = {'VULVA OR VAGINA': pat_list}
    map_list.append(mapping)

    return map_list
