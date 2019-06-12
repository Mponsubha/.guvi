a,b=input().split()
a=int(a)
b=int(b)
g=0
array = [int(i) for i in input().split()]
for x in range (0,b):
    g=g+array[x]
print(g)
