n = int(input("Enter Hollow Right Triangle Pattern Rows = "))
print("Hollow Right Triangle Star Pattern") 
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1 or i == n or j == 1 or j == i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
