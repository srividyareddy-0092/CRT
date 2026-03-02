'''
Debugging in Python:
   bug is an error
   Finding and Fixing of Errors called Debugging

   Types of Errors:
     
     1)Syntax Errors-->Missing of colon, Missing of indentation
     2)Run-time Errors-->Any num is Divisible by Zero
     3)Logical Errors-->Missing of Logics


Debugging Techniques:
     1)print() -->Run the code line by line





a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
c= a+b
print("value of a is:", a)
print("value of b is:", b)
print("the sum is:", c)
'''

try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by zero")
except ValueError:
    print("Invalid imput.")