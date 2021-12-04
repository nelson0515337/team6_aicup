'''
Create userdict for Jieba without specify the frequency
Input: the 3 excel files contains keywords\02chem
Output: A text file "userdict.txt" contains all keyword

'''


import pandas as pd

df1 = pd.read_excel(r"./Keywords/02chem.list.xlsx", header = None)
df2 = pd.read_excel(r"./Keywords/02crop.list.xlsx", header = None)
df3 = pd.read_excel(r"./Keywords/02pest.list.xlsx", header = None)

n=0
with open('./jieba/userdict.txt', 'w', encoding="utf-8") as f:
    for word in df1.to_numpy().flatten():
        if(isinstance(word, str)):
            f.write(word+'\n')
            n = n + 1
            print(word)
            #print(n)
    for word in df2.to_numpy().flatten():
        if(isinstance(word, str)):
            f.write(word+'\n')
            n = n + 1
            print(word)
            #print(n)
    for word in df3.to_numpy().flatten():
        if(isinstance(word, str)):
            f.write(word+'\n')
            n = n + 1
            print(word)
            #print(n)
