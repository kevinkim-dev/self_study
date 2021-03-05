#########################
#  SWEA number 4613
#  by 김승현                
#########################

# Q. 러시아 국기 같은 깃발

# 1. 맨 윗줄은 무조건 W
# 2. 두번째 줄부터는 w 혹은 b로 바뀔 수 있다
# 3. 맨 밑줄은 무조건 R
# 4. 그냥 두번째 줄부터 시작. 

colors = ['W', 'B', 'R']

def color(row_idx, cnt, color_idx):
    global min_cnt
    if row_idx == rows-1:
        if color_idx != 0:
            min_cnt = min(min_cnt, cnt)
        return
    if color_idx != 2:
        color(row_idx+1, cnt + cols - flag[row_idx].count(colors[color_idx+1]), color_idx+1)
    color(row_idx+1, cnt + cols - flag[row_idx].count(colors[color_idx]), color_idx)

for t in range(1, int(input())+1):
    rows, cols = map(int, input().split())
    flag = [input() for _ in range(rows)]
    cnt = 2*cols - flag[0].count('W') - flag[-1].count('R')
    min_cnt = float('inf')
    color(1, cnt, 0)
    print("#%d %d" %(t, min_cnt))