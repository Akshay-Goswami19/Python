num = int(input("Enter the number to find factorial"))

i = 1
factorial = 1

#loop for finding factorial
while i<=num:
    factorial = factorial*i
    i+= 1

#printing the final answer
print(factorial) 