def odd_int(i):
    return i%2==1
l = [12,13,15,14,19,17]
odd = list(filter(odd_int,l))
print(odd)
