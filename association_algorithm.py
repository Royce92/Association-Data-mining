import itertools
import ast

minSup = .50
page= 491
Confidence = 0.5
minTimes = minSup*page
out = open('output.txt', 'w')
def beta(file):
    pager = 0
    file = open(file)
    ##Read the index file and create key value pair
    data = file.readlines()
    file.close()
    dic = {}
    for words in data:
        word = words.split()
        key = word[0]
        value = str(word[1:]).replace("[", "").replace("]","").replace('"','').strip().replace(",","")
        for val in value.split():
            val=ast.literal_eval(val)
            if key not in dic:
                dic[key] = [val]
            else:
                dic[key].append(val)
            
    firstOrderPotential = {} ## first order
    
    for words in dic:
        support =  len(dic[words])
        if support >= minTimes:
            firstOrderPotential[words] = dic[words]
    
    firstOrder = []
    for d in firstOrderPotential:
        level1 = len(firstOrderPotential[d])
        if level1 >= minTimes:
            firstOrder.append(d)
        

            
    secondPotential= []
    secondOrder = []
    for index0 in range(0, len(firstOrder)):
        for index1 in range(index0+1, len(firstOrder)):
            count = 0
            pair = [firstOrder[index0], firstOrder[index1],]
            for val in firstOrderPotential[firstOrder[index1]]:
                if val in firstOrderPotential[firstOrder[index0]]:
                    count +=1
                    S = count/page
                    C= count/len(firstOrderPotential[pair[0]])
                    if S >= minSup and pair not in secondOrder and C >= Confidence :
                        pair = [firstOrder[index0], firstOrder[index1]]
                        
                        output = (str(pair[0])+ " ==> "  + str(pair[1]) + ": Support:"+str(round(S,2))+ " Confidence:"+str(round(C,2)))
                        print(output)
                        pager +=1
                        secondOrder.append(pair)
                        out.write(str(pager) +": "+ str(output) + '\n')

                
    ThirdPotential = []
    thirdOrder = []

    for index0 in range (len(secondOrder)):
        for index1 in range(1+index0, len(secondOrder)):
            third = secondOrder[index0]+secondOrder[index1]
            for word in third:
                if third.count(word) >=2:
                    third.remove(word)                    
            ThirdPotential.append(third)

    FourthOrder = []
    for word in ThirdPotential:
        counter=0
        for val in firstOrderPotential[word[0]]:
            if val in firstOrderPotential[word[1]] and val in firstOrderPotential[word[2]]:
                counter+=1
                thirdS = counter/page
                thirdC = counter/ len(firstOrderPotential[word[0]])
                if thirdS >= minSup and word not in thirdOrder and C >= Confidence and (len(word)==3):
                    thirdOrder.append(word)
                    output = str(word[0])+" ==> "+ str(word[1:])+": Support: "+ str(round(thirdS,2))+ " Confidence:" + str(round(thirdC,2))
                    print(output)
                    pager +=1 
                    out.write(str(pager) +": "+ str(output) + '\n')
                if thirdS >= minSup and word not in FourthOrder and len(word) >3:
                    FourthOrder.append(word)
  
    for level4 in FourthOrder:
        for i in range(3):
            a = level4.pop(i)
            b = level4.pop(i)
            cd = level4
            print(a,b, "=>",cd)
            print(cd, "=>", a,b)
            level4.insert(i,a)
            level4.insert(i,b)
    out.close()

beta("index.txt")



        

        

        

              

