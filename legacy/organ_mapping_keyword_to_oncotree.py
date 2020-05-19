
def _mapping_site_keyword_to_oncotree():
    # Creates list of dictionaries that will map keywords to the oncotree organ

    # Initialize list for mapping from met sample biopsy site to organ
    map_list = []

    # Other
    pat_list = ['MEDIASTINUM', 'MEDIASTINAL', 'UNSPECIFIED SITE', 'OTHER SPECIFIED SITES', 'UNKNOWN PRIMARY SITE']
    mapping = {'OTHER': pat_list}
    map_list.append(mapping)

    # Adrenal gland map
    pat_list = ['ADRENAL']
    mapping = {'ADRENAL GLAND': pat_list}
    map_list.append(mapping)

    # Ampulla of vater
    pat_list = ['AMPULLA']
    mapping = {'AMPULLA OF VATER': pat_list}
    map_list.append(mapping)

    # BLADDER OR URINARY TRACT
    pat_list = ['BLADDER', 'URINARY', 'URETHRA', 'URETER']
    mapping = {'BLADDER OR URINARY TRACT': pat_list}
    map_list.append(mapping)

    # BILIARY TRACT
    pat_list = ['BILE', 'BILIARY', 'GALLBADDER']
    mapping = {'BILIARY TRACT': pat_list}
    map_list.append(mapping)

    # BONE
    pat_list = ['BONE']
    mapping = {'BONE': pat_list}
    map_list.append(mapping)

    # BLOOD
    pat_list = ['BLOOD', 'POLYCYTHEMIA VERA', 'MASTOCYTOSIS', 'MYELO', 'LEUKEMIA']
    mapping = {'BLOOD': pat_list}
    map_list.append(mapping)

    # BOWEL
    pat_list = ['BOWEL', 'ANAL', 'COLON', 'RECTUM', 'APPENDIX', 'INTESTINE', 'ANUS', 'GASTROINTESTINAL TRACT',
                'INTESTINAL', 'CECUM', 'RECTOSIGMOID JUNCTION', 'SMALL BOWEL', 'SMALL INTESTINE', 'ILEUM',
                'DUODENUM', 'JEJUNUM']
    mapping = {'BOWEL': pat_list}
    map_list.append(mapping)

    # Head and Neck
    pat_list = ['HEAD', 'FACE', 'NECK', 'MOUTH', 'TONGUE', 'LARYNX', 'TONSIL', 'SALIVARY', 'NASOPHARYNX', 'NASAL',
                'SINUS', 'GLOTTIS', 'LIP ', 'LIP,', 'OROPHARYNX', 'SUBMANDIBULAR', 'NASOPHAR', 'MUCOSA', 'OROPHAR',
                'LACRIMAL GLAND', 'GUM,', 'PHARYNX', 'PAROTID', 'ORAL', 'TRACHEA']
    mapping = {'HEAD AND NECK': pat_list}
    map_list.append(mapping)

    # Breast map
    pat_list = ['BREAST']
    mapping = {'BREAST': pat_list}
    map_list.append(mapping)

    # CNS/Brain map
    pat_list = ['BRAIN', 'CEREBRAL', 'MENINGES', 'PITUITARY', 'FRONTAL LOBE', 'TEMPORAL LOBE', 'OCCIPITAL LOBE',
                'CEREBRUM', 'CEREBELLUM', 'CEREBRUM', 'PARIETAL LOBE', 'SPINAL CORD', 'EPENDYMOMA',
                'CRANIOPHARYNGIOMA', 'CRANIOPHARYNGEAL', 'CRANIAL', 'EPIDURAL', 'SPINE', 'PARASPINAL']
    mapping = {'CNS/BRAIN': pat_list}
    map_list.append(mapping)

    # Cervix map
    pat_list = ['CERVIX', 'CX UTERI']
    mapping = {'CERVIX': pat_list}
    map_list.append(mapping)

    # Esophagus/Stomach map
    pat_list_esoph = ['ESOPHAGUS', 'ILEUM', 'DUODENUM', 'JEJUNUM']
    pat_list_stomach = ['STOMACH']
    pat_list = pat_list_esoph + pat_list_stomach
    mapping = {'ESOPHAGUS OR STOMACH': pat_list}
    map_list.append(mapping)

    # Eye map
    pat_list = ['EYE', 'RETINA', 'CHOROID', 'CONJUNCTIVA', 'ORBIT', 'OPTIC']
    mapping = {'EYE': pat_list}
    map_list.append(mapping)

    # Kidney
    pat_list = ['KIDNEY', 'RENAL PELV', ' RENAL']
    mapping = {'KIDNEY': pat_list}
    map_list.append(mapping)

    # Liver
    pat_list = ['LIVER']
    mapping = {'LIVER': pat_list}
    map_list.append(mapping)

    # Lung
    pat_list = ['LUNG', 'BRONCHUS']
    mapping = {'LUNG': pat_list}
    map_list.append(mapping)

    # Lymph nodes
    pat_list = ['LYMPH NODE', 'LYMPH', 'LN ', 'SPLEEN']
    mapping = {'LYMPH': pat_list}
    map_list.append(mapping)

    # OVARY OR FALLOPIAN TUBE
    pat_list = ['OVARY', 'FALLOPIAN']
    mapping = {'OVARY OR FALLOPIAN TUBE': pat_list}
    map_list.append(mapping)

    # Pancreas
    pat_list = ['PANCREAS']
    mapping = {'PANCREAS': pat_list}
    map_list.append(mapping)

    # PENIS
    pat_list = ['PENIS', 'SCROTUM', 'URACHUS', 'PENILE']
    mapping = {'PENIS': pat_list}
    map_list.append(mapping)

    # Peripheral Nervous System
    pat_list = ['PRPH NERVE', 'PERIPHERAL NERVE']
    mapping = {'PERIPHERAL NERVOUS SYSTEM': pat_list}
    map_list.append(mapping)

    # PERITONEUM
    pat_list = ['PERITONEUM', 'PERITONEAL', 'PERITONEAL IMPLANT', 'PERITONEAL FLUID', 'PERITON', 'RETROPERITENIUM']
    mapping = {'PERITONEUM': pat_list}
    map_list.append(mapping)

    # PLEURA
    pat_list = ['PLEURA']
    mapping = {'PLEURA': pat_list}
    map_list.append(mapping)

    # PROSTATE
    pat_list = ['PROSTATE']
    mapping = {'PROSTATE': pat_list}
    map_list.append(mapping)

    # SKIN
    pat_list = ['SKIN', 'SCALP']
    mapping = {'SKIN': pat_list}
    map_list.append(mapping)

    # Soft Tissue
    pat_list = ['HEMANGIOMA', 'SOFT TIS', 'SFT TIS', 'LIPOMA', 'TRUNK', 'CONN,', 'PARAGANGLIOMA', 'SACRAL MASS']
    mapping = {'SOFT TISSUE': pat_list}
    map_list.append(mapping)

    # TESTIS
    pat_list = ['TESTIS']
    mapping = {'TESTIS': pat_list}
    map_list.append(mapping)

    # THYMUS
    pat_list = ['THYMUS']
    mapping = {'THYMUS': pat_list}
    map_list.append(mapping)

    # THYROID
    pat_list = ['THYROID']
    mapping = {'THYROID': pat_list}
    map_list.append(mapping)

    # UTERUS
    pat_list = ['UTERUS', 'CORPUS UTERI', 'MYOMETRIUM', 'FUNDUS UTERI', 'UTERINE', 'ENDOMETRIUM']
    mapping = {'UTERUS': pat_list}
    map_list.append(mapping)

    # VULVA OR VAGINA
    pat_list = ['VULVA', 'VAGINA']
    mapping = {'VULVA OR VAGINA': pat_list}
    map_list.append(mapping)

    # SKIN
    pat_list = ['SKIN', 'EYELID', 'MERKEL']
    mapping = {'SKIN': pat_list}
    map_list.append(mapping)

    return map_list