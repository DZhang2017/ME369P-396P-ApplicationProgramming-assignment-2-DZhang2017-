## Assignment2 ME369P/ME396P
## Name: <fill in the blank>
## EID : <fill in the blank>
## Section: <fill in the blank>

## Fill in the class and functions below. 
## Make sure your class runs with the tests in main
## You may use any imports, but do not use any import function for 
##      norm calculation or matrix operations. Be wary of numpy.

import random

'''
PROBLEM 1
Assume if a kwarg is not present, you should create the basic matrix
Assume the style is default to random
Assume the set is default to [0, 1]
kwargs can be :
    n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
    i =>  number of rows     NOTE: If i is passed, assume j will be too
    j =>  number of columns
    range => [min, max] list 
                NOTE: Can also be reversed [max,min]
    set   => [number1, ..., numberN]
                NOTE: If set is specified, use that over range
                NOTE: If not specified, assume the set is the range
    style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                NOTE: Any non-square matrix will be random
                NOTE: Different styles will always be square matrices
                NOTE: Use zeroes in the stylized matrices even if not in the given numbers
    format1 => string for formating 1st  element of each row
    format2 => string for formating last element of each row
                NOTE: If both formats are '', assume the default of no format
                NOTE: If one format is '', assume the other format is a string that is reversable
Assume all matrix entries are a single digit (i.e. no 10's 100's, etc)
'''
class myAwesomeMatrix:
    ## Put code for question 1 in this function
    ## print out matrix with newlines between rows
    ## print out elements in rows 1 space apart, with space between the format strings and the values
    ## use the getRandomValue helper function to generate random numbers from an input list


    def getRandomValue(self,values):
        return random.choice(values)


'''
PROBLEM 2
Assume all operators will be valid from the set: + - * / ^ ( )
    NOTE: Only 2c will use ()
Assume all inputs will be valid numbers, operators, or 'q'
Return answer as a decimal rounded to 1 place 
'''
def myCalculator2A():
    ## Put code for question 2a in this function

def myCalculator2B():
    ## Put code for question 2a in this function

def myCalculator2C():
    ## Put code for question 2a in this function
  
  
if __name__ == '__main__':

    # You may enter your own tests here
    # Nothing in the main function will interfere with grading
    m = myAwesomeMatrix()
    print(m)

    myCalculator2A()
    myCalculator2B()
    myCalculator2C()
