# Bicanic, Iva & Korver, Richard - Dicht bij huis (2020)

import os
import glob
import re
from datetime import date

# Renaming the file
#os.rename(old_name, new_name)
bookLocation  = 'C:\\Scripts\\pythontestfiles\\'
documentLocation = 'C:\\Scripts\\pythontestfiles\\'

# Functions
def getFileName(name):
    # function to get the filename without it's location
    return name[len(bookLocation):]

def getFirstName(fileName):
    # When the filename layout is as followed: Lastname, Firstname - bookname,
    # we want to change that filename. we search for the comma after the first word
    firstWord = fileName.split()[0]
    if firstWord[-1] == ',':
        firstName = fileName.split("-",1)[0]
        firstName = firstName.split(",",1)[1]
        return firstName[1:]
    else:
        return firstWord + " "

def getLastName(filename):
    firstWord = filename.split()[0]
    if firstWord[-1] == ',':
        return firstWord[:-1]
    else:
        return filename.split(' ')[1]

def getBookTitle(filename):
    title = filename.split("-", 1)[1]
    title = title.split(".epub", 1)[0]
    print("Book title: " + title)
    # remove from which year the book is from
    title = re.sub("\([0-9][0-9][0-9][0-9]\)",'', title)
    print("Book title(removed year): " + title)
    title = re.sub("(epub)",'', title)    
    return title


# start of program
today = date.today()
today = str(today)
file = open(documentLocation + "Log\\" + today + ".txt", "a")

# for each epub file in location
for name in glob.glob(bookLocation + '*.epub'):
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
        lastName = getLastName(oldFileNameFirstPart) + " &"
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
    bookTitle = getBookTitle(oldFileName)


    if multipleAuthors == True:
        print("First name second author: " + firstNameSecondAuthor)
        print("Last name second author: " + lastNameSecondAuthor)
        newFileName = firstName + lastName + firstNameSecondAuthor +  lastNameSecondAuthor + " -" + bookTitle
    else:
        newFileName = firstName + lastName + " -" + bookTitle
    
    print("New file name: " + newFileName)

    #os.rename(folderLocation + oldFileName, folderLocation + firstName + " " + lastName + " - " + bookTitle + ".epub")
    file.write( "-" * 50 + "\n")
    file.write("= Originele bestandsnaam:\n     " + oldFileName + "\n")
    file.write("= Nieuwe bestandsnaam:\n    " + newFileName + "\n")


print("Datum: " + str(date.today()))
print("-" * 100)