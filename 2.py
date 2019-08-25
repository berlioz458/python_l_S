a = int(input())
b = int(input())

mean = 0
s = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        counter += 1

mean = s / counter

print(mean)
