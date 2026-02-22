#Write a program to check if a given number is an Armstrong number or not.
# (Note : if a 3 digit number is equal to the sum of the cubes of its each digit, then it is an Armstrong Number)
num = int(input("Enter a 3 digit number: "))
sum = 0
temp = num 
while(temp>0):
    digit = temp%10
    sum += digit ** 3
    temp //= 10
if(num == sum):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")