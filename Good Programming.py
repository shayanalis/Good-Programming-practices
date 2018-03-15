############### SOME GOOD PRACTICES IN PYTHON ###############
#helpful for HAckerRank , CodeJam , Hacker Earth





############### RECURSIVE CODE

# guide to recursive problems and solutions for them
# print 123....N
# ref: https://www.hackerrank.com/challenges/python-print/problem
from __future__ import print_function
# if __name__ == '__main__':
#     n = int(raw_input())
# Editorial methods
def plus1(x):
	return(x+1)

# print (*map(plus1 ,range(n)),sep='');

# # Editorial method 2
# print (*range (1, n + 1), sep='')

def getpts(key):
    if (key==0):
        return
    else:
         return 10

points = getpts(1) or 0 


#my method
def digits(n):
    if (int(n/10) == 0):
        return 1
    else:
        return 1 + digits(n/10)
    
def expand(n):
    if(n==1):
        return n
    else:
        return (n + expand(n-1)*10**(digits(n)))



# Factorial

def Factorial(n):
	if(n<2):
		return 1
	else:
		return n*Factorial(n-1)


############### Function parameters

def TotalScore(Sixes , fours , isOut , Noballs=0 ):
    if (isOut):return 0
    return sum([Sixes,fours,Noballs])

# print( TotalScore(1,4,False) )


# print(TotalScore(
#         Sixes=1,
#         fours=4,
#         isOut=False)
# )

############### MAP FILTER REDUCE LAMBDAS

listOfInts = [1,2,3,4,5,6]
listOfStrings = ['hello','how','are','you','buddy?']
print ( filter(lambda x: x%2==0,listOfInts) )

print( map(lambda x: x**2 , listOfInts) )

print(map(lambda x: x.upper()  , listOfStrings))

print (
    reduce(lambda x,y : (x+y) , listOfInts)
    )

print (
    reduce(lambda x,y : (x+' '+y) , listOfStrings)
    )


############### LIST COMPREHENSIONS

ListOfCubes = [x**3 for x in range(1,6) if(x%2 == 0)]
# print (ListOfCubes)

#make subsets of a set
SetOfChars = 'halo'
SubsetsOfChars = [(x,y) for x in SetOfChars for y in SetOfChars if(x!=y)]
# print(SubsetsOfChars)


def RemoveRepetitions(inp):
    elements = ''
    listWithOutrepts=''
    for char in inp:
        if(char not in elements):
            listWithOutrepts+=(char)
            elements+=(char)

    return listWOrepts

# inp = 'aacnsifnsccsaesdcv'
# print(inp)
# print(RemoveRepetitions(inp))


############### Tower of hanoi problem

def SolveTowerOfHanoi(n):
    # some data structure needed to represent tower
    T1 = [range(n,1)]
    T2 = []
    T3 = []

def RecSolveTowerOfHanoi(T1,T2,T3):
    if (T3 == [range(n,1)] and T1==[] and T2==[]):
        return 
    
def pushInTower(list,elem):
    if(elem < list[-1]):
        list.append(elem)
        return list
    else:
        return None

def PopTower(list):
    if(len(list) <1): return None
    return list[0:-1], list[-1]


def moveStackToT3(T1,T2,T3):
    moveDisc(T1,T2)
    moveDisc(T1,T3)
    

def moveDisc(T1,T2):
    T1,elem = PopTower(T1)
    pushInTower(T2,elem)


# READ INPUT 
# 4
# 3 2 1 3

# queries = int(raw_input().strip())
# ar = map(int, raw_input().strip().split(' '))

# queries = int(raw_input().strip())
# for i in range(queries):
#     L,R,K = map(int, raw_input().strip().split(' '))
#     print L,R,K


# for index,value in enumerate(mylist):
    #use both index and value inside the loop


def solve(caseNo):
    if (caseNo == 2):
        throw('ValueError')
    return '5 5'
############### read Write file AND TEST CASE DRIVEN PROGRAMMING

with open("testresults.txt",'r') as TestResultsFile:
    TestResults = TestResultsFile.readlines()

    for caseNo , groundTruth in enumerate(TestResults):
        groundTruth = groundTruth.strip()
        if((solve(caseNo) or 'Impossible') == groundTruth):
            print 'Testcase #{}  passed'.format(caseNo+1)
        else:
            print '\n****Testcase#{} failed***'.format(caseNo+1)
            print 'Expected: {}'.format(groundTruth)
            print 'Actual: {}\n'.format(solve(caseNo))
            catch:
                print 'a'

def ResolveQuery(Query):
    return 'result'


#Resolves 1 Query only: nice readable code
with open('Testcases.txt') as TestCases:
    NumInputs = int(TestCases.readline())
    arr,Array = [],[]
    for i in range(NumInputs):
        arr = map(int, TestCases.readline().strip().split(' '))
        Array.append(arr)
    Query = map(int,TestCases.readline().strip().split(' '))

with open("testresults.txt",'r') as TestResults:
    groundTruth = TestResults.readline()
    if((ResolveQuery(Query) or 'Impossible') == groundTruth):
        print '#1 test case passed'
    else:
        print 'test case failed'
