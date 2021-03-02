#########################
#  SWEA number 1220
#  by 김승현                
#########################

# Q. Magnetic

for t in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    tab = zip(*table)
    cnt = 0
    for line in tab:
        n_flag = 0
        s_flag = 0
        for n in range(N):
            # N 자성체
            if line[n] == 1:
                n_flag = 1
            # S 자성체
            elif line[n] == 2:
                # N이 있으면 교착상태
                if n_flag:
                    cnt += 1
                    n_flag = 0
    print("#%d %d" %(t, cnt))
                    
