#!/usr/bin/python3

# Title Fixer by Michelle Warren from engineerbabe.com | 2021
# This script takes user input of a directory and decodes UTF-8 encoded
# bytes of files with a user-defined extension, so that your file names
# can be human-readable!
# See git repo for details. Thanks for using!

# Make needed python modules available. 
import shutil
import glob
import sys
import os
from os import listdir
from os.path import isfile, isdir, join
import urllib.parse

print("\n\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f Hi there! Thanks for using the title_fixer.py script by Michelle Warren from engineerbabe.com!\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f\n")

# Ask User to define the folder where files are stored
user_input = input("Enter the directory of your files: ")

# Check if that folder exists
isDir = isdir(user_input)
if isDir == False: 
	print("\n Oop! That directory path does not exist. Try again. \n")
	
else:
	onlyfiles = [f for f in listdir(user_input) if isfile(join(user_input,f))]
	
	# Print the files in that directory
	print("\nHere's a list of all the files in the directory '%s':\n" % user_input)
	for i in onlyfiles:
		print("    %s" % i)
	print("\n")

	# Confirm that this is the desired directory
	confirm = input("Is this the directory you wanted? Y/N ")
	if confirm == "Y" or confirm == "y":
		print("Cool beans!\n")

		# Ask the user for the desired extension
		ext = input("What is the extension of the file(s) you'd like to change? For example, '.doc', '.mp3', etc.: ")
		files = glob.glob('%s/*%s' % (user_input,ext))

		# Print names of files with that extension
		for j in files:
			print(j)

		# UTF-8 decode the file names
		for f in files:
			newFileName = urllib.parse.unquote(f)
			shutil.move(f,newFileName)
		print("Your file names have been fixed! Here are their new names:")

		# Print the new file names
		newfiles = [f for f in listdir(user_input) if isfile(join(user_input,f))]
		for k in newfiles:
                	print(k)
		
	elif confirm == "N" or confirm == "n":
		print("Oop. Try again!")

	else:
		print("Sorry. Input invalid. Try again.") 

