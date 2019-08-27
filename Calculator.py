# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:20:54 2019

@author: akuma222

BASIC CALCULATOR
"""
result=''

def display():
    print("."*25)
    print ("!RESULT="+" "*16+"!")
    print ("!"+result+" "*(23-len(result))+"!")
    print("."*25)
    print("|1   |2   |3   |4   |5  |")
    print("."*25)
    print("|6   |7   |8   |9   |0  |")
    print("."*25)
    print("|plus|minus|divide|multi|")
    print("."*25)
    print("|mod|power              |")
    print("."*25)
    
def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def divide(num1,num2):
    return num1/num2

def multi(num1,num2):
    return num1*num2

def mod(num1,num2):
    return num1%num2

def power(num1,num2):
    return num1**num2

oplist=['plus','minus','divide','multi','mod','power']
execute = {'plus':plus,'minus':minus,'divide':divide,'multi':multi,'mod':mod,'power':power}  
display()
while (True):

    try:
        num1=int(input("please enter the first number:"))
        num2=int(input("please enter the second number:"))    
        op = input("please enter the operation to perform:")
        
    except:
        print("please enter an integer/valid number:")
    else:
        if op in oplist:
            result=str(execute[op](num1,num2))
            display()
            break
        else:
            print("Enter a valid operation from the calculator")
            continue
        
            
    
    