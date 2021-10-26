import os
import glob

# Absolute path of a file
old_name = r"C:\Scripts\pythontestfiles\oldfile.txt"
new_name = r"C:\Scripts\pythontestfiles\newfile.txt"

# Renaming the file
#os.rename(old_name, new_name)
folderLocation  = 'C:\\Scripts\\pythontestfiles\\'

# for each file in location
for name in glob.glob(folderLocation + '*,*.epub'):

    # get  current filename
    fileName = name[len(folderLocation):]
    #print("filename: " + fileName)

    # get first word of file
    lastName = fileName.split()[0]
    # remove the comma
    lastName = lastName[:-1]
    #print("Last name: " + lastName)

    # get second word
    firstName = fileName.split()[1]
    #firstName = firstName[:-4]    # Later wordt dit -5 voor epub files
    #print("First name: " + firstName)

    bookTitle = fileName[(len(firstName + lastName ) + 2):]
    #print("Book title: " + bookTitle)

    affix  = os.path.splitext(name)[1]
    #print("affix: " + affix)

    newFileName = firstName + " " + lastName + bookTitle
    #print ("new name: " + newFileName)
    print("Old filename: " + fileName)
    print("New name:  " + name, folderLocation + newFileName)
    os.rename(name, folderLocation + newFileName)
