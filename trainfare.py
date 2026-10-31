age=int(input())
dist=int(input())
fare = dist * 5
if age < 12:
  fare = fare * 0.5
elif age <= 59:
  fare = fare
else:
  fare = fare * 0.75
print(int(fare))
