



def _mapping_impact_met_site_to_oncotree():
    # Initialize list for mapping from met sample biopsy site to organ (Mapping by Francisco)
    map_list = []

    # Adrenal gland map
    keyword_list = ['ADRENAL GLAND', 'ADRENAL']
    mapping = {'ADRENAL GLAND': keyword_list}
    map_list.append(mapping)

    # Brain map
    keyword_list = ['BRAIN', 'BRAIN - DURA', 'RIGHT FRONTAL BRAIN', 'CEREBELLUM', 'BRAIN', 'LEFT OCCIPITAL']
    # mapping = {'BRAIN': keyword_list}
    mapping = {'CNS/BRAIN': keyword_list}

    map_list.append(mapping)

    # Bone map
    keyword_list = ['BONE', 'SKULL', 'SKULL BASE', 'VERTEBRATE', 'RIB', 'LEFT 2ND RIB', 'PUBIC BONE',
                    'SPINE BONE', 'SPINE', 'HIP', 'ILIAC BONE', 'ILIAC', 'FEMUR', 'TIBIA', 'HUMERUS',
                    'BONE FEMUR', 'SACRUM', 'SACRAL MASS', 'RIGHT ILIAC BONE', 'SCAPULA', 'STERNUM',
                    'LUMBAR SPINE', 'MANUBRIUM', 'PELVIS', 'CLIVUS']
    mapping = {'BONE': keyword_list}
    map_list.append(mapping)

    # Breast map
    keyword_list = ['BREAST', 'CONTRALATERAL BREAST', 'IPSILATERAL BREAST']
    mapping = {'BREAST': keyword_list}
    map_list.append(mapping)

    # Heart map
    keyword_list = ['HEART', 'PERICARDIUM', 'PERCARDIUM', 'PERICARDIAL FLUID', 'HEART - RIGHT VENTRICLE']
    mapping = {'HEART': keyword_list}
    map_list.append(mapping)

    # Bowel map
    keyword_list = ['SMALL BOWEL', 'SMALL INTESTINE', 'ILEUM', 'DUODENUM', 'JEJUNUM', 'PERIRECTAL']
    mapping = {'BOWEL': keyword_list}
    map_list.append(mapping)

    # Epidural map
    keyword_list = ['EPIDURAL', 'EPIDURAL MASS']
    # mapping = {'EPIDURAL': keyword_list}
    mapping = {'CNS/BRAIN': keyword_list}
    map_list.append(mapping)

    # Colon map
    keyword_list = ['SIGMOID COLON', 'TRANSVERSE COLON', 'RECTOSIGMOID COLON', 'CECUM', 'ASCENDING COLON',
                    'COLONIC SEROSA', 'CUL-DE-SAC']
    # mapping = {'COLON': keyword_list}
    mapping = {'BOWEL': keyword_list}
    map_list.append(mapping)

    # Lymph map
    keyword_list = ['RETROPERITONEAL LND', 'LYMPH', 'AXILLARY LYPMH NODES']
    mapping = {'LYMPH': keyword_list}
    map_list.append(mapping)

    # Pleura map
    keyword_list = ['PLEURAL FLUID', 'LEFT PARIETAL PLEURA', 'RIGHT LUNG PLEURA']
    mapping = {'PLEURA': keyword_list}
    map_list.append(mapping)

    # Stomach map
    keyword_list = ['STOMACH', 'GASTRIC']
    # mapping = {'STOMACH': keyword_list}
    mapping = {'ESOPHAGUS OR STOMACH': keyword_list}
    map_list.append(mapping)

    # PERITONEUM map
    keyword_list = ['PERITONEUM', 'PERITONUEM', 'OMENTUM', 'MESENTERY']
    mapping = {'PERITONEUM': keyword_list}
    map_list.append(mapping)

    # BLADDER map
    keyword_list = ['BLADDER', 'BLADDER NECK']
    mapping = {'BLADDER': keyword_list}
    map_list.append(mapping)

    # BILIARY TRACT
    pat_list = ['BILE', 'BILIARY', 'GALLBADDER']
    mapping = {'BILIARY TRACT': pat_list}
    map_list.append(mapping)

    # SOFT TISSUE map
    keyword_list = ['SOFT TISSUE', 'CHEST WALL SOFT TISSUE', 'SOFT TISSUE BACK', 'SOFT TISSUE NECK',
                    'SOFT TISSUE, POSTERIOR LEFT SHOULDER', 'AXILLA', 'ABDOMEN', 'DIAPHRAGM', 'DIAPHRAM', 'MUSCLE',
                    'SUBCUTANEOUS TISSUE', 'GROIN', 'THIGH', 'AXILA', 'UMBILICAL CORD', 'ARM', 'EXTREMITY',
                    'LIGAMENT', 'FLANK', 'LEG', 'FOREARM', 'BACK', 'BUTTOCK', 'UMBILICUS']
    mapping = {'SOFT TISSUE': keyword_list}
    map_list.append(mapping)

    # PELVIS map
    keyword_list = ['PELVIS', 'PELVIS MASS', 'PELVIC NODULE', 'PELVIC WALL', 'RENAL PELVIS', 'RIGHT ISCHIUM',
                    'ISCHIUM']
    # mapping = {'PELVIS': keyword_list}
    mapping = {'BONE': keyword_list}
    map_list.append(mapping)

    # PANCREAS map
    keyword_list = ['PANCREAS', 'PANCREATIC HEAD']
    mapping = {'PANCREAS': keyword_list}
    map_list.append(mapping)

    # ABDOMEN map
    keyword_list = ['ABDOMEN', 'ABDOMINAL MASS', 'ABODOMINAL WALL']
    # mapping = {'ABDOMEN': keyword_list}
    mapping = {'SOFT TISSUE': keyword_list}
    map_list.append(mapping)

    # UTERUS map
    keyword_list = ['UTERUS', 'CERVIX', 'UTERINE SEROSA', 'UTERUS/CERVIX', 'ADNEXA OR ENDOMTERIUM']
    mapping = {'UTERUS': keyword_list}
    map_list.append(mapping)

    # UNKNOWN
    keyword_list = ['UNKNOWN', 'NOT AVAILABLE', 'NA']
    mapping = {'UNKNOWN': keyword_list}
    map_list.append(mapping)

    return map_list
