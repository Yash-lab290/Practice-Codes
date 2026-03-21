age= int(input(" Enter your current age : \n"))
year_left=(90-(age))
days=year_left * 365
weeks=year_left * 52
months=year_left * 12
print(f"you have left {days} days, or {weeks} weeks or {months} months only ")

# NEW PROGRAMM
height=int(input("enter height in feet :"))
if(height>=3):
 print("buy token")
else:
    print("no token required")