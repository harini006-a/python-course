n=int(input())
array=list(map(int,input().split()))
key=int(input())
for i in range(n):
  if array[i] == key:
    print(i)
    break
else:
  print(-1)
