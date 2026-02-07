a = int(input())
arr = list()
arr11 = list()
pairs = list()
for i in range(a):
    b = input()
    arr.append(b)
for i in range(a):
    if arr[i] in arr11:
        continue
    else:
        arr11.append(arr[i])
        pairs.append((arr[i],i+1))
pairs.sort()
for x,y in pairs:
    print(x,y)
    
        

