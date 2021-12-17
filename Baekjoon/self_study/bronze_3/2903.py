###########################
#  BaekJoon 2903번
#  by 김승현                
###########################

# Q. 중앙 이동 알고리즘

k = 3

N = int(input())

for i in range(N-1):
    k = 2*k-1

print(k*k)