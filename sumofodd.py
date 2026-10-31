n=int(input())
b=list(map(int,input().split()))
evensum=oddsum=0

for i in b:
    if i% 2== 0:
       evensum+=i
    else:
       oddsum+=i
print(evensum,end=" ")
print(oddsum,end=" ")
  
