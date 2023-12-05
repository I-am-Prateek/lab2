#Code by Pratik Shrestha(23026137)
#Python program using nested for loop to print the (*) pattern
for i in range(2, 9):
    # Loop through columns
    for j in range(1, 9):
        # Printing Pattern
        if (i == j) or (j == 1):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
