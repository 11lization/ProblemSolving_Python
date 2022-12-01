N, K = map(int, input().split())
arra = list(map(int, input().split()))
arrb = list(map(int, input().split()))

arra.sort()
# 애초에 reverse를 이용해서 정렬하면 편리하다.
arrb.sort(reverse=True)

for i in range(K):
    if arra[i] < arrb[i]:
        arra[i], arrb[i] = arrb[i], arra[i]
    # 사실상 없어도 되지만 더 효율적인 code를 위한 것
    else:
        break

# 이정도는 좀 알고 있자.
print(sum(arra))