# Organ Site Mapping for Metastatic Cancer
Note: When using this resource, please credit Renzo DiNatale, M.D. and Christopher Fong, Ph.D. (MSKCC) 

##### Purpose
Cancer is a disease that can involve metastatic spread from it primary site (Ex. Lung) to another organ (Ex. Liver).
However, the naming conventions used for this organs can slightly vary, or may be specified with more granularity than commonly appropriate. 
This is evident in free text entries, where the variability is large.  

This repository contains functions that, for a given input file containing a list of organ sites, will annotate the table with a standardized organ site map. 
The annotator will leverage various organ site names to a standard ontology.


## Standard Ontologies
##### Overview
From cBioPortal, a user can download a study summary of a cohort (Example at `/demo_data/msk_impact_2017_clinical_data.tsv`), and find the `Primary Tumor Site` and `Metastatic Site` columns, specifying the specific locations of the primary cancer and, if applicable, the metastatic sequenced sample. 
Here, a custom mapping to a standard set of organ sites have been created containing 82 different locations.

Annotations between primary and metastatic sites include:
- Distant or local extention of cancer spread
- Local or distant lymph node metastasis
- Organ type according to hematogenous spread (Liver, lung, portal, non-portal)   

##### Mapping granularity
Granularity may vary from project to project, and to accommodate, two additional organ mapping profiles have been created to
- Reduce the number of metastatic sites for the purpose of aggregating cases to increase the N in bins
- Have the metastatic sites reflect that of how ICD billings codes for how secondary malignant neoplasms are represented
Therefore, three mappings are included in this annotation package: 
1. A manually curated version, where, for each site in a 
2. A mapping of tissue types according to [oncotree](http://oncotree.mskcc.org/#/home) tissue types
3. A mapping of metastatic sites based on [ICD billings codes](https://icdlist.com/) on secondary malignant neoplasms     

##### More information
See the readme in `/mappings` for comprehensive details on the mapping

## Organ Site Data Inputs
There are two input systems can be utilized for this repository:
- Free text as provided in cBioPortal summary tables
- ICD billing codes related to secondary malignant neoplasms or metastatic cancer

## Repository Setup
This repository is built for Python 3.6+. 

Library dependencies:
- Pandas

## Annotations 
An annotated version of the input dataset. Additional columns:

|Annotation Column                |Description            |
|---------------------------------|---------------------|
|PRIMARY_SITE_RDN_MAP      | Standardized Primary Cancer Site|
|PRIMARY_SITE_RDN_MAP_MAIN | Main category name from PRIMARY_SITE_RDN_MAP |  	
|PRIMARY_SITE_RDN_MAP_SECONDARY | Secondary category name from PRIMARY_SITE_RDN_MAP |	
|METASTATIC_SITE_RDN_MAP	| Standardized Metastatic Cancer Site |
|METASTATIC_SITE_RDN_MAP_MAIN |	Main category name from METASTATIC_SITE_RDN_MAP |
|METASTATIC_SITE_RDN_MAP_SECONDARY  | Secondary category name from METASTATIC_SITE_RDN_MAP |	
|LYMPH_SPREAD	| Annotation if metastatic site is a lymph node, and if it is a regional or distant spread |
|LOCAL_EXTENSION |	Annotation if metastatic site is a local extension to the the primary site |
|hematogenous_grouping  | Annotation label for hematogenous metastatic dissemination.  Can be either Portal, Non-Portal, Lung, or Liver |	
|METASTATIC_SITE_ONCOTREE_RDN  |	Metastatic site annotations from METASTATIC_SITE_RDN_MAP, aggregated to fit oncotree tissue types |
|METASTATIC_SITE_BILLING_RDN  | Metastatic site annotations from METASTATIC_SITE_RDN_MAP, aggregated to fit ICD Billing codes (Secondary malignant neoplasms) | 

## Jupyter Notebook Examples
#### met_site_data_creation_impact.ipynb
##### Input 
Organ sites using the MSK-IMPACT cohort (Nat. Med. 2017) via [cBioPortal](https://www.cbioportal.org/study/summary?id=msk_impact_2017) 

Data from this cohort is located at `/demo/msk_impact_2017_clinical_data.tsv`




## Relevant Functions



   
 


