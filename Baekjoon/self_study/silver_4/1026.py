###########################
#  BaekJoon 1026번
#  by 김승현                
###########################

# Q. 보물

N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A[i]*B[i]

print(ans)