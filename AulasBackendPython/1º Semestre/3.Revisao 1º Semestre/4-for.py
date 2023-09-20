
# Trecho 1
for i in range(5): #de 0 a 4
    pass
print(i) #i = 4

print('-' * 10)

# Trecho 2
a = 0
for i in range(3): #de 2 a 2
    print(a) #0, 0, 1
    a += i
print(a)#a = 3

print('-' * 10)

# Trecho 3
a = 0
for i in range(2, 10, 2):#de 10 a 9 passo 2
    a += i
    print(a) #2, 6, 12, 20
print(a) #a = 20

print('-' * 10)

# Trecho 4
a = 10
for i in range(5, 1, -1): #de 2 a 2 passo -1
    a -= i #5, 1, -2, -4
print(a) #a = -4