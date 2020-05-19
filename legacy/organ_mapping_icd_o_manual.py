


def _mapping_seer_icd_o_code_to_oncotree():
    # Creates list of dictionaries that will map keywords to the oncotree organ
    # Derived from https://seer.cancer.gov/siterecode/icdo3_dwhoheme/index.html
    # Initialize list for mapping from met sample biopsy site to organ
    map_list = []

    # Other
    pat_list = ['Trachea, Mediastinum and Other Respiratory Organs', 'Other Digestive Organs',
                'Other Male Genital Organs', 'Other Endocrine including Thymus',
                'Other Female Genital Organs',
                'Mesothelioma', 'Kaposi Sarcoma', 'Miscellaneous']
    mapping = {'OTHER': pat_list}
    map_list.append(mapping)

    # Adrenal gland map
    pat_list = ['C740', 'C741', 'C749']
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
    pat_list = ['Small Intestine', 'Colon and Rectum']
    mapping = {'BOWEL': pat_list}
    map_list.append(mapping)

    # Head and Neck
    pat_list = ['Oral Cavity and Pharynx', 'Larynx', 'Nose, Nasal Cavity and Middle Ear']
    mapping = {'HEAD AND NECK': pat_list}
    map_list.append(mapping)

    # Breast map
    pat_list = ['Breast', 'C502', 'C508', 'C509']
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
    pat_list = ['Ovary', 'C570']
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
    pat_list = ['C728', 'C729']
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
    pat_list = ['Skin excluding Basal and Squamous']
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
    pat_list = ['C379']
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