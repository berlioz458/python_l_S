from __future__ import print_function

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('', end='\t')

for i in range(c, d):
    print(i, end="\t")

print(d, end="\n")

for i in range(a, b):
    print(i, end="\t")
    for j in range(c, d):
        print(i * j, end='\t')
    print(i * d, end='\t')
    print('', end='\n')

print(b, end="\t")
for i in range(c, d):
    print(b * i, end='\t'),

print(b * d, end='\t')
