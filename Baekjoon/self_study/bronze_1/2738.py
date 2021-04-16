###########################
#  BaekJoon 2738번
#  by 김승현                
###########################

# Q. 행렬 덧셈

N, M = map(int, input().split())
A, B = list(), list()
for _ in range(N):
    A.extend(list(map(int, input().split())))
for _ in range(N):
    B.extend(list(map(int, input().split())))
C = [a + b for a, b in zip(A, B)]
for n in range(N):
    print(*C[n*M:(n+1)*M])
