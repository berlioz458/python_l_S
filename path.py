x = []
a = int(input())
for i in range(1, a + 1):
    count = 1
    while (count <= i) & (len(x) < a):
        x.append(i)
        count += 1

for i in range(len(x)):
    print(x[i], end=" ")
