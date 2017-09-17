# 7_fileReading.py


#Reading a file using For loop
import os
currentWorkingDirector =  os.getcwd()
pathToFile = os.path.join(currentWorkingDirector,'DataFolder','pokerData.csv')
print("Reading the file "+ pathToFile)
# fileObject = open(filepath,'r')


try :
	fileObject = open(pathToFile,'r')
	#Loop through entire file and print
	for line in fileObject:
		print(line)
	fileObject.close()

except:
	print("Error while processing the file")

#######################################################
#######################################################
#######################################################
#Reading a file as table, using csv module
import csv

currentWorkingDirector =  os.getcwd()
pathToFile = os.path.join(currentWorkingDirector,'DataFolder','pokerData.csv')
print("Reading the file "+ pathToFile)


fileObject = open(pathToFile,'r')
csvReader = csv.reader(fileObject,delimiter=",")
table = []


while True:
	try:
		row = next(csvReader)
		#Reade the file and save it to a list
		table.append(row)
	except StopIteration:
		print("Reached end of  exception")
		break
	except:
		print("General exception")
		break



print("------------------------->>>>")
print("Printing the first 100 rows")
# Print the first 100 rows of the file saved
for line in table[0:100]:
	print(line)

print("Printing the pokerhand alone")

hand = {
		"0":"Nothing in hand","1":"One pair","2":"Two pairs",
		"3":"Three of a kind","4":"Straight","5":"Flush",
		"6":"Full house","7":"Four of a kind","8":"Straight Flush",
		"9":"Royal Flush"
	}


for line in table[0:100]:
	#Printing the poker hand or the last row in the data column
	print(hand[line[-1]])



# Write a loop to iterate over the table variable and find 
# the percentage of "Full house"
# Excerise for readers
# Hint - Use python len() function to calculate total number of rows





