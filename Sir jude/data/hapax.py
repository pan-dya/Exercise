import os, string

file = str(input("Enter your file name: "))
myBuku = open(os.getcwd()+'\\'+file, 'r')
myFile = myBuku.read().lower()
myBuku2 = myFile.translate(str.maketrans('', '', string.punctuation))

def wordCounts(data):
    # count = dict()
    # word = data.split()
    # for i in word:
    #     if i in count:
    #         count[word] += 1
    #     else:
    #         count[word] = 1
    # return count
   
    counts = dict()
    words = data.split()
    for words in words:
        if words in counts:
            counts[words] += 1
        else:
            counts[words] = 1

    hapaxes = []
    for key,value in counts.items():
        if value == 1:
            hapaxes.append(key)

    return hapaxes

hapax = wordCounts(myBuku2) 

print('The hapaxes are', hapax)