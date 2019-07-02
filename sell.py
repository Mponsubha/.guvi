sp=int(input())
if sp>1:
  for i in range(2,sp):
    if sp%i == 0:
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
