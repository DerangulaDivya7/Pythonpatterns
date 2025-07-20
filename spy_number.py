n = 123
m = n
sum = 0
prod = 1

while n != 0:
    d = n % 10
    sum = sum + d
    prod = prod * d
    n = n // 10  # ✅ Missing line to update n

if sum == prod:
    print("yes")
else:
    print("NO")
