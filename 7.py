s_input = input().split()

for i in range(len(s_input)):
    if len(s_input) == 1:
        print(s_input[i], end=" ")
        break
    if i == len(s_input) - 1:
        print(int(s_input[i - 1]) + int(s_input[0]), end=" ")
    else:
        print(int(s_input[i - 1]) + int(s_input[i + 1]), end=" ")
