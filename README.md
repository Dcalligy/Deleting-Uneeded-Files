# Deleting Uneeded Files
This practice problem is from chapter 9 of Automate the Boring Stuff with Pyhton.

## The problem states the following

It's uncommon  for a few unneeded but humungous files or folders to take up the bulk of space on your hard drive. 
If you're trying to free up room on your computer, you'll get the most bang for your buck by deleting the most
massive of unwanted files. But first you have to find them. 

Write a program that walks through a folder tree and searches for exceptionally large files or folders - say, 
ones that have a file size of more than 100MB. (Remember, to get a file's size, you can use os.path.getsize()
from the os module.) Print these files with their absolute path to the screen. 
