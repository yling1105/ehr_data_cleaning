"""
This module including functions that preprocessing the 4 datasets:
- patients
- drugs
- dx
- lab
"""

import pandas as pd
from tqdm import tqdm

def drug_to_indi(name_list):
    """
    Input: a list of drugs' names
    ----
    Return: a indicator vector
    """
    res = [0] * len(patients)
    index = 0 # Used to indicate which patient
    key = drugs.loc[0, 'patient_sk']
    for i in tqdm(range(len(drugs))):
        if drugs.loc[i, 'patient_sk'] == key:
            if res[index] == 1:
                continue
            else:
                if drugs.loc[i, 'generic_name'] in name_list:
                    res[index] = 1
        else:
            index += 1
            key = patients.loc[index, 'patient_sk']
            if drugs.loc[i, 'generic_name'] in name_list:
                res[index] = 1
            else:
                continue
    return res

def dx_to_indi(name_list):
    """
    Input: List: list of phe_code codes
    ----
    return: List: a indicator vector
    """
    res = [0] * len(patients)
    index = 0 # Used to indicate which patient
    key = patients.loc[0, 'patient_sk']
    for i in tqdm(range(len(dx))):
        if dx.loc[i, 'patient_sk'] == key:
            if res[index] == 1:
                continue
            else:
                if dx.loc[i, 'phecode'] in name_list:
                    res[index] = 1
        else:
            index += 1
            key = patients.loc[index, 'patient_sk']
            if dx.loc[i, 'phecode'] in name_list:
                res[index] = 1
            else:
                continue
    return res   