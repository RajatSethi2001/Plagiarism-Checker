FileColName = input(); #Input list of files
T = eval(input()); #Amount of Matches Required for Reporting
LenK = eval(input()); #Amount of Matching Words Required for being a "Match"
print("NAME OF THE FILE COLLECTION: " + FileColName + '\r');
print("SIMILARITY THRESHOLD (T): " + str(T) + '\r');
print("SEQUENCE LENGTH (K): " + str(LenK) + '\r');
FileCol = open(FileColName, 'r', encoding='utf-8');
FileNames = [];

data = 'proxy';

while (data != ''): #Read every text file in the list
    data = FileCol.readline();
    data = data.replace('\n', '');
    DoesFileExist = True;
    try: #Does the file actually exist?
        FileCheck = open(data, 'r', encoding='utf-8');
    except: #If the file does not exist, don't add it to the list of files.
        DoesFileExist = False;
    
    if DoesFileExist:
        FileNames.append(data);

#print(FileNames);

words = []; #Turns the files into String Arrays and stores them into one giant list. 
for i in range(len(FileNames)): #For every file
    TempFile = open(FileNames[i], 'r', encoding='utf-8');
    text = TempFile.readlines();
    separator = ' ';
    passage = separator.join(text); 
    
    #Replace all of the newlines, punctuation, and other garbage with empty strings
    passage = passage.replace('\n', '');
    passage = passage.replace('\t', '');
    passage = passage.replace('\r', '');
    passage = passage.replace('Õ', '');
    passage = passage.replace('Ó', '');
    passage = passage.replace('Ò', '');
    passage = passage.replace('Ô', '');
    passage = passage.replace('!', '');
    passage = passage.replace('?', '');
    passage = passage.replace(':', '');
    passage = passage.replace(';', '');
    passage = passage.replace('.', '');
    passage = passage.replace(',', '');
    passage = passage.replace('(', '');
    passage = passage.replace(')', '');
    passage = passage.replace('\"', '');
    passageArr = passage.split(' '); #Split the mega-string into an array (separate all of the words)
    passageArr = list(filter(lambda a: a != '', passageArr));

    words.append(passageArr); #Add to the mega-list of words

wordSet = []; #Takes all of the unique words of every file and shoves them into another list
for i in range (len(words)): #Look at every file
    mySet = set(words[i]); #Create a set for that file
    #for j in range (len(words[i])): #Keep adding words to the set, removing any non-unique words
        #mySet.add(words[i][j]);
    
    myList = list(mySet); #Convert the set into a list
    #myList.insert(0, FileNames[i]);
    wordSet.append(myList); #Add the new unique list into the wordSet list

#print(wordSet);

wordLocations = []; #Find the locations of every word in every file
for i in range (len(wordSet)): #For Every Text File
    textLocations = [];
    for j in range (len(wordSet[i])): #For Every Unique Word in the Text File
        locations = [];
        for k in range(len(words[i])): #For Every Word in the Text File
            if (wordSet[i][j] == words[i][k]): #If the word in the set matches the word in the file
                locations.append(k); #Add the location (k) onto the location list
        textLocations.append(locations); #Take all of the locations of that one word and put it into the file's location bank
    wordLocations.append(textLocations); #Take all of the location banks and combine it into one mega-list

#print(wordLocations);

AllMatches = []; #A list that will contain the matches of each file pair (when matches > T)
LargestMatchTotal = 0; #Global variables for largest match and their respective files
LargestLocationA = 0;
LargestLocationFileA = '';
LargestLocationB = 0;
LargestLocationFileB = '';
#print(words[1]);
for i in range (len(words)): #First File
    for j in range (i + 1, len(words)): #Second File
        FirstFile = words[i].copy();
        SecondFile = words[j].copy();
        SecondFileUnique = wordSet[j].copy();
        amountOfMatches = 0;
        k = 0;
        while k < len(words[i]): #For every word in the first file
            myWord = FirstFile[k];
            try:
                existInSecond = SecondFileUnique.index(myWord); #If that word exists in the Second File, keep going
            except: 
                existInSecond = -1;
                k += 1;
           
            if (existInSecond != -1):           
                locationsInSecond = wordLocations[j][existInSecond]; #Find the locations of the word in the Second File
                for l in locationsInSecond:
                    a = k; #Starting positions to begin checking for a match
                    b = l;
                    matchLen = 0; #Length of the match
                    MatchSoFar = True;
                    while (a < len(FirstFile) and b < len(SecondFile) and MatchSoFar): #If the words match
                        if (FirstFile[a].lower() == SecondFile[b].lower()):
                            FirstFile[a] = '';
                            #SecondFile[b] = '';
                            matchLen += 1;
                            a += 1; #Move on to the next word and check for another match
                            b += 1;
                        else:
                            MatchSoFar = False;
                            
                    k = a;
                
                    if (matchLen > LargestMatchTotal and matchLen >= LenK): #If the word match length is the largest yet
                        LargestMatchTotal = matchLen; #Establish new largest match
                        LargestLocationA = a - matchLen; #Starting Location of match in the first file
                        LargestLocationFileA = FileNames[i]; #Name of the First File
                        LargestLocationB = b - matchLen; #Starting Location of match in the second file
                        LargestLocationFileB = FileNames[j]; #Name of the Second File
                
                    if (matchLen >= LenK): #If the match length is greater than K 
                        amountOfMatches += 1; #Increase the number of matches found for these two files
                        
                
        if (amountOfMatches >= T): #If the amount of matches found between these two files are greater than T
            AllMatches.append([amountOfMatches, FileNames[i], FileNames[j]]); #Print it out later and place into the AllMatches list
            

print('\r');
print("NUMBER OF MATCHES PER FILE PAIR WHERE T = " + str(T) + " AND K = " + str(LenK) + ":\r");
print('\r');
AllMatches = sorted(AllMatches); #Sort the matches found 
AllMatches.reverse(); #Reverse the sorted list (greatest first)
for i in range(len(AllMatches)): #For every match found
    firstStr = str(AllMatches[i][0]) + ": ";
    print(firstStr + AllMatches[i][1]  + ", " + AllMatches[i][2] + '\r'); #Print out the match
    
print('\r');
print("LONGEST SEQUENCE OF MATCHING TEXT:\r"); #Print information of largest match
print('\r');
print("Match length: " + str(LargestMatchTotal + 1) + '\r'); 
print("Source 1: At location " + str(LargestLocationA + 1) + " in file " + LargestLocationFileA + '\r');
print("Source 2: At location " + str(LargestLocationB + 1) + " in file " + LargestLocationFileB + '\r');
print('\r');
print("Matching words:\r");
try:
    tempFileA = open(LargestLocationFileA, 'r', encoding='utf-8');
    text = tempFileA.readlines();
    separator = ' ';
    passage = separator.join(text);
    passageArr = passage.split(' ');
    passageArr = list(filter(lambda a: a != '', passageArr));
    
    stolenStr = '';
    for i in range(LargestLocationA, LargestMatchTotal + LargestLocationA):
        stolenStr = stolenStr + ' ' + passageArr[i]; #Add all the matching words together

    stolenStr = stolenStr[1:];
    print(stolenStr + '\r'); #And print it out
except:
    print();

            