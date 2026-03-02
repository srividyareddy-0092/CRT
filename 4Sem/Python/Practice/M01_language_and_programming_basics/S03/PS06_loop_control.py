'''
Docstring for 4Sem.Python.Practice.M01.S03.PS06_loop_control,py
for i in range(1, 11):
    
    if i == 5:
        continue
    print(i,end=" ")
else:
    print("Loop completed")
'''
'''
password retry system (max 3 attempts) 
if password is coorect show login successful 
else ask for password 3 times.
once attemptd exceed show account locked.'''

p1= "abcd123"
for i in range(3):
    p2= input()
    if p1 == p2:
        print("Login successful")
        break 
else:
    print("Account locked")
