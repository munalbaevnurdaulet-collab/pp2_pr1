def is_valid(n):
    for digit in n:
        if int(digit) % 2 != 0:
            return "Not valid"
    return "Valid"


number = input()
print(is_valid(number))