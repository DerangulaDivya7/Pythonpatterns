n = 5
for i in range(n - 1):

    for k in range(i):
        print("*", end=" ")
    print()
for i in range(n):

    for k in range(i, n - 1):
        print("*", end=" ")

    print()


