#########################
#  SWEA number 1493
#  by 김승현                
#########################

# Q. 수의 새로운 연산

def find_xy(num):
    _sum, _add = 0, 0
    while _sum < num:
        _add += 1
        _sum += _add
    dif = _sum - num
    return (_add - dif, 1 + dif)

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    a_loc, b_loc = find_xy(a), find_xy(b)
    c_loc = (a_loc[0]+b_loc[0], a_loc[1] + b_loc[1])
    dif = c_loc[1] - 1
    cross = (c_loc[0] + dif)*(c_loc[0] + dif + 1)//2
    print("#%d %d" %(t, cross-dif))
