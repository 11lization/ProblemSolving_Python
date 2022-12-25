#볼링공 고르기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

#전체 결과 출력 변수
res = 0

#특정 무게 공의 갯수
cnt = 0

for i in range(1, M + 1):
    for ball in arr:
        if ball == i:
            cnt += 1
    res += cnt * (N - cnt)
    cnt = 0

print(res//2)

# # #여집합 풀이
# res = N * (N - 1) // 2
# cnt = 0
# for i in range(1, M + 1):
#     for ball in arr:
#         if ball == i:
#             cnt += 1
#     res -= cnt * (cnt - 1) // 2
#     cnt = 0
#
# print(res)