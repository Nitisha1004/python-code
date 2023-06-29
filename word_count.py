# The sys module in Python provides various functions and
#  variables that are used to manipulate different parts of 
# the Python runtime environment. It allows operating on the interpreter 
# as it provides access to the variables and functions 
# that interact strongly with the interpreter. 
import sys
# word count is function to calculate word in present string 
def wordCount(text):
    # split method splits a string into a list.
    # then separator is any whitespace.
    word=text.split()
    # return length of words
    return len(word)
# To achieve this using the sys module, the sys 
# module provides a variable called sys.argv.
# then len (sys.argv) is not equal to 2  that either no argument 
# or more than one argument was provided.
if len(sys.argv)!=2:
    print("Usage: Python word_count.py ,")
    #  Exits the program with a status code of 1, 
    # indicating an error or abnormal termination.
    sys.exit(1)
# sys.argv is a list in Python that contains the
#  command line arguments passed to the script. 
text=sys.argv[1]
# invoked the function wordcount then return the value store
#  in count variable.
count=wordCount(text)
# Print the word count in given statement in command
print("Word Count : ",count)