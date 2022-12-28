# def solution(s):
#     s_len = len(s)
#     comp = ""
#     answer = 1000
#     for i in range(1, s_len//2 + 1):
#         cnt = 1
#         for j in range(i, s_len, i):
#             tempStr = ""
#             flag = True
#             for k in range(i):
#                 tempStr += s[j]
#                 if s[j - k] == s[j]:
#                     flag = False
#             if flag = True:
#                 cnt += 1
#             else:
#                 if cnt > 1:
#                     comp += str(cnt)
#                     comp += tempStr
#             answer = min(answer, len(comp))
#     return answer

def solution(s):
    s_len = len(s)
    answer = 1000
    for i in range(1, s_len//2 + 1):
        comp = ""
        tempArr = []
        tempStr = ""
        temp = 0
        for j in range(s_len):
            tempStr += s[j]
            temp += 1
            if temp == i or j == s_len - 1:
                tempArr.append(tempStr)
                tempStr = ""
                temp = 0
        tempArr.append("")
        print(tempArr)
        cnt = 1
        tempArr_len = len(tempArr)
        for j in range(1, tempArr_len):
            if tempArr[j] == tempArr[j - 1]:
                cnt += 1
            else:
                if cnt > 1:
                    comp += str(cnt)
                    comp += tempArr[j - 1]
                    cnt = 1
                else:
                    comp += tempArr[j - 1]
                    cnt = 1
        print(comp)
        answer = min(answer, len(comp))
    print(answer)
    return answer