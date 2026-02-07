a,b,c = map(int,input().split())
arr = list(map(int,input().split()))

arrp2 = arr[b-1:c]
arrp2.reverse()
arr[b-1:c] = arrp2

print(*arr)