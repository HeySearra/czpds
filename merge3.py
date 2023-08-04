import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import pandas as pd
import json
from tqdm import tqdm
from dict import choose_item_dict
import re

data = pd.read_excel('./data/pre/merge_2.xlsx')

item_map = {}
patients_data_list = []
patients_temp = {}
key_list = []

for key in choose_item_dict.keys():
    for i in range(data.shape[0]):
        if re.match(r';\d+;', str(data.loc[i, key])):
            data.loc[i, key] = int(data.loc[i, key][1: -1])

data.to_excel('./data/pre/merge_3.xlsx')