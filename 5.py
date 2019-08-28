workers = ['Kate', 'Yulia']

for worker in workers:
    print("Hello, " + worker)


print(workers[-1])
print(len(workers))

# списки можно складывать
# списки можно перемножать

workers.append('Olga')
workers += ['Evgenia']

for worker in workers:
    print("Hello, " + worker)

workers.insert(0, 'Lena')

for worker in workers:
    print("Hello, " + worker)

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(len(students))

# delete
workers.remove('Olga')
del workers[0]
for worker in workers:
    print("Hello, " + worker)


# search : in or not in
# sort

# generation list
a = [0] * 5
b = [0 for i in range(5)]
c = [i * i for i in range(5)]
d = [int(i) for i in input().split()]
