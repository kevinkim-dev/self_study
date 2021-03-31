###########################
#  BaekJoon 1242번
#  by 김승현                
###########################

# Q. 소풍

N, K, M = map(int, input().split())
kick = 1
cnt = 0
while True:
    kick += K-1
    while kick > N-cnt:
        kick = kick - (N-cnt)
    cnt += 1
    if kick == M or cnt == N:
        break
    elif kick < M:
        M -= 1
print(cnt)
    
