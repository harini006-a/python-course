n=int(input())
arr=list(map(int,input().split()))
even=[]
odd=[]
for i in arr:
  if i % 2 == 0:
     even.append(i)
  else:
     odd.append(i)
if len(even) != 0:
  print(max(even))
else:
  print("None")
if len(odd) != 0:
  print(max(odd))
else:
  print("None")
    
