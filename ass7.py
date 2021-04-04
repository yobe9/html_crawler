"""
Yoav Berger
313268393
01
ass07
"""

# the difference from index we find to start of the link
strDiff = 6

"""
* Function Name: fillDictionary
* Input: file_Str, hyper_Lst, begin
* Output: void
* Function Operation: takes string of whole file and scans it to find hyperlinks
                      when we find a link, insert it to a list
"""
def fillDictionary(fileStr, hyperLst, begin):

    # if there is hyper link in the file/ rest of the file
    if fileStr.find("href=", begin) == -1:
        return

    # setting the places of the hyperlink so we can cut it and save it
    begin = fileStr.find("href=", begin) + strDiff
    finish = fileStr.find('"', begin)
    hyperName = fileStr[begin:finish]
    hyperLst.append(hyperName)

    # recursive call to the func so we keep read the file
    fillDictionary(fileStr, hyperLst, finish)

"""
* Function Name:recursiveDictionary
* Input: filesDictionary, key
* Output: void
* Function Operation: fill the dictionary in a recursive call
"""
def recursiveDictionary(filesDictionary, key):

    # iterating threw objects in the list of specific key
    # if there is no objects in the list or the object already have a key return
    for value in filesDictionary[key]:
        if value is None:
            return
        if value in filesDictionary:
            return

        # setting a new key for the object from the list, and scans it's file
        # creating a list of hyperlinks and insert it into the new key's value
        # afterwards calls recursively
        else:
            filesDictionary[value] = None
            tmpLst = []
            htmlFile = open(value, "r")
            htmlFileStr = htmlFile.read()
            htmlFile.close()
            fillDictionary(htmlFileStr, tmpLst,0)
            filesDictionary[value] = tmpLst
            recursiveDictionary(filesDictionary, value)
    return

# functioning as a main, input the users source file, create the first keys and values
# and calls to the recursive function, and print
usersFile = input("enter source file:\n")
filesDictionary = {usersFile: None}
first_file = open(usersFile, "r")
fileStr = first_file.read()
first_file.close()
lst = []
fillDictionary(fileStr, lst, 0)
filesDictionary[usersFile] = lst
recursiveDictionary(filesDictionary, usersFile)
#print(filesDictionary)

# creating csv file, converting the dictionary into right format and insert it to the file
newCsvFile = open("results.csv", "w")
linesCounter = 0
for i in filesDictionary:
    newStr = i + ","
    for j in filesDictionary[i]:
        newStr = newStr + j + ","
    newStr = newStr[:-1] + "\n"
    linesCounter = linesCounter + 1
    if linesCounter == len(filesDictionary):
        newStr = newStr[:-1]
    newCsvFile.write(newStr)
newCsvFile.close()

# gets file name as input from the users and print its list of values in a "alpha-betic" sorted way
usersChoice = input("enter file name:\n")
usersLst = filesDictionary[usersChoice]
usersLst.sort()
print(usersLst)
