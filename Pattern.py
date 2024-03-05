row = int(input("Enter how many rows you want to print"))

# Outer loop for printing rows
for i in range(1, row+1):

    # loop for printing spaces
    for j in range(1, row-i+1):
        print(" ", end="")

    # loop for printing stars   
    for k in range(1, i+1):
        print("*", end=" ")

    print()