# 6_function.py
# Functions are code snippets that gets execute when called
# Syntax for function
# def functioname():
# 	Function code....

def displayfunction():
	print("Function block is executed")

#Calling the function
displayfunction()

def functionWithArgument( arg1,arg2):
	#Function body goes here
	print(arg1+arg2)

#Calling the function
functionWithArgument(2.0,5.5)

import os
pathToDir = os.getcwd()
def ListDirectory(dirpath):
	# check if the argument dirpath is a dirpath
	if (os.path.isdir(dirpath)):
		print(  os.listdir(dirpath) )
	else:
		print("The dirpath provided does not point to valid directory")

# Calling the function
ListDirectory(pathToDir)
ListDirectory('this/is/invalid/path/to/a/directory')

# Calling a function within a for loop
for i in [0,1,2,3,4,5]:
	functionWithArgument(i,i+1)






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


	#Dictionary defined inside function
	suite = {1:"Hearts", 2:"Spade", 3:"Diamond" ,4:"Clubs" }
	rank = {1:"Aces",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen",13:"King"}
	hand = {0:"Nothing in hand",1:"One pair",2:"Two pairs",3:"Three of a kind",4:"Straight",5:"Flush",6:"Full house",7:"Four of a kind",8:"Straight Flush",9:"Royal Flush"}

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



#Calling the function with the arguments
print(convert(1,10,3,3,3,10,2,10,4,3,1))
print(convert(4,10,2,1,4,11,3,11,2,11,3))
print(convert(1,11,3,12,3,10,4,9,2,13,4))