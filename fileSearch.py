#! python3
# Ch.9 Pratice Problem - Deleting Uneeded Files
"""
It's uncommon  for a few unneeded but humungous files or folders to take up the bulk of space on your hard drive. 
If you're trying to free up room on your computer, you'll get the most bang for your buck by deleting the most
massive of unwanted files. But first you have to find them. 

Write a program that walks through a folder tree and searches for exceptionally large files or folders - say, 
ones that have a file size of more than 100MB. (Remember, to get a file's size, you can use os.path.getsize()
from the os module.) Print these files with their absolute path to the screen. 

This program does not delete any files, it simply displays the files onto a screen.
"""
import os

# Create the absolute file path we want to walk through
# path = os.path.abspath('.') - We didnt use this because 
# we're in a specific file directory where my python projects are kept.
# We can rewrite the program to ask a user to provide input to search
# for a specific directory. In this case we would use a try and except statement.
path = os.path.abspath('C:\\Program Files/')
print('Searching files...')

# Loop through the files in the working directory and print out files larger
# than 100MB. Since size is in bytes we have to convert 100MB to bytes (100MB = 100000000)
# We create a full, absolute path for the fileName by joining the folderName with the fileName.
# If the size of the fileName is larger than 100MB we print the absolute path and the size of the file. 
for folderName, subFolders, fileNames in os.walk(path):
    for fileName in fileNames:
        # Get the full, absolute file paths.
        fileName = os.path.join(folderName, fileName)
        size = os.path.getsize(fileName)
        # If file size is more than 100MB, print the files with their absolute path to the screen.
        if size > 100000000:
            print('File larger than 100MB: ' + os.path.abspath(fileName) + ' - ' + str(size))
print('Search completed.')
