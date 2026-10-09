

list_of_strings = ["ekemini", 'chibuzor', 'mr ebuka', 'naafiu', 'mr majek', 'gloryyy', 'abba', 'anna']

count = 0
firstLetter = ""
lastLetter = ""
matchingIndex = ""


for index in range(0, len(list_of_strings)):

    #count += 1

    if( len(list_of_strings[index]) >= 2 ):

            for indexTwo in range(0, len(list_of_strings[index]) ):
            
                    if(indexTwo == 0):
                            firstLetter += (list_of_strings[index])[indexTwo]
                            #print(firstLetter)   


                    if(indexTwo == (len(list_of_strings[index])-1) ):
                            lastLetter += (list_of_strings[index])[indexTwo] 
                            #print(lastLetter) 


                            if(firstLetter == lastLetter):
                                    matchingIndex = list_of_strings[index]

                                    count += 1
                                    
                                    print(matchingIndex)

                                    #print(firstLetter) 
                                    #print(lastLetter) 

          

    else :
        print("string length is less than 2")

    firstLetter = ""
    lastLetter = ""   


#print(matchingIndex)

