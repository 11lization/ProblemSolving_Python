# n = int(input())
# arr = [0] * n
# for i in range(n):
#     arr[i] = int(input())

# arr = [list(map(int, input().split())) for _ in range(10)]
# print(arr)
# x, y = 1, 1
# arr[y][x] = 9
#
# while True:
#     if arr[y][x + 1] == 0:
#         arr[y][x + 1] = 9
#         x += 1
#     else if arr[y + 1][x] == 0:
#         arr[y + 1][x] = 9
#         y += 1
#     else if arr[y][x + 1] == 2:
#         arr[y][x + 1] = 9
#         break
#     else if arr[y + 1][x] == 2:
#         arr[y + 1][x] = 9
#         break
#     else:
#     break
#
# for fir in arr:
#     for sec in fir:
#         print(sec, end=' ')
#     print()

# check = [False for _ in range(10)]
# case = list(input().split())
# false = 0
#
# for i in range(len(case)):
#     for c in case[i]:
#         check[int(c)] = True
#     for t in check:
#         if not t:
#             false = 1
#             break
#     if false :
#         print("false", end = ' ')
#     else:
#         print("true", end = ' ')
#     false = 0
#     for i in range(10):
#         check[i] = False

arr = map(int, input().split())
arr1 = list(arr)
print(arr)
print(arr1)