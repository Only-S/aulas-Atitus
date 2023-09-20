
# Trecho 1
a = 1
while a < 5:
    a += 1
print(a) #valor de a é 5

print('-' * 10)

# Trecho 2
a = 1
while a <= 5:
    print(a) #1, 2, 3, 4, 5
    a += 1
print(a) #valor de a é 6

print('-' * 10)

# Trecho 3
a = 0
while a < 5:
    a += 1
    print(a) #1, 2, 3, 4, 5
print(a) #valor de a é 5

print('-' * 10)

# Trecho 4
a = 6
b = 0
while (a - 2) > (b + 1): #4 > 1, 3 > 1, 2 > 1, 1 > 1
    print(f"{a} - {b}") #6-0, 5-0, 4-0
    a -= 1
print(a) #valor de a é 3