def func(result, target):
    if result == 0 or target == 0 or result == 1 or target == 1:
        result += target
    else:
        result *= target
    return result

str = input()
arr = list(str)

result = int(arr[0])
for i in range(0, len(arr) - 1):
    result = func(result, int(arr[i + 1]))

print(result)
