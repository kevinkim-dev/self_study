#########################
#  SWEA number 2117
#  by 김승현                
#########################

# Q. 홈 방범 서비스

def home_cnt(size):
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for home in homes:
                if abs(home[0] - i) + abs(home[1] - j) <= size-1:
                    cnt += 1
            if cnt == home_num or cnt == cost:
                return cnt
            max_cnt = max(cnt, max_cnt)
    return max_cnt

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    homes = []
    for i in range(N):
        city_row = list(map(int, input().split()))
        for j in range(N):
            if city_row[j] == 1:
                homes.append((i, j))
    home_num = len(homes)
    max_size = N if N % 2 else N+1
    max_home = 0
    for size in range(1, max_size+1):
        cost = size**2 + (size-1)**2
        h_cnt = home_cnt(size)
        if h_cnt * M - cost >= 0:
            if h_cnt == home_num:
                max_home = h_cnt
                break
            max_home = max(max_home, h_cnt)
    print("#%d %d" %(t, max_home))
        
