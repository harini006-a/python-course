n = int(input())

temp = n
digits = len(str(n))
s = 0

while n > 0:
    d = n % 10
    s += d ** digits
    n //= 10

if temp == s:
    print("Armstrong")
else:
    print("Not Armstrong")
