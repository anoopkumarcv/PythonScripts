# -*- coding: utf-8 -*-
"""
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

"""

def Fibonacci (num):
    num1=0
    num2=1
    for num in range(0,num):
        yield num1
        num1,num2=num2,num2+num1

while(True):        
    try:
        num=int(input ("Please enter a number till where to generate Fibonacci sequence:"))
    except:
        print("You have not entered an integer")
    else:
        print("Fibonacci sequence")    
        for i in Fibonacci(num):
            print (i)
        break
    

