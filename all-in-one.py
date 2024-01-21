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
    if Operator == '÷':
        return number1 // number2
    if Operator.endswith('-'):
        return number1 - number2
    if Operator.endswith('+'):
        return number1 + number2
    return -1


def cal(exp):
    if exp.__len__() == 3:
        return calculate(exp[0],exp[1],exp[2])
    if exp.__len__() == 5:
        tmpValue = calculate(exp[0],exp[2],exp[3])
        return calculate(exp[1],tmpValue,exp[4])

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
    exp = ['×', '÷']
    index = random.randint(0,2)
    return exp[index]

def generateHundredExp():
    # Generate the operands
    operand = []
    for _ in range(2):
        operand.append(random.randint(100, 999))

    # Generate the operations
    operator = []
    operator.append(random.choice(['+', '-']))

    # Switch operands if necessary
    if operator[0] == '-':
        if operand[0] < operand[1]:
            operand[0], operand[1] = operand[1], operand[0]

    # Create the expression
    exp = []
    exp.extend(operator)
    exp.extend(operand)

    return exp

def generateThreeExp():
    # Generate the operands
    operand = []
    for _ in range(3):
        operand.append(random.randint(10, 99))

    # Generate the operations
    operator = []
    for _ in range(2):
        operator.append(random.choice(['+', '-']))

    # If both operations are subtraction, put the maximum number at the beginning of the list
    result = 0
    if operator[0] == '-' and operator[1] == '-':
        max_num_idx = operand.index(max(operand))
        operand[0], operand[max_num_idx] = operand[max_num_idx], operand[0]
        result = operand[0] - operand[1] - operand[2]
        if result < 0:
            operand[2] = random.randint(0, operand[2] + result)
        result = operand[0] - operand[1] - operand[2]
        if operand[0] % 10 > operand[1] % 10 or operand[0] - operand[1] < 11:
            if makeRandomInt(0, 100) < 80:
                return generateThreeExp()
    elif operator[0] == '-' and operator[1] == '+':
        min_num_idx = operand.index(min(operand))
        operand[1], operand[min_num_idx] = operand[min_num_idx], operand[1]
        if operand[0] % 10 > operand[1] % 10 or operand[0] - operand[1] < 11:
            if makeRandomInt(0, 100) < 80:
                return generateThreeExp()
        result = operand[0] - operand[1] + operand[2]
    elif operator[0] == '+' and operator[1] == '-':
        min_num_idx = operand.index(min(operand))
        operand[2], operand[min_num_idx] = operand[min_num_idx], operand[2]
        if operand[0] + operand[1] > 100:
            return generateThreeExp()
        if operand[0] % 10 + operand[1] % 10 < 10:
            if makeRandomInt(0, 100) < 80:
                return generateThreeExp()
        result = operand[0] + operand[1] - operand[2]
    elif operator[0] == '+' and operator[1] == '+':
        if operand[0] + operand[1] > 100:
            return generateThreeExp()
        if operand[0] % 10 + operand[1] % 10 < 10:
            if makeRandomInt(0, 100) < 80:
                return generateThreeExp()
        result = operand[0] + operand[1] + operand[2]

    if result >= 160 or min(operand[2:5]) < 10 or max(operand[2:5]) < 20:
        return generateThreeExp()

    # Create the expression
    exp = []
    exp.extend(operator)
    exp.extend(operand)

    return exp


'''
this method can produce a list which contains one operator and two numbers.

'''
def generateMultiplyExp():
    exp = []
    exp.append('×')
    exp.append(makeRandomInt(2, 10))
    exp.append(makeRandomInt(3, 25))
    if exp[2] > 11:
        rnd = random.randint(0, 100)
        if rnd >= 10:
            return generateMultiplyExp()
    return exp

'''
this method can produce a list which contains one operator and two numbers.

'''
def generateMoneyExp():
    exp = []
    ops = '$' + random.choice(('+', '+', '-', '-', '='))
    exp.append(ops)
    exp.append(makeRandomInt(10, 200))
    exp.append(makeRandomInt(10, 100))
    if ops == '$-' and exp[1] < exp[2]:
        exp[1], exp[2] = exp[2], exp[1]
    if ops == '$+':
        if exp[1] % 10 + exp[2] % 10 < 10:
            if random.randint(1, 100) > 10:
                return generateMoneyExp()
    if ops == '$-':
        if exp[1] % 10 > exp[2] % 10:
            if random.randint(1, 100) > 10:
                return generateMoneyExp()
    return exp

'''
this method can produce a list which contains one operator and two numbers.

'''
def generateLengthExp():
    exp = []
    ops = 'm' + random.choice(('+', '+', '-', '-', '='))
    exp.append(ops)
    exp.append(makeRandomInt(10, 200))
    exp.append(makeRandomInt(10, 100))
    if ops == 'm-' and exp[1] < exp[2]:
        exp[1], exp[2] = exp[2], exp[1]
    if ops == 'm+':
        if exp[1] % 10 + exp[2] % 10 < 10:
            if random.randint(1, 100) > 10:
                return generateLengthExp()
    if ops == 'm-':
        if exp[1] % 10 > exp[2] % 10:
            if random.randint(1, 100) > 10:
                return generateLengthExp()
    if ops == 'm=':
        exp[1] = random.randint(10, 99)
    return exp


'''
this method can produce a list which contains one operator and two numbers.

'''
def generateDivisionExp():
    exp = []
    exp.append('÷')
    o1 = makeRandomInt(2, 11)
    o2 = makeRandomInt(3, 10)
    exp.append(o1 * o2)
    exp.append(o1)
    return exp

def generateExpression(ops):
    if ops == '÷':
        return generateDivisionExp()
    elif ops == '×':
        return generateMultiplyExp()
    elif ops == '|':
        return generateThreeExp()
    elif ops.startswith('$'):
        return generateMoneyExp()
    elif ops.startswith('m'):
        return generateLengthExp()
    elif ops.startswith('h'):
        return generateHundredExp()
    else:
        return None


def formatNormalExp(exp, pos):
    result = cal(exp)
    if len(exp) == 3:
        if exp[0] == '÷' and pos >= 3:
            pos = makeRandomInt(0, 2)
        if pos == 3 and (result not in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 50, 54, 56, 60, 63, 64, 70, 72, 80, 81, 90, 100]):
            pos = makeRandomInt(0, 2)
        if pos == 0:
            return ("{}{}{}=(   )".format(exp[1], exp[0], exp[2]), result)
        elif pos == 1:
            return ("(   ){}{}={}".format(exp[0], exp[2], result), exp[1])
        elif pos == 2:
            return ("{}{}(   )={}".format(exp[1], exp[0], result), exp[2])
        elif pos == 3 and result in [12, 16, 18, 20, 24, 30, 36, 40]:
            return ("{}=(   ){}(   )=(   ){}(   )".format(result, exp[0],exp[0]), (exp[1], exp[2]))
        else:
            return ("{}=(   ){}(   )".format(result, exp[0]), (exp[1], exp[2]))

def formatAddSubExp(exp, pos):
    result = cal(exp)
    if len(exp) == 5:
        if exp[0] != exp[1] and pos != 0:
            pos = random.choice((0, 3))
            print(exp, pos)
        if pos == 0:
            return ("{}{}{}{}{}=(   )".format(exp[2], exp[0], exp[3], exp[1], exp[4]), result)
        elif pos == 1:
            return ("(   ){}{}{}{}={}".format(exp[0], exp[3], exp[1], exp[4], result), exp[2])
        elif pos == 2:
            return ("{}{}(   ){}{}={}".format(exp[2], exp[0], exp[1], exp[4], result), exp[3])
        elif pos == 3:
            return ("{}{}{}{}(   )={}".format(exp[2], exp[0], exp[3], exp[1], result), exp[4])

def _money_str(m):
    y = m // 10
    j = m % 10
    if y == 0 and j == 0:
        return '0元'
    elif y == 0:
        return '{}角'.format(j)
    elif j == 0:
        return '{}元'.format(y)
    else:
        return '{}元{}角'.format(y, j)

def formatMoneyExp(exp, pos):
    result = cal(exp)
    if len(exp) == 3:
        if exp[0] == '$=':
            if pos == 1:
                return ("{}角=(   )元(   )角".format(exp[1]), _money_str(exp[1]))
            else:
                return ("{}=(   )角".format(_money_str(exp[1])), exp[1])
        else:
            if pos == 0:
                return ("{}{}{}=(   )元(   )角".format(_money_str(exp[1]), exp[0][1], _money_str(exp[2])), _money_str(result))
            elif pos == 1:
                return ("(   )元(   )角{}{}={}".format(_money_str(exp[0][1], _money_str(exp[2]), _money_str(result))), _money_str(exp[1]))
            elif pos == 2:
                return ("{}{}(   )元(   )角={}".format(_money_str(exp[1]), exp[0][1], _money_str(result)), _money_str(exp[2]))

def _length_str(l):
    m = l // 10
    c = l % 10 * 10
    if m == 0 and c == 0:
        return '0m'
    elif m == 0:
        return '{}cm'.format(c)
    elif c == 0:
        return '{}m'.format(m)
    else:
        return '{}m{}cm'.format(m, c)

def formatLengthExp(exp, pos):
    result = cal(exp)
    if len(exp) == 3:
        if exp[0] == 'm=':
            if pos == 1:
                return ("{}cm=(   )m(   )cm".format(exp[1] * 10), _length_str(exp[1]))
            else:
                return ("{}=(   )cm".format(_length_str(exp[1])), exp[1])
        else:
            if pos == 0:
                return ("{}{}{}=(   )m(   )cm".format(_length_str(exp[1]), exp[0][1], _length_str(exp[2])), _length_str(result))
            if pos == 1:
                return ("(   )m(   )cm{}{}={}".format(_length_str(exp[0][1], _length_str(exp[2]), _length_str(result))), _length_str(exp[1]))
            if pos == 2:
                return ("{}{}(   )m(   )cm={}".format(_length_str(exp[1]), exp[0][1], _length_str(result)), _length_str(exp[2]))

'''
this method format a expression to style which can be read by a pupil
'''
def formatExpression(exp, pos):
    if len(exp) == 5:
        return formatAddSubExp(exp, pos)
    elif exp[0].startswith('$'):
        return formatMoneyExp(exp, pos)
    elif exp[0].startswith('m'):
        return formatLengthExp(exp, pos)
    else:
        return formatNormalExp(exp, pos)


'''
this method produce a quiz and return quiz as a list.
e.g: [[exp1,exp2,exp3],[res1,res2,res3]]
'''
def generateQuiz(amount):
    quiz = []
    expression = []
    results = []
    quiz.append(expression)
    quiz.append(results)
    while len(expression) < amount:
# use this variable r to control 2 or 3 expression
        rnd = makeRandomInt(1, 100)
        ops = '|' if rnd < 30 else '÷' if rnd < 45 else '×' if rnd < 60 else '$' if rnd < 75 else 'm' if rnd < 90 else 'h'
        exp = generateExpression(ops)
        rnd = makeRandomInt(1, 100)
        if exp[0] == '×':
            pos = 0 if rnd < 20 else 1 if rnd < 40 else 2 if rnd < 60 else 3
            if max(exp[1], exp[2]) > 11:
                pos = 0
        elif exp[0] == '÷':
            #  pos = 0 if rnd < 60 else 1 if rnd < 70 else 2
            pos = random.choice([0, 0, 1, 2, 2])
        elif exp[0].endswith('='):
            pos = random.choice([0, 1])
        else:
            pos = 0

        fexp = formatExpression(exp, pos)
        if not fexp[0] in expression:
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
    file_name = 'quiz-all-in-one.pdf'

    myQuiz = generateQuiz(number_quizes)
    operatePdf.set_margin(50, 10)
    operatePdf.set_layout(columns_per_line=3, height_of_row=40)
    operatePdf.write(myQuiz[0], myQuiz[1], file_name)
    print('{} generated!'.format(file_name))
