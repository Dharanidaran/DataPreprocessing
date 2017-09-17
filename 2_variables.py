# Creating a variable

#The variable path holds a string value
path = "some string value"
print(path)

#The variable path now holds a different string value
path = "path/to/a/file/we/want/to/point/to"
print(path)

# Python variable of are dynamic, 
# now the same variable path can hold a different object type
# in the following case it holds an integer

path = 123
print(path)


# Let us import a module
import os

#Save the path returned by the function getcwd onto a variable "path"
directory= os.getcwd()
print(directory)
filename = "myfile.csv"


path = directory+filename
#Let us print the path of our file name
print(path)

# My path looks like this 
# /Users/dharanidaran/Developer/PythonMan/myfile.csv

# But your might be different based on where the file is located and the OS
# If you are windows user that path might look like
# c:\\Username\\path\\to\\file
# The os module helps us to bridge the disparity between operation system.
# The code fail to locate the path to file if we try write the path manually.


#Let us list all the files in a directory
print(  os.listdir(directory) )


# Lets suppose we have a file named = pokerData.csv and we 
# want a variable to hold on the path to the file
pathToDir="/Path/To/Directory/"
filename = "pokerData.csv"
pathToFile = pathToDir + filename
print(pathToFile)

# Generating path string dynamically using the os.path.join() function 
pathToDir = os.getcwd()
print(pathToDir)
filename = "pokerData.csv"


filepath = os.path.join(pathToDir,filename)
print(filepath)
#This means the code does not fail to find the path to the file when it shipped to different 
# Operating system or if the project folder is moved to a different location





