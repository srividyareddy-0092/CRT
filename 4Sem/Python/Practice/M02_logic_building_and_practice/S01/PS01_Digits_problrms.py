'''
sample input : 1234
sample output : 4

sample input : 12236
sample output : 5

num = int(input("Enter a number: "))
if num == 0:
    num_digit = 1
else:
    num_digit = 0
    while num > 0:
        num = num//10
        num_digit += 1
print("Number of digits:", num_digit)

n=int(input())
count=0
while n>0:
    count += 1
    n=n//10
print(count)

'''
"""
sample input : 1234
sample output : 10

sample input : 12236
sample output : 14

n = int(input())
s = 0
while n > 0:
    s += (n%10)
    n=n//10
print(s)


n=int(input())
while n>0:
    digit = n%10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n//10
"""
def reverse(num):
    rev = 0
    while num>0:
        rev=(rev*10)+(num%10)
        num = num//10
    return rev
n=reverse(int(input()))
while n>0:
    digit=n%10
    if digit%2==0:
        print(digit,end=" ")
    n=n//10