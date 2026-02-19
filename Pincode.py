# write a program to input an address containing a pincode and extract and print the pincode from the input address
print ("Enter an address containing a pincode : ")
add=input ("Enter text :")
i=0 
ln=len(add)
# for ch in add:
while i<ln:
    ch=add[i]
    if ch.isdigit():
        sub=add[i:(i+6)]
        if sub.isdigit():
            print(sub)
            break
    i+=1  
    # Example input : New Delhi, 110001
    # output : 110001   