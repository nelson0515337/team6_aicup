
import os

def buildSimilarWordDict():
    #get dir of keyword
    root = 'Keywords/'
    dirs = ['02pest.list.csv', '02chem.list.csv', '02crop.list.csv']
    wordDict = {}
    for dir in dirs:
        print(dir)
    
        with open(root+dir, encoding = 'utf-8') as f:
            rows = f.readlines()
            for row in rows:
                split_row = [x.strip() for x in row.split(',')]
                res = []
                for word in split_row :
                    if word != '':
                        res.append(word)
                    else:
                        break
                for i in range(1, len(res)):
                    wordDict[res[i]] = res[0]
    
    return wordDict



def repalceSimilarWords():
    global wd
    root = 'dataTrainComplete/'
    dirs = os.listdir(root)

    for dir in dirs:
        text_file = open(root+dir, 'r')
        data = text_file.read()
        text_file.close()

        for k,v in wd.items():
            data = data.replace(k,v)
        
        f = open(root+dir, 'w')
        f.write(data)
        f.close()

wd = buildSimilarWordDict()
repalceSimilarWords()




