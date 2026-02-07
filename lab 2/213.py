n = int(input())
sum = 0
for i in range(2,n):
    if n%i==0:
        sum+=1
if sum == 0:
        print("Yes")
else:
        print("No")