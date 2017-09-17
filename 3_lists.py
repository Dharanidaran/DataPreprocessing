"""
	One of the important data structure that you cannot escape if you intent to use
	python, is lists. Lists is a sequencial data structure and each 
	element of the sequence is assigned a index. We can access the elements in 
	the list using its index

"""


courses = ['MBA', 'Business', 'python']
numbers = [1, 2, 3, 4, 5 ]
alphabets = ["a", "b", "c", "d"]


# Accessing Values in List
# Lists are Zero indexed

# print the first element from the list numbers
print(numbers[0])
#print the second element from the list numbers
print(numbers[1])

#print the last element from the list numbers
#we can use negative index to traverse in reverse direction
print(numbers[-1])


# Updating list
#printing the hole list
print(courses)


# Let us add a new course to the courses list
courses.append("Machine Learning")
print(courses)

alphabets.append("e")
print(alphabets)


# Removing a element form the list
del courses[-1]
print(courses)



#adding two list
alpha1 = ["a", "b", "c", "d"]
alpha2 = ["e","f","g","h"]

alphabets = alpha1+alpha2
#List concatenation

print(alphabets)



#Finding the length of the list element
print(len(numbers))

# Visit the link to learn to try some examples
# https://www.tutorialspoint.com/python/python_lists.htm