N = int(input())
arr = list(map(int, input().split()))

arr.sort()

imp = 1
for i in range(0, N):
    if imp < arr[i]:
        break
    imp += arr[i]

print(imp)