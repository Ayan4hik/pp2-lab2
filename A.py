line = input().split()
length = len(line)
answer = []

for i in range(length):
    line[i] = int(line[i])
    answer.append(0)
answer[0] = 1

for i in range(length):
    if answer[i] == 1:
        num = line[i]
        while num>0:
            if i + num>length-1:
                num = num-1
            else:
                answer[i+num] = 1
                num = num - 1

print(answer[length-1])

