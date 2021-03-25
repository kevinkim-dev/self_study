###########################
#  BaekJoon 2231번
#  by 김승현                
###########################

# Q. 분해합

N = int(input())
min_cre = 1000001
for n in range(N-9*len(str(N)), N):
    if n <= 0:
        continue
    m = n + sum(list(map(int, list(str(n)))))
    if m == N:
        min_cre=min(min_cre, n)
print(min_cre) if min_cre != 1000001 else print('0')