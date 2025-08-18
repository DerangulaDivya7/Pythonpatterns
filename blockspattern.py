Block=int(input("enter no of blocks"))
Line=int(input("enter no of Lines"))
Star=int(input("enter no of Stars"))
for i in range(Block):
    count=0
    for j in range(Line-i):
        for k in range(Star):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    print("____________")
