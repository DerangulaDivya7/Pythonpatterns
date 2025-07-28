n = 5
for i in range(n):
  for k in range(i,n):
    print(' ',end=" ")
  for j in range(i):
        print("*",end=" ")
  print()
for i in range(n):
    for j in range(i):
        print(' ',end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()
