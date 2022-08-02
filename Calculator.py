import cmath
import math
import sys
import os
from cmath import *
from xml.dom.pulldom import IGNORABLE_WHITESPACE

#f  =open ("Log.txt", "a")
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

print("Welcome to the calculator!")
print("These are the available operations:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")
print("5. Exponentiation(^)")
print("6. Square Root(sqrt)")
print("7. Logarithm(log)")
print("8. Sinus(sin) [degrees]")
print("9. Cosinus(cos) [degrees]")
print("10. Tangens(tan) [degrees]")
print("^-1 is the inverse of the function or number")
print("^2 is the square of the number")
print("^3 is the cube of the number")
print("^4 is the fourth power of the number")
number1 = input("Type out your first number: ")
try:
    number1 = float(number1)
except ValueError:
    print("You have to type a number!")
    sys.exit()
operator1 = input("Type out your operator: ")
    #operator1 == '+' or '-' or '*' or '/' or '^' or 'sqrt' or 'log' or 'sin' or 'cos' or 'tan' or ('tan^-1') or ('cos^-1') or ('sin^-1')
ch = ['+' , '-' , '*' , '/' , '^' , 'sqrt' , 'log' , 'sin' , 'cos' , 'tan' , 'tan^-1' ,'cos^-1' ,'sin^-1']
ch_trig = ['sin' , 'cos' , 'tan' , 'tan^-1' ,'cos^-1' ,'sin^-1' 'sqrt' , 'log' ,'^']
if operator1 in ch:
    pass

else:
    print("You have to type an operator!")
    sys.exit()
if operator1 in ch_trig:
    pass
else:
    number2 = input("Type out your second number: ")
    try:
        number2 = float(number2)
    except ValueError:
        print("You have to type a number!")
        sys.exit()

    

if operator1 == '+':
    answer = number1 + number2
    print("The answer is: " + str(answer))
    with open('Log.txt', 'a') as f:
        f.writelines(str(number1)  + str(operator1) + str(number2) + '=' + str(answer) + '\n')
elif operator1 == '-':
    answer = number1 - number2
    print(answer)
    with open('Log.txt', 'a') as f:
        f.write(str(number1) + str(operator1) + str(number2) + '=' + str(answer) + '\n')
elif operator1 == '*':
    answer = number1 * number2
    print(answer)
    with open('Log.txt', 'a') as f:
        f.write(str(number1) + str(operator1) + str(number2) + '=' + str(answer)+ '\n')
elif operator1 == '/':
    answer = number1 / number2
    print(answer)
    with open('Log.txt', 'a') as f:
        f.write(str(number1) + str(operator1) + str(number2) + '=' + str(answer)+ '\n')
elif operator1 == '^':
    answer = number1 ** number2
    print(answer)
    with open('Log.txt', 'a') as f:
        f.write(str(number1) + str(operator1) + str(number2) + '=' + str(answer)+ '\n')
elif operator1 == 'sqrt':
    answer = cmath.sqrt(number1)
    print(answer)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answer)+ '\n')
elif operator1 == 'log':
    answer = cmath.log(number1)
    print(answer)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answer)+ '\n')
elif operator1 == 'sin':
    answer = cmath.sin(number1)
    answerln =  answer * (180/pi) #converts radians to degrees
    print(answerln) #prints answer in degrees
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answerln)+ '\n')
elif operator1 == 'cos':
    answer = cmath.cos(number1)
    answerln =  answer * (180/pi) #converts radians to degrees
    print(answerln)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answerln)+ '\n')
elif operator1 == 'tan':
    answer = cmath.tan(number1)
    answerln =  answer * (180/pi) #converts radians to degrees
    print(answerln)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answerln)+ '\n')
elif operator1 == 'sin^-1':
    number1degrees = number1 * (180/pi) #converts radians to degrees
    answer= cmath.asin(number1degrees)
    answerln =  answer
    print(answerln)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answerln)+ '\n')
elif operator1 == 'cos^-1':
    number1degrees = number1 * (180/pi)
    answer = cmath.acos(number1degrees)
    answerln =  answer
    print(answerln)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answerln)+  '\n')
elif operator1 == 'tan^-1':
    number1degrees = number1 * (180/pi)
    answer  = cmath.atan(number1degrees)
    answerln =  answer
    print(answerln)
    with open('Log.txt', 'a') as f:
        f.write(str(operator1) + '(' + str(number1) + ')' '=' + str(answerln)+ '\n')        
f.close()

    


