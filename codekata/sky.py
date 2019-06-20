def g(n1,n2):
  if(n2==0):
    return n1
  else:
    return g(n2,n1%n2)
n1,n2=map(int,input().split())
print(g(n1,n2))
