import pandas as pd
import os
import re
import sys

# turn csv into txt format dataset

def read(path, filetype='csv'):
    if path == '':
        path = 'annotations.csv'
    if filetype == 'text':
        with open(path, encoding='utf-8') as q:
            return q.read()
    elif filetype == 'csv':
        return pd.read_csv(path)

def tagTranslate(tag):
    if tag == 'rbc':
        return 1
    elif tag == 'wbc':
        return 0

def positionCalculation(xmin, xmax, ymin, ymax, tag):
    return tagTranslate(tag), (xmin+xmax)/2, (ymin+ymax)/2, xmax-xmin, ymax-ymin

def dataReshape(df, format='df'):
    data_reshape = {}
    if format == 'df':
        for i in range(len(df)):
            # print(df.loc[i, 'image'])
            if df.loc[i, 'image'] not in data_reshape:
                data_reshape[df.loc[i, 'image']] = []
            data_reshape[df.loc[i, 'image']].append(positionCalculation(
                df.loc[i, 'xmin'], df.loc[i, 'xmax'], df.loc[i, 'ymin'], df.loc[i, 'ymax'], df.loc[i, 'label']
            ))
        #  print(data_reshape)
        return data_reshape

def fileRename(original_name):
    # 使用 regular expression 进行文件名重命名（png->txt）
    name = re.sub(r'.png$', '.txt', original_name)
    return 'labels/' + name

def generateTxt(name, content):
    name = fileRename(name)
    text = ''
    lines = 0
    for i in content:
        if lines == 0:
            text = str(i[0]) + ' '+ str(i[1]) + ' '+ str(i[2]) + ' '+ str(i[3])+' '+ str(i[4])
        else:
            text = str(text) + '\n' + str(i[0]) + ' '+ str(i[1]) + ' '+ str(i[2]) + ' '+ str(i[3])+' '+ str(i[4])
        lines += 1
    print('text is ', text)
    if not os.path.exists('labels'):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.mkdir('labels')
    with open(name, "w") as file:
        file.write(text)
    return text



rawdata = read(input('Input .csv file path (by default:annotations.csv):'))
print(rawdata)
reshapedDict = dataReshape(rawdata)
for i in reshapedDict:
    generateTxt(i, reshapedDict[i])