#此程序旨在去除每个段落的前几个字符，具体去除几个可由用户输入
#This program aims to remove the first few characters from each paragraph
#The number of characters removed can be input by the user


#For example, if the user enetered 8:
#1. (  ) Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#2. (  ) Eu scelerisque felis imperdiet proin fermentum leo vel orci porta. 
#3. (  ) Sed adipiscing diam donec adipiscing tristique risus nec feugiat.
# will be output as
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#Eu scelerisque felis imperdiet proin fermentum leo vel orci porta. 
#Sed adipiscing diam donec adipiscing tristique risus nec feugiat.


#使用此程序前，需要将py程序和文章放在同一个路径下，并将文章命名为"passage.txt"
#标好的文件会被命名为'passage_removed.txt'

#This program requires the passage file under the same directory with the py file
#The passage file should be named "passage.txt".
#The numbered version is named 'passage_removed.txt'



inputFile = open('passage.txt', 'r')
outputFile = open('passage_removed.txt', 'w')
print("How many letters do you want to remove?")
ch_length = int(input("Please input a number.\n"))

line = 'abc'
while line:
    line = inputFile.readline()
    newLine = ''
    i = 0
    for ch in line:
        i +=1
        if i>ch_length:
            newLine += ch
    if newLine != '':
       outputFile.write(newLine)
inputFile.close()
outputFile.close()
