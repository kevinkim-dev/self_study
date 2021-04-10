#########################
#  SWEA number 11387
#  by 김승현                
#########################

# Q. 몬스터 사냥

for t in range(1, int(input())+1):
    D, L, N = map(int, input().split())
    damage = D*N + D*L*N*(N-1)//200
    print("#%d %d" %(t, damage))