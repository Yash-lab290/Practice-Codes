# Program to find frequencies of all elements of a list. Also print the list of unique elements in the list and Duplicate elements in the given list.
lst= eval(input("Enter list : "))
length = len(lst)
uniq = []    #list to hold Unique elements
dupl = []    #list to hold duplicate elements
count =i= 0
while i < length :
    element = lst[i]
    count = 1   # Count as 1 for the element at lst[i]
    if element not in uniq and element  not in dupl:
        i += 1
        for j in range(i, length):
            if element == lst[j]:
                count += 1
        else:    # when inner loop - for loop ends
            print("Element", element, "frequency:",count)
            if count == 1 :
                uniq.append(element)
            else:
                dupl.append(element)
    else:
        i += 1  # when element is not found in uniq or lists
print("Original list", lst)
print("Unique elements list", uniq)
print("Duplicate elements list", dupl)
