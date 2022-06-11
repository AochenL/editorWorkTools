#此程序旨在为段落自动以画圈数字标号（"①","②","③"），最多可以标记30段
#This program aims to number paragraphs with circled numbers（"①","②","③"）
#Maximum paragraph: 30

#For example:
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#Eu scelerisque felis imperdiet proin fermentum leo vel orci porta. 
#Sed adipiscing diam donec adipiscing tristique risus nec feugiat.
#will be numbered as
#① Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#② Eu scelerisque felis imperdiet proin fermentum leo vel orci porta. 
#③ Sed adipiscing diam donec adipiscing tristique risus nec feugiat.


#使用此程序前，需要将py程序和文章放在同一个路径下，并将文章命名为"passage.txt"
#标好的文件会被命名为'passage_numbered.txt'

#This program requires the passage file under the same directory with the py file
#The passage file should be named "passage.txt".
#The numbered version is named 'passage_numbered.txt'



circledNumArray = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪","⑫","⑬","⑭"
"⑮","⑯","⑰","⑱","⑲","⑳","㉑","㉒","㉓","㉔","㉕","㉖","㉗","㉘","㉙","㉚"]
i = 0
outputFile = open('passage_numbered.txt','w')

with open('passage.txt','r') as inputFile:
    line = inputFile.readline()
    while line:
        if line != "\n":
            outputFile.write(circledNumArray[i]+" "+line)
            i += 1
        line = inputFile.readline()
    
inputFile.close()
outputFile.close()
