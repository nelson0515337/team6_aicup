import os
import pandas as pd
from itertools import combinations


# read file name(id)
list_of_files = os.listdir("./dataTrainComplete") # len=560
index_list = []
for file_name in list_of_files:
    index_list.append(int(file_name.removesuffix('.txt')))


# read file content
titles = []
texts = []
notices = []
for file in list_of_files:
    f = open("./dataTrainComplete/{}".format(file), "r")
    temp = f.readlines()
    titles.append(temp[0])
    texts.append(temp[1])
    notices.append(temp[2])
    f.close()
    
        
# make general table
df_dirty = pd.DataFrame(
    {'ID': index_list,
     'title': titles,
     'text': texts,
     'notice': notices
    })


# make text_pair_table, data scope can be changed, I only include "text" here
# number of data pair = C560取2
combs = combinations(df_dirty[['ID', 'text']].values, r=2)
combs = pd.DataFrame([[s for s in comb] for comb in combs], columns=['left', 'right'])
combs[['id_left', 'left']] = combs['left'].to_list()
combs[['id_right', 'right']] = combs['right'].to_list()


# make relativeness set
labels = pd.read_csv('TrainLabel.csv')
pairs = set()
for _, row in labels.iterrows():
    temp = frozenset([row['Test'], row['Reference']])
    if temp not in pairs:
        pairs.add(temp)
        
        
# mark relativeness label on text_pair_table
combs['label'] = 0
for ind, row in combs.iterrows():
    if {row['id_left'], row['id_right']} in pairs:
        combs.at[ind, 'label'] = 1