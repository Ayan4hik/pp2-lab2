line = input().split()
x = int(line[0])
y = int(line[1])
field = []
dist = []


n = int(input())
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = (a-x)*(a-x) + (b-y)*(b-y)
    field.append(a)
    field.append(b)
    field.append(c)

for i in range(3*n):
    if i%3 == 2:
        dist.append(field[i])

dist.sort()

for i in range(n):
    for j in range(3*n):
        if j%3 == 2:
            if dist[i] == field[j]:
                print(field[j-2], field[j-1])
                dist[i] = 999999999999
