n = int(input())
demons = {}
hunters = {}
left = 0
for i in range(n):
    demon, weakness =input().split()
    if weakness in demons:
        demons[weakness]=demons[weakness] + 1
    else:
        demons[weakness]=1

m = int(input())
for i in range(m):
    hunter, ability, power = input().split()
    if ability in hunters:
        hunters[ability] = hunters[ability] + int(power)
    else: 
        hunters[ability] = int(power)

for x in demons:
    if x in hunters:
        if demons[x] > hunters[x]:
            left = left + demons[x] - hunters[x]
    else:
        left = left + demons[x]
print("Demons left: " + str(left))