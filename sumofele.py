n=int(input())
b=list(map(int,input().split()))
evensum=oddsum=0
for i in range(len(b)):
  if i % 2 == 0:
    evensum+=b[i] 
  else:
    oddsum+=b[i]
print(evensum,end=" ")
print(oddsum,end=" ")
    
