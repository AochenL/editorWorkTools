#This file aims to split Chinese phrases.
#For example, "你好，我是奥晨!" will be split to "你好\n 我是奥晨\n"
file_data = open('source_data.txt', 'r')
file_split = open('split_data.txt', 'w')
line = file_data.readline()
while line:
    line = file_data.readline()
    phrase = ''
    for ch in line:
        if ch == ' ' or ch ==',' or ch =='。' or ch =='，' or ch =='!':
            if phrase != '':               
                file_split.write(phrase+'\n')               
            phrase = ''
        else:
            phrase += ch
    if phrase != '':
       file_split.write(phrase)

file_split.close()
file_data.close()
