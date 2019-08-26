s = input()

count = 1
j = 1
i = 0

for i in range(len(s)):
    if j == len(s):
        print(s[i], end="")
        print(count, end="")
        break
    if s[i] == s[j]:
        count += 1
        i += 1
        j += 1
    else:
        print(s[i], end="")
        print(count, end="")
        count = 1
        i += 1
        j += 1
