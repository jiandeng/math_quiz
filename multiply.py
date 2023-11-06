#!- encoding = utf-8 -!

'''
Author: Dou Liyou
Program Time: 2017-07-14
Version: 1.0

Script using:
'''

import random
import operatePdf

'''
define a method called 'calculate' with 3 parameters: number1, number2 and expression.
the method calculate depend on the expression, this version only support '*' , '/'
other expression will return None
'''

def calculate(Operator,number1,number2):
    if Operator == '×':
        return number1 * number2
    if Operator == '/':
        return number1 / number2
    return -1


def cal(exp):
    if exp.__len__() == 3:
        return calculate(exp[0],exp[1],exp[2])

'''
this method is used to produce a random int which is between 'begin' and 'end'.

'''
def makeRandomInt(begin,end):
    if begin <= end:
        return random.randint(begin,end)
    else:
        return random.randint(end,begin)


'''
this method is used to produce a operator optionally. which should be '*' or '/'
'''
def makeRandomOper():
    exp = ['×', '/']
    index = random.randint(0,1)
    return exp[index]


'''
this method can produce a list which contains one operator and two numbers.

'''
def generateExpression():
    exp = []
    exp.append('×')
    exp.append(makeRandomInt(2, 10))
    exp.append(makeRandomInt(3, 12))
    return exp


'''
this method format a expression to style which can be read by a pupil
'''
def formatExpression(exp, pos):
    result = cal(exp)
    if exp.__len__() == 3:
        if pos == 3 and (result not in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 50, 54, 56, 60, 63, 64, 70, 72, 80, 81, 90, 100]):
            pos = makeRandomInt(0, 2)
        if pos == 0:
            return ("{}{}{}=(      )".format(exp[1], exp[0], exp[2]), result)
        elif pos == 1:
            return ("(    ){}{}={}".format(exp[0], exp[2], result), exp[1])
        elif pos == 2:
            return ("{}{}(    )={}".format(exp[1], exp[0], result), exp[2])
        elif pos == 3 and result in [12, 16, 18, 20, 24, 30, 36, 40]:
            return ("{}=(    ){}(    )=(    ){}(    )".format(result, exp[0],exp[0]), (exp[1], exp[2]))
        else:
            return ("{}=(    ){}(    )".format(result, exp[0]), (exp[1], exp[2]))


'''
this method produce a quiz and return quiz as a list.
e.g: [[exp1,exp2,exp3],[res1,res2,res3]]
'''
def generateQuiz(amout):
    quiz = []
    expression = []
    results = []
    quiz.append(expression)
    quiz.append(results)
    for i in range(amout):
# use this variable r to control 2 or 3 expression
#        r = random.randint(0,1)
        exp = generateExpression()
        rnd = makeRandomInt(1, 100)
        pos = 0 if rnd < 20 else 1 if rnd < 40 else 2 if rnd < 60 else 3
        if max(exp[1], exp[2]) > 10:
            pos = 0
        fexp = formatExpression(exp, pos)
        expression.append(fexp[0])
        results.append(fexp[1])
    return quiz

'''
this method produce the number which is useful in the expression,
e.g: give a 45 , then need a number which caculate with given one with add or minus, must not over 10
     1,2,3,4 ; 11,12,13,14 ; 21,22,23,24, 31,32,33,34; 41,42,43,44; 51,52,53,54;
'''
def produceNum(givenNum,Oper,max):
    nMax = max-givenNum
    if Oper=='+':
        nList=list(str(nMax))
        length = len(nList)
        if length == 1:
            return makeRandomInt(0,nMax)
        elif length > 1:
            m=0
            for n in nList:
                m = m*10+makeRandomInt(0,int(n))
            return m
    if Oper=='-':
        nList=list(str(givenNum))
        nLength = len(nList)
        mList=list(str(max))
        mLength = len(mList)
        if nLength == mLength:
#            print('exec this line nLength == mLength')
            m=0
            c=0
            for n in nList:
                m = m*10 + makeRandomInt(int(n),int(mList[c]))

                c+=1
            return m
        elif nLength < mLength:
#            print('exec this line nLength < mLength')
            c=nLength-mLength
            n=0
            for m in mList:
                if c<0:
                    n = n*10 + makeRandomInt(0,int(m))
                    c+=1
                else:
                    n = n*10 +makeRandomInt(int(nList[c]),int(m))
                    c+=1
            return n
    return 0
if __name__=="__main__":
    #  print('auto generate quiz starts ...')
    #  print(makeRandomOper())
    #  exptmp = generateExpression()
    #  result = cal(exptmp)
    #  print(exptmp)
    #  print(formatExpression(exptmp, 0))
    #  print(formatExpression(exptmp, 1))
    #  print(formatExpression(exptmp, 2))
    #  print(formatExpression(exptmp, 3))

#####generate 2 number expression.
    number_quizes = 50
    file_name = 'quiz-multiply.pdf'

    myQuiz = generateQuiz(number_quizes)
    operatePdf.write(myQuiz[0], myQuiz[1], file_name)
    print('{} generated!'.format(file_name))
