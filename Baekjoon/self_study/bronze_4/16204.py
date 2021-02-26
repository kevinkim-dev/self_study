###########################
#  BaekJoon 16204번
#  by 김승현                
###########################

# Q. 카드 뽑기

n, m, k = map(int, input().split())

print(min(m, k) + min(n-m, n-k))