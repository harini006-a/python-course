n = int(input())

temp = n
s = 0

while n > 0:
    d = n % 10
    fact = 1

    for i in range(1, d + 1):
        fact *= i

    s += fact
    n //= 10

if temp == s:
    print("Strong")
else:
    print("Not Strong")
