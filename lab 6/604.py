a = int(input())
b = input().split()
c = input().split()
blist=list()
clist=list()
total=list()
for i in range(a):
    b[i]=int(b[i])
    c[i]=int(c[i])
    blist.append(b[i])
    clist.append(c[i])

for blists,clists in zip(blist,clist):
    total.append(blists*clists)

print(sum(total))