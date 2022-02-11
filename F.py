

n = int(input())
max = 0
kbtu = {}

for i in range(n):
    line = input().split()
    name = line[0]
    compensation = int(line[1])
    if name in kbtu:
        kbtu[name] = kbtu[name] + compensation
    else:
        kbtu[name] =  compensation

for x in kbtu:
    if max < kbtu[x]:
        max = kbtu[x]
sorted=sorted(kbtu.keys())

for i in range(len(kbtu)):
    if kbtu[sorted[i]]==max:
        print(sorted[i] + " is lucky!")
    else:
        print(sorted[i] + " has to receive " + str(max - kbtu[sorted[i]]) + " tenge")