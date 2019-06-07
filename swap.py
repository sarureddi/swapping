n1 = int(input())
l1=list(map(int,input().split()))
l1.sort()
s1=0
c1=0
for i1 in range(0,len(l1)):
    if l1[i1]>=s1:
        c1=c1+1
    s1=s1+l1[i1]
print(c1)
