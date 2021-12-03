import os
import numpy as np
import pandas as pd
from itertools import combinations



def make_table(path):
    # read file names(id)
    list_of_files = os.listdir(path) # len=560
    index_list = []
    for file_name in list_of_files:
        index_list.append(int(file_name.removesuffix('.txt')))

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
