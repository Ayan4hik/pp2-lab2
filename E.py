line = input().split()
n = int(line[0])
if len(line)==1:
    x = int(input())
else:
    x = int(line[1])
arr=[]
for i in range(n):
    arr.append(x+2*i)
answer = arr[0]
for i in range(n-1):
    answer = answer ^ arr[i+1]
print (answer)
