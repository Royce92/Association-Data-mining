def createIndex(directory):
    import os, string, re
    index = {}                                                                              #Create the index dictionary
    fileNum = 0                                                                             #Counter to keep track of file numbers

    stopwords = open('stop-words_english_en.txt', 'r').read().split()
    
    for file in os.listdir(directory):                                                      #Look for files in a specified directory
        cleanwords = []                                                                     #List to add the stripped/cleaned words

        if file.endswith(".txt"):                                                           #Look for solely .txt files
            fileNum += 1                                                                    #Add one to the counter if file found
            words = open(file, 'r').read().split()                                          #Open the file, read it and split it by words

            for phrase in words:                                                            #For loop to go through each item in words
                lower = phrase.lower().strip().strip('\^`')                                 #Strip the item of trailing & leading symbols/spaces & lowercase
                clean = re.sub("[^a-zA-z]",'', lower).strip()
                                                                                            #Assured word contained alphabet characters & stripped again 
                if clean not in cleanwords and clean not in stopwords:
                    cleanwords.append(clean)                                                    
                                                                                            
            for i in range(len(cleanwords)):                                                #For loop to run for each word in the clean words list
                word = cleanwords[i]                                                        #Equal the word at that index in order to give position
                
                if word not in index and len(word) > 1:                                     #Add the word to the index if its length is greater than 1
                    index[word] = [str(fileNum)]                                            #Create the instance of the word in the dictionary with file                                                                                            #number and position in the file
                elif word in index and len(word) > 1:                                       #If the word is in the index and its length is greater than 1
                    index[word].append(str(fileNum))

    save = open('index.txt', 'w') ##create index file for writing.
    for key in index: ## get key and value pair one by one
        save.write(str(key) + ' ' + str(index[key]) + '\n') ##write the and valued pair and go to the next line.
    save.close()
    print(counter,"Files has been successfully Scanned")
createIndex("C:/Users/jefrey/Desktop/Classes/crawlerr/Source/")




