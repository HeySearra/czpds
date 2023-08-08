import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import pandas as pd
import json

from dict import merge_dict1

data_0 = pd.read_csv('./data/PDS_CZ_0_.csv')
data_1 = pd.read_csv('./data/PDS_CZ_1_.csv')

# item_map = {}  # 防止重复双主键 (PatientID & Time)
patients_data_list = []
tot = 0
from tqdm import tqdm

for _, i in tqdm(data_1.iterrows(), total=data_1.shape[0]):
    # if tot > 10: break
    if i['sectionID'] not in merge_dict1.keys():
        continue
    for _, j in data_0.iterrows():
        # if tot > 10: break
        patient_item = {}
        if i['userId'] == j['userId']:
            # and str(i['userId']) not in item_map
            # item_map[str(i['userId'])] = 1
            # print(tot)
            tot += 1

            # date = i['labdt']
            # converted_date = datetime.strptime(date, '%m/%d/%Y')
            # patient_item['date'] = str(converted_date)

            patient_item['userId'] = i['userId']
            patient_item['department'] = i['department']
            patient_item['formID'] = i['formID']
            patient_item['sectionID'] = i['sectionID']
            patient_item['itemId'] = i['itemId']
            patient_item['itemValue'] = i['itemValue']
            patient_item['actualExamineDate'] = i['actualExamineDate']
            patient_item['userName'] = j['userName']
            patient_item['gender'] = j['gender']
            patient_item['birthday'] = j['birthday']
            patient_item['diyCode'] = j['diyCode']
            patient_item['userTag'] = j['userTag']
            patients_data_list.append(patient_item)
            break  # 找到了对应项，便退出该层循环

# Step 2: 处理Patients表，将Patients表中的特有指标加进前面的patient_item中

# 2.1) 为了检索方便，先将Paitents表中的所需指标信息存在dict里

# patient_info_map = {}
# for i in patients_data_list:
#     patient_info_map[i['userId']] = [
#         i['gender'], i['age'], i['cause_ESRD'], i['mDiabDiag'], i['All_Died_7']]
#     # gender 0, age 1, cause_ESRD 2, mDiabDiag 3, all_died_7 4
#
# # 2.2) 合并操作
# for i in patients_data_list:
#     q = patient_info_map[i['patient_id']]
#     if q is not None:
#         i['gender'] = 1 if q[0] == 'Male' else 0
#         i['age'] = q[1]
#         i['origin_disease'] = q[2]
#         i['diabetes'] = 1 if q[3] == 'Yes' else 0
#         i['death'] = q[4]
#     else:  # 如果不在Patient表中，该条数据删除
#         patients_data_list.remove(i)

# space_count = 0
# for i in patients_data_list[:]:
#     if np.sum(1 - np.isnan(np.array([i['co2'] ,i['wbc'], i['ca'], i['k'], i['na'], i['cre'], i['p'], i['alb'], i['glu']
#                                      , i['pre_weight'], i['pst_weight'], i['pre_sys'], i['pst_sys'], i['pre_dia'], i['pst_dia'], i['pre_urea']
#                                      , i['pst_urea'], i['bmi']]))) == 0:
#
#         print(i['patient_id'])
#         patients_data_list.remove(i)
#         space_count += 1
# print("space: ", space_count)
print(tot) # 14314
df_excel = pd.read_json(json.dumps(patients_data_list, ensure_ascii=False))
df_excel.to_excel('./data/pre/2_merge_1.xlsx', index=False)
