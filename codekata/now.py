def lc(ny1,ni2):
  if ny1>ni2:
    a2=ny1
  else:
    a2=ni2
  while(True):
    if a2%ny1==0 and a2%ni2==0:
      l1=a2
      break
    a2=a2+1
  return l1
  
ny1,ni2=map(int,input().split())
ano=lc(ny1,ni2)
print(ano)





