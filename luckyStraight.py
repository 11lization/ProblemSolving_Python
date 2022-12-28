score = input()
arr = list(score)

arr_len = len(arr)
#파이썬에 리스트를 반으로 쪼개는 것이 있나?
front = 0
back = 0
for i in range(arr_len // 2):
    front += int(arr[i])
    back += int(arr[(arr_len - 1) - i])

if front == back:
    print("LUCKY")
else:
    print("READY")