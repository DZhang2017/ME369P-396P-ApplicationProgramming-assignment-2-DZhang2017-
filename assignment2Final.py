## Assignment2 ME369P/ME396P
## Name: <David Zhang>
## EID : <DZ4338>
## Section: <fill in the blank>

## Fill in the class and functions below. 
## Make sure your class runs with the tests in main
## You may use any imports, but do not use any import function for 
##      norm calculation or matrix operations. Be wary of numpy.

import random
import operator

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

    matrix = [[]]
    stringForm1 = ""
    stringForm2 = ""

    def __init__(self, **kwargs):
        vals = {'n': False,
                'i': False,
                'j': False,
                'range': False,
                'set': False,
                'style': 'random',
                'format1': "",
                'format2': ""}
        if len(kwargs) == 0:
            self.matrix = self.buildMatrix(vals.get('set'), 4, 4, vals.get('style'))
        else:
            vals.update(kwargs)
            self.stringForm1 = vals.get('format1')
            self.stringForm2 = vals.get('format2')
            if vals.get('n') is not False:
                if vals.get('range') is False:
                    if vals.get('set') is False:
                        self.matrix = self.buildMatrix([0,1], vals.get('n'), vals.get('n'), vals.get('style'))
                    else:
                        self.matrix = self.buildMatrix(vals.get('set'), vals.get('n'), vals.get('n'), vals.get('style'))
                else:
                    if vals.get('set') is False:
                        newSet = self.createSet(vals.get('range')[0], vals.get('range')[1])
                        self.matrix = self.buildMatrix(newSet, vals.get('n'), vals.get('n'), vals.get('style'))
                    else:
                        self.matrix = self.buildMatrix(vals.get('set'), vals.get('n'), vals.get('n'), vals.get('style'))
            else:
                if vals.get('range') is False:
                    if vals.get('set') is False:
                        self.matrix = self.buildMatrix([0,1], vals.get('i'), vals.get('j'), vals.get('style'))
                    else:
                        self.matrix = self.buildMatrix(vals.get('set'), vals.get('i'), vals.get('j'), vals.get('style'))
                else:
                    if vals.get('set') is False:
                        newSet = self.createSet(vals.get('range')[0], vals.get('range')[1])
                        self.matrix = self.buildMatrix(newSet, vals.get('i'), vals.get('j'), vals.get('style'))
                    else:
                        self.matrix = self.buildMatrix(vals.get('set'), vals.get('i'), vals.get('j'), vals.get('style'))

    def createSet(self, minNum, maxNum):
        res = []
        if maxNum < minNum:
            newMax = minNum
            minNum = maxNum
            maxNum = newMax
        for i in range(minNum, maxNum + 1):
            res.append(i)
        print(res)
        return res

    def buildMatrix(self, set, rows, cols, style):
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]  
        if style == 'random':
            for i in range(rows):
                for j in range(cols):
                    matrix[i][j] = self.getRandomValue(set)
        elif style == 'diagonal':
            for i in range(rows):
                for j in range(cols):
                    if i == j:
                        matrix[i][j] = self.getRandomValue(set)
                    else:
                        matrix[i][j] = 0
        elif style == 'upper':
            for i in range(rows):
                for j in range(cols):
                    if i <= j:
                        matrix[i][j] = self.getRandomValue(set)
                    else:
                        matrix[i][j] = 0
        elif style == 'lower':
            for i in range(rows):
                for j in range(cols):
                    if i >= j:
                        matrix[i][j] = self.getRandomValue(set)
                    else:
                        matrix[i][j] = 0
        else:
            for i in range(rows):
                for j in range(i, cols):
                    matrix[i][j] = self.getRandomValue(set)
                    matrix[j][i] = matrix[i][j]
        return matrix


    def getRandomValue(self,values):
        return random.choice(values)

    def __repr__(self):
        res = ""
        if len(self.stringForm1) == 0 and len(self.stringForm2) != 0 or len(self.stringForm1) != 0 and len(self.stringForm2) == 0:
            if len(self.stringForm1) == 0:
                self.stringForm1 = self.stringForm2[::-1]
            else:
                self.stringForm2 = self.stringForm1[::-1]
        for i in range(len(self.matrix)):
            res = res + self.stringForm1 + ' '
            for j in range(len(self.matrix[i])):
                if j == len(self.matrix[i]) - 1:
                    res = res + str(self.matrix[i][j]) + ' ' + self.stringForm2 +"\n"
                else:
                    res = res + str(self.matrix[i][j]) + " "
        return res


'''
PROBLEM 2
Assume all operators will be valid from the set: + - * / ^ ( )
    NOTE: Only 2c will use ()
Assume all inputs will be valid numbers, operators, or 'q'
Return answer as a decimal rounded to 1 place 
'''
def myCalculator2A():
    ## Put code for question 2a in this function
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '^' : operator.pow,
    }
    while True:
        Expression = input("Enter expression: ")
        if Expression == 'q':
            break
        Expression = Expression.split()
        num1 = float(Expression[0])
        num2 = float(Expression[2])
        operation = Expression[1]
        res = ops[operation](num1, num2)
        ans = round(res, 1)
        print(ans)



def myCalculator2B():
    ## Put code for question 2a in this function
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '^' : operator.pow,
    }
    while True:
        Expression = input("Enter expression: ")
        if Expression == 'q':
            break
        Expression = Expression.split()
        res = float(Expression[0])
        for i in range(1, len(Expression) - 1, 2):
            num1 = res
            num2 = float(Expression[i + 1])
            operation = Expression[i]
            res = ops[operation](num1, num2)
        ans = round(res, 1)
        print(ans)

def myCalculator2C():
    ## Put code for question 2a in this function
    while True:
        Expression = input("Enter expression: ")
        if Expression == 'q':
            break
        else: 
            if ') (' in Expression:
                Expression = Expression.replace(') (', ') * (')
            if '^' in Expression:
                Expression = Expression.replace('^', '**')
            ans = eval(Expression)
            ans = round(ans, 1)
        print(ans)
                         

  
if __name__ == '__main__':

    # You may enter your own tests here
    # Nothing in the main function will interfere with grading
    #m = myAwesomeMatrix()
    #print(m)

    #myCalculator2A()
    myCalculator2B()
    #myCalculator2C()
