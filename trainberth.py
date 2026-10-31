a=int(input())
if a % 8 == 1 or a % 8 == 4:
  print("LB")
elif a % 8 == 2 or a % 8 == 5:
  print("MB")
elif a % 8 == 3 or a % 8 == 6:
  print("UB")
elif a % 8 == 7:
  print("SL")
else:
  print("SU")
