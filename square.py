i = 1
x = 0
square = 0
suum = 0
while i != 0:
    x = int(input())
    square += x * x
    suum += x
    if suum == 0:
        break
print(square)
