import os
import numpy as np
import pandas as pd
from itertools import permutations


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


def make_table(path):
    # read file names(id)
    list_of_files = os.listdir(path) # len=560
    index_list = []
    for file_name in list_of_files:
        # index_list.append(int(file_name.removesuffix('.txt')))  # for python 3.9+
        index_list.append(int(remove_suffix(file_name, '.txt')))

    # read file content
    titles = []
    texts = []
    notices = []
    for file in list_of_files:
        f = open("{}/{}".format(path, file), "r")
        temp = f.readlines()
        titles.append(temp[0])
        texts.append(temp[1])
        try:
            notices.append(temp[2])
        except:
            notices.append('')
        f.close()

    # make general table
    df_dirty = pd.DataFrame(
        {'ID': index_list,
         'title': titles,
         'text': texts,
         'notice': notices
        })
    return df_dirty



def make_data(dataType, table):
    import itertools
    
    # make text_pairs, data scope can be changed, I only include "title" here
    # number of text_pairs = Pn取2, train:n=560; test:n=421

    combs = permutations(table[['ID', 'title']].values, r=2)
    combs = pd.DataFrame([[s for s in comb] for comb in combs], columns=['text_a', 'text_b'])
    # combs[['id_text_b', 'text_b']] = combs['text_b'].to_list()
    temp_l = pd.DataFrame(combs['text_a'].to_list(), columns = ['id_text_a', 'text_a'])
    temp_r = pd.DataFrame(combs['text_b'].to_list(), columns = ['id_text_b', 'text_b'])
    combs = pd.concat([temp_l, temp_r], axis=1)
    

    if dataType=='train':
        # make label set
        labels = pd.read_csv('TrainLabel.csv')
        pairs = set()
        for _, row in labels.iterrows():
            temp = frozenset([row['Test'], row['Reference']])
            if temp not in pairs:
                pairs.add(temp)

        # mark label on text_pairs
        combs['label'] = 'unlike'
        for ind, row in combs.iterrows():
            if {row['id_text_a'], row['id_text_b']} in pairs:
                combs.at[ind, 'label'] = 'like'

    
    # combs.to_csv("{}.tsv".format(dataType), sep="\t", index=False)            
    return combs

