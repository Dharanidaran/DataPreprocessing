# 8_filewritter.py

import csv
import os


def convert(Suite1,Rank1,Suite2,Rank2,Suite3,Rank3,Suite4,Rank4,Suite5,Rank5,PokerHand):
	"""
	# 0: Nothing in hand; not a recognized poker hand 
	# 1: One pair; one pair of equal ranks within five cards
	# 2: Two pairs; two pairs of equal ranks within five cards
	# 3: Three of a kind; three equal ranks within five cards
	# 4: Straight; five cards, sequentially ranked with no gaps
	# 5: Flush; five cards with the same suit
	# 6: Full house; pair + different rank three of a kind
	# 7: Four of a kind; four equal ranks within five cards
	# 8: Straight flush; straight + flush
	# 9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush
	"""


	# suite = {1:"Hearts", 2:"Spade", 3:"Diamond" ,4:"Clubs" }
	# rank = {1:"Aces",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen",13:"King"}
	# hand = {0:"Nothing in hand",1:"One pair",2:"Two pairs",3:"Three of a kind",4:"Straight",5:"Flush",6:"Full house",7:"Four of a kind",8:"Straight Flush",9:"Royal Flush"}


	suite = {"1":"Hearts", "2":"Spade", "3":"Diamond" ,"4":"Clubs" }
	rank = {"1":"Aces","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"Jack","12":"Queen","13":"King"}
	hand = {"0":"Nothing in hand","1":"One pair","2":"Two pairs","3":"Three of a kind","4":"Straight","5":"Flush","6":"Full house","7":"Four of a kind","8":"Straight Flush","9":"Royal Flush"}


	#Create an empty temporary list
	card = []

	card1 = rank[Rank1]+" "+suite[Suite1]
	card2 = rank[Rank2]+" "+suite[Suite2]
	card3 = rank[Rank3]+" "+suite[Suite3]
	card4 = rank[Rank4]+" "+suite[Suite4]
	card5 = rank[Rank5]+" "+suite[Suite5]

	#Append Elements into a list
	card.append(card1)
	card.append(card2)
	card.append(card3)
	card.append(card4)
	card.append(card5)
	card.append(hand[PokerHand])
	return card





def WriteToFile(filepath,outputfilepath):

	suite = {"1":"Hearts", "2":"Spade", "3":"Diamond" ,"4":"Clubs" }
	rank = {"1":"Aces","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"Jack","12":"Queen","13":"King"}
	hand = {"0":"Nothing in hand","1":"One pair","2":"Two pairs","3":"Three of a kind","4":"Straight","5":"Flush","6":"Full house","7":"Four of a kind","8":"Straight Flush","9":"Royal Flush"}


	fileObject = open(filepath,'r')
	writeObject = open(outputfilepath,'w')

	csvReader = csv.reader(fileObject,delimiter = ",")
	#Here we use ";" as the delimter to seperate the columns
	csvWriter = csv.writer(writeObject,delimiter = ";")

	while True:
		try:
			# Read the file  
			row = next(csvReader)
			# write the row to the outputfilepath 
			writerow = convert(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
			csvWriter.writerow(writerow)

		except StopIteration:
			print("Reached end of the file")
			break
		except:
			print("General exception")
			print("Close the file objects opened")
			break

currentWorkingDirector =  os.getcwd()
filepath = os.path.join(currentWorkingDirector,'DataFolder','pokerData.csv')
outputfilepath = os.path.join(currentWorkingDirector,'DataFolder','pokerDataReadable.csv')


WriteToFile(filepath,outputfilepath)
