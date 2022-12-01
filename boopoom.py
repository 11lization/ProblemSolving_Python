# def biSearch(target):
#     start = 0
#     end = N
#     middle = N//2
#     while start <= end:
#         if produce[middle] == target:
#             return True
#         if produce[middle] > target:
#             end = middle - 1
#             # 어차피 2번 쓸 바에는 while문 앞으로 옮기는 게..?
#             middle = (end + start)//2
#         if produce[middle] < target:
#             start = middle + 1
#             middle = (end + start)//2
#     return False
#
# N = int(input())
# produce = list(map(int, input().split()))
# M = int(input())
# consume = list(map(int, input().split()))
#
# # array sort method 이용하기
# produce.sort()
#
# for num in consume:
#     if biSearch(num):
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')

# ---------------------------------------------------------
from bisect import bisect_left

N = int(input())
produce = list(map(int, input().split()))
M = int(input())
consume = list(map(int, input().split()))

produce.sort()

for num in consume:
    if produce[bisect_left(produce, num)] == num:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')