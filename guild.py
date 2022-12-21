N = int(input())
mo = list(map(int, input().split()))
mo.sort(reverse=True)

arrLen = len(mo)
cnt = 0
temp = []
for i in range(0, arrLen):
    temp.append(mo.pop())
    if temp[len(temp) - 1] == len(temp):
        temp = []
        cnt += 1

print(cnt)