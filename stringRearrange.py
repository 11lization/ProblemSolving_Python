import heapq

str = input()
q = []
arr = []
sum = 0

for data in str:
    if ord(data) >= 65:
        heapq.heappush(q, data)
    else:
        sum += int(data)

while q:
    arr.append(heapq.heappop(q))

for data in arr:
    print(data, end = '')
print(sum)
