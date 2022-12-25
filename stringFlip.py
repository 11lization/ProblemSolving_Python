#문자열 뒤집기
str = input()
arr = list(str)

#0과 1이 바뀔 때마다 증가하는 count
cnt = 1

#0과 1이 바뀌는지 check
for i in range(0, len(arr) - 1):
    if arr[i] != arr[i + 1]:
        cnt += 1

#결국 0과 1중 하나를 뒤집어야 하는데, 홀수번 바뀌었다면 적은 쪽이 cnt//2, 많은 쪽이 cnt//2 + 1
print(cnt//2)
