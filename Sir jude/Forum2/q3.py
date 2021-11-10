import string

myFile = open("note.txt","r")
myfile = myFile.read()
file = myfile.translate(str.maketrans('','', string.punctuation))
a = file.split()
wordCount = 0
wordLength = 0
for line in file:
    words = a
    wordCount += len(words)     #count the number of words in the document
    for word in words:
        wordLength += len(word) #count the length of every word in the document

average = wordLength/float(wordCount)
print(average)
myFile.close()