# Bicanic, Iva & Korver, Richard - Dicht bij huis (2020)

import os
import glob
import re

# Renaming the file
#os.rename(old_name, new_name)
folderLocation  = 'C:\\Scripts\\pythontestfiles\\'

# Functions
def getFileName(name):
    # function to get the filename without it's location
    return name[len(folderLocation):]

def getFirstName(fileName):
    # When the filename layout is as followed: Lastname, Firstname - bookname,
    # we want to change that filename. we search for the comma after the first word
    firstWord = fileName.split()[0]
    if firstWord[-1] == ',':
        firstName = fileName.split("-",1)[0]
        return firstName.split(",",1)[1]
    else:
        return firstWord

def getLastName(filename):
    firstWord = filename.split()[0]
    if firstWord[-1] == ',':
        return firstWord[:-1]
    else:
        return filename.split(' ')[1]
    
# start of program

# for each epub file in location
for name in glob.glob(folderLocation + '*.epub'):
    print("-" * 100)
    
    # get  current filename
    oldFileName = getFileName(name)
    print("filename: " + oldFileName)  

    # if there are more authors
    if(re.search("&",oldFileName)):
        print("'&' found!")
        oldFileNameFirstPart = oldFileName.split("&", 1)[0]
        oldFileNameLastPart = oldFileName.split("&", 1)[1]
        print("First part: " + oldFileNameFirstPart)
        print("Last part: "+ oldFileNameLastPart)
        oldFileNameSplitted = oldFileName.split("&", 1)[1]
        print("splitted: " + oldFileNameSplitted)
        firstNameSecondAuthor = getFirstName(oldFileNameLastPart)
        lastNameSecondAuthor = getLastName(oldFileNameLastPart)
        firstName = getFirstName(oldFileNameFirstPart)
        lastName = getLastName(oldFileNameFirstPart) + " & "
        multipleAuthors = True

    else:
        firstName = getFirstName(oldFileName)
        lastName = getLastName(oldFileName)
        multipleAuthors = False


    print("First name: " + firstName)
    print("Last name: " + lastName)

    # print("First name second author: " + firstNameSecondAuthor)
    # print("Last name second author: " + lastNameSecondAuthor)
    
    # Get the book title
    bookTitleWithExtention = oldFileName.split("-", 1)[1]
    bookTitle = bookTitleWithExtention.split(".epub", 1)[0]
    print("Book title: " + bookTitle)
    # remove from which year the book is from
    bookTitle = re.sub("\([0-9][0-9][0-9][0-9]\)",'', bookTitle)
    print("Book title(removed year): " + bookTitle)

    if multipleAuthors == True:
        print("First name second author: " + firstNameSecondAuthor)
        print("Last name second author: " + lastNameSecondAuthor)
        newFileName = firstName + "," + lastName + firstNameSecondAuthor + "," +  lastNameSecondAuthor + ",-," + bookTitle
    else:
        newFileName = firstName + lastName + " -" + bookTitle

    print("New file name: " + newFileName)

    #os.rename(folderLocation + oldFileName, folderLocation + firstName + " " + lastName + " - " + bookTitle + ".epub")




print("-" * 100)