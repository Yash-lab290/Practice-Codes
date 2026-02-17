# Write a program to check if a given number is a palindrome number or not.
# (A palindrom number's reversed number is a same as the number )
num = int(input("Enter a number:"))
wnum = num # working number stores num initially 
rev = 0
while(wnum>0):
    dig = wnum % 10
    rev = rev*10 + dig 
    wnum = wnum // 10
if(num == rev):
    print("Number",num ,"is a palindrome!!")
else:
    print("Number", num ," is not a palindrome!!")
