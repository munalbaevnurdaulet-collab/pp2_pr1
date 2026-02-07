a = int(input())
b = input().split()
c = list()
for i in range(a):
    b[i] = int(b[i])
for i in range(a):
    if b[i] in c:
        print("NO")
        continue
    else:
        print("YES")
        c.append(b[i])
      

    

        
