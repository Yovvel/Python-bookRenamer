import os
import glob

# Absolute path of a file
old_name = r"C:\Scripts\pythontestfiles\oldfile.txt"
new_name = r"C:\Scripts\pythontestfiles\newfile.txt"

# Renaming the file
#os.rename(old_name, new_name)


for name in glob.glob('C:\Scripts\pythontestfiles\*,*.txt'):
    print(name)
    os.rename(name, new_name)
