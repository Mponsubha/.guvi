f11=input()
f2=""
for i in f11:
  if i not in f2:
    f2=f2+i
if(f11==f2):
  print("Yes")
else:
  print("No")
