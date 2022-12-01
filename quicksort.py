def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if pivot >= x]
    right = [x for x in tail if pivot < x]

    return quicksort(left) + [pivot] + quicksort(right)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

result = quicksort(arr)
print(result)