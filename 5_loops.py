Pokerhand = {"0":"Nothing in hand","1":"One pair","2":"Two pairs","3":"Three of a kind","4":"Straight","5":"Flush","6":"Full house","7":"Four of a kind","8":"Straight Flush","9":"Royal Flush"}
#adding two list
alpha1 = ["a", "b", "c", "d"]
alpha2 = ["e","f","g","h"]
alphabets = alpha1+alpha2


# Iterating over a list of elements
# Note the indentation if mean the code indent is within the for loop
for char in alphabets :
	print(char)


print("Understanding loop depth -- >")
for i in range(5):
	print(" ---- ")
	for j in range(10):
		print(i*j)


#Iterating over a dictionary
for key,value in Pokerhand.items():
	print(key,value)




