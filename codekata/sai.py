ai1=int(input())
ak1=list(map(int,input().split()))
for i in ak1:
    if ak1[i]>ak1[i+1]:
        print(i)
        break
