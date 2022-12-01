N = int(input())
c = [[] for _ in range(101)]

for _ in range(N):
    name, score = input().split()
    c[int(score)].append(name)

# 아래 for문의 time complexity는 최대 학생수인 100,000이라고 봐야겠지? 겉으로는 2중 for문이지만 최대 원수의 갯수가 N개로 제한되어 있으니까.
for i in range(1, 101):
    for x in c[i]:
        print(x, end = ' ')

# tuple로 묶은 뒤에 key 값을 이용한 sorting을 통해서도 풀어낼 수 있다.