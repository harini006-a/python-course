n = int(input())

c = 0

if n == 0:
    c = 1
else:
    while n > 0:
        d = n % 10

        if d == 0:
            c += 1

        n //= 10

print(c)
