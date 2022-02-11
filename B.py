n = int(input())
line = input().split()
for i in range(n):
    line[i] = int(line[i])
line.sort()
print(line[n-1]*line[n-2])
