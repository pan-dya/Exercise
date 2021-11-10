file = open("note.txt", "r")
new_file = open("note1.txt", "x")
myFile = file.read().replace('\n','')
counter = 0
file.close()
# print(myFile)

for i in myFile:
    counter += 1
    new_file.write(str(counter) + '. ' + str(myFile[counter-1]) + '\n')