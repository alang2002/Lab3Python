# Python Project (Lab 3)
# Purpose: Randomly generate a quote based on the category the user selects, using random int generator
# Aaron Lang
# 9/20/2020

import random

# Read the file and parse through it
quotes = open("quotes.txt")
qList = quotes.read().split("\n")
quotesDictionary = {}
currentCategory = ""

# Add categories as keys to dictionary, else add quotes as values to keys
for line in qList:
	if line[0] != '"':
		currentCategory = line
		quotesDictionary[currentCategory] = []
	else:
		quotesDictionary[currentCategory].append(line)

# Turns the dictionary into a list
categoryList = list(quotesDictionary)

# Prints the categories with numbers for the user
for i in range(0, len(categoryList)):
	print(str(i+1) + "." + categoryList[i])

userChoice = 0
while (userChoice != -1):
	userChoice = int(input("Select your category!\nType -1 to exit\n"))
	# There is a better way to do this, but I need to do it this way to include the elif
	if (userChoice == 1):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[0]]) - 1)
		print(quotesDictionary[categoryList[0]][quoteSelected])
	elif (userChoice == 2):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[1]]) - 1)
		print(quotesDictionary[categoryList[1]][quoteSelected])
	elif (userChoice == 3):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[2]]) - 1)
		print(quotesDictionary[categoryList[2]][quoteSelected])
	elif (userChoice == 4):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[3]]) - 1)
		print(quotesDictionary[categoryList[3]][quoteSelected])
	elif (userChoice == 5):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[4]]) - 1)
		print(quotesDictionary[categoryList[4]][quoteSelected])
	elif (userChoice == 6):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[5]]) - 1)
		print(quotesDictionary[categoryList[5]][quoteSelected])
	elif (userChoice == 7):
		quoteSelected = random.randint(0, len(quotesDictionary[categoryList[6]]) - 1)
		print(quotesDictionary[categoryList[6]][quoteSelected])
	else:
		print("'Not a category.' - Aaron Lang")