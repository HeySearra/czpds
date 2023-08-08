import math

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import pandas as pd
import json
from tqdm import tqdm
from dict import choose_item_dict
import re

data = pd.read_excel('./data/pre/2_merge_3.xlsx')

item_map = {}
patients_data_list = []
patients_temp = {}
key_list = []
tot = 0
tot1 = 0
tot2 = 0
for _, i in tqdm(data.iterrows(), total=data.shape[0]):
    if type(i['腹透充分性_性别']) == float and math.isnan(i['腹透充分性_性别']):
        tot1 += 1
        continue
    if type(i['gender']) == float and math.isnan(i['gender']):
        tot2 += 1
        continue
    if not (i['腹透充分性_性别'] == 1 and i['gender'] == '男' or i['腹透充分性_性别'] == 2 and i['gender'] == '女'):
        tot += 1

print(tot, tot1, tot2) # 0 4 0

for idx, i in tqdm(data.iterrows(), total=data.shape[0]):
    if type(i['腹透充分性_性别']) == float and math.isnan(i['腹透充分性_性别']):
        data.loc[idx, '腹透充分性_性别'] = 1 if data.loc[idx, 'gender'] == '男' else 2
        continue
    if type(i['gender']) == float and math.isnan(i['gender']):
        continue
    # if not (i['性别'] == 1 and i['gender'] == '男' or i['性别'] == 2 and i['gender'] == '女'):
    #     data.loc[idx, 'gender'] = data.loc[idx, '性别']

data.to_excel('./data/pre/2_merge_4.xlsx')

