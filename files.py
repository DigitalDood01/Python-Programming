#THIS PROGRAM IS ABOUT FILES

#Reading a file
fileref = open("learn_file.txt", "r")
for l in fileref:
    print(l.strip())
fileref.close()

#Writing a file
filewrite = open("write_file.txt", 'w')
for i in range(15):
    sq = i*i
    print(sq)
    filewrite.write(str(sq) + '\n')
    #filewrite.write("\n")

#with for files
with open('learn_file.txt', 'r') as file:
    for line in file:
        print(line)
