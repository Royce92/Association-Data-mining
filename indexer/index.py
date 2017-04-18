import os, sys
def indexer ():
    path ="./Source/"
    dirs = os.listdir( path )
    dic = {}
    counter = 0
    unique = 0
    for file in dirs: ##Scan each file one by one
        print(counter)
        counter += 1 ##Increase the counter everytime a file is open
        Op = open(path+file, encoding="utf-8-sig", errors='ignore') ##Open file
        Op = Op.read().split()##read the file and split
        for i in range(len(Op)): ##Scan the entire length of the file make i the possition
            word = Op[i]  ##Op[i] is the word possition
            doc = str(counter)
            if word not in dic and len(word) > 2: ##if Word not in dictionary                                        
                dic[word] = [doc]            ##and the word length is greater than 2
            if word in dic and len(word) > 2 and doc not in dic.values(): ## if word already in dictionary append
                dic[word].append(doc)




                
    save = open('index.txt', 'w') ##create index file for writing.
    s = sorted(dic.keys()) ##sort dictionary key by alphabetical order
    for key in s: ## get key and value pair one by one
        save.write(str(key)  + '\n') ##write the and valued pair and go to the next line.
        unique += 1 ## increase unique by one to keep track of the unique words.
    save.close()
    print(counter,"Files has been successfully Scanned")
indexer()

   
