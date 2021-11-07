# Bicanic, Iva & Korver, Richard - Dicht bij huis (2020)

import os
import glob

# Renaming the file
#os.rename(old_name, new_name)
folderLocation  = 'C:\\Scripts\\pythontestfiles\\'

# for each epub file in location
for name in glob.glob(folderLocation + '*.epub'):
    print("-" * 100)
    # get  current filename
    oldFileName = name[len(folderLocation):]
    print("filename: " + oldFileName)  

    

    # if there are more authors
    if(oldFileName.find('&')):
        print("'&' found!")
        oldFileNameSplitted = oldFileName.split("&", 1)[1]
        print("splitted: " + oldFileNameSplitted)

        firstWord = oldFileNameSplitted.split()[0]
        print(firstWord)
        if firstWord[-1] == ',':
            print("A comma found!")
            lastNameSecondAuthor = firstWord[:-1]
            firstNameSecondAuthor = oldFileNameSplitted.split()[1]
        else:
            firstNameSecondAuthor = firstWord
            lastNameSecondAuthor = oldFileNameSplitted.split()[1]

    # When the filename layout is as followed: Lastname, Firstname - bookname,
    # we want to change that filename. we search for the comma after the first word
    firstWord = oldFileName.split()[0]
    if firstWord[-1] == ',':
        print("A comma found!")
        lastName = firstWord[:-1]
        firstName = oldFileName.split()[1]

    else:
        firstName = firstWord
        lastName = oldFileName.split()[1]

    print("First name: " + firstName)
    print("Last name: " + lastName)

    print("First name second author: " + firstNameSecondAuthor)
    print("Last name second author: " + lastNameSecondAuthor)
    

    bookTitleWithExtention = oldFileName.split("-", 1)[1]
    bookTitle = bookTitleWithExtention.split(".epub", 1)[0]
    print("Book title: " + bookTitle)

    print("New file name: " + firstName + " " + lastName + " - " + bookTitle)

    #os.rename(folderLocation + oldFileName, folderLocation + firstName + " " + lastName + " - " + bookTitle + ".epub")




print("-" * 100)