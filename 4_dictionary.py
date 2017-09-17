#Dictionary is a key-value store 
suite = {1:"Hearts", 2:"Spade", 3:"Diamond" ,4:"Clubs" }
rank = {"1":"Aces","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"Jack","12":"Queen","13":"King"}
hand = {"0":"Nothing in hand","1":"One pair","2":"Two pairs","3":"Three of a kind","4":"Straight","5":"Flush","6":"Full house","7":"Four of a kind","8":"Straight Flush","9":"Royal Flush"}


#Let us retreive a value using a key
print(suite[1])
print(hand["9"])


# Updating Dictionary

#Let us add a new suite to the cards
suite [5]="Jokker"

print(suite)


# Try retreive and Updating values from the other Dictionary



# Deleting Dictionary elements
del suite[5]
print(suite)