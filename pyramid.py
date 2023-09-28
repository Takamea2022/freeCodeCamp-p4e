# n = int(input("Enter the number of rows in the pyramid "))

# for i in range(1, n + 1) :
#   #Print spaces before the asterisks in each row
#   for j in range(n - 1) :
#     print(" ", end=" ")

#   #print asterisks for the current row
#   for k in range(i) :
#     print("*", end= " ")
  
#   #Move to the next line after printing each row
#   print()

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print("  ", end=" ")
    
    k = 0
    while k != 2 * i - 1:
        print("* ", end=" ")
        k += 1
    
    print()