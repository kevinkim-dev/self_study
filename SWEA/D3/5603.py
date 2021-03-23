#########################
#  SWEA number 5603
#  by 김승현                
#########################

# Q. [Professional] 건초더미

for t in range(1, int(input())+1):
    N = int(input())
    grass_list = [int(input()) for _ in range(N)]
    avg = sum(grass_list)//N
    change = 0
    for n in range(N):
        change += abs(grass_list[n] - avg)
    print("#%d %d" %(t, change//2))