n=int(input())
arr=list(map(int,input().split()))
oddsum=evensum=0
for i in arr:
  if i % 2 == 0:
    evensum += i
  else:
    oddsum += i
diff=oddsum - evensum
print(diff)
