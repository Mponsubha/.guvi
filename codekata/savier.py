aill,bill=map(int,input().split())
lav=list(map(int,input().split()))
lav1=[]
for i in range(0,len(lav)):
  if lav[i]%2!=0:
    lav1.append(lav[i]) 
print(lav1[bill-1])
