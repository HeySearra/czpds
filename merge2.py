import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import pandas as pd
import json
from tqdm import tqdm
from dict import merge_dict2, merge_dict1

data = pd.read_excel('./data/pre/2_merge_1.xlsx')
data_83 = pd.read_excel('./data/pre/2_merge_83.xlsx')

item_map = {}  # 防止重复双主键 (PatientID & Time)
patients_data_list = []
patients_temp = {}
key_list = []
for _, i in tqdm(data.iterrows(), total=data.shape[0]):
    patient_item = {}
    if str(i['userId']) + i['actualExamineDate'] not in item_map:
        item_map[str(i['userId']) + i['actualExamineDate']] = 1
    else:
        patient_item = patients_temp[str(i['userId']) + i['actualExamineDate']]
    key = merge_dict1[i['sectionID']]+ '_' + merge_dict2[i['sectionID']][i['itemId']]
    if key not in key_list:
        key_list.append(key)
    patient_item['userId'] = i['userId'] if 'userId' not in patient_item.keys() else patient_item['userId']
    patient_item['department'] = i['department'] if 'department' not in patient_item.keys() else patient_item['department']
    patient_item['formID'] = i['formID'] if 'formID' not in patient_item.keys() else patient_item['formID']
    patient_item[key] = i['itemValue'] if key not in patient_item.keys() else patient_item[key]
    patient_item['actualExamineDate'] = i['actualExamineDate'] if 'actualExamineDate' not in patient_item.keys() else patient_item['actualExamineDate']
    patient_item['userName'] = i['userName'] if 'userName' not in patient_item.keys() else patient_item['userName']
    patient_item['gender'] = i['gender'] if 'gender' not in patient_item.keys() else patient_item['gender']
    patient_item['birthday'] = i['birthday'] if 'birthday' not in patient_item.keys() else patient_item['birthday']
    patient_item['diyCode'] = i['diyCode'] if 'diyCode' not in patient_item.keys() else patient_item['diyCode']
    patient_item['userTag'] = i['userTag'] if 'userTag' not in patient_item.keys() else patient_item['userTag']
    # for _, j in data_83.iterrows():
    #     if patient_item['userId'] == j['userId'] and patient_item['首次日期'] == j['itemValue']:

    patients_temp[str(i['userId']) + i['actualExamineDate']] = patient_item


df_excel = pd.read_json(json.dumps(list(patients_temp.values()), ensure_ascii=False))
df_excel.to_excel('./data/pre/2_merge_2.xlsx', index=False)