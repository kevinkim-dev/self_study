###########################
#  BaekJoon 1463번
#  by 김승현                
###########################

# Q. 1로 만들기

def make_one(num, cnt):
    global min_cnt
    if num == 1:
        min_cnt = min(min_cnt, cnt)
        return
    if cnt >= min_cnt:
        return
    if num % 2 == 0:
        make_one(num // 2, cnt + 1)
    if num % 3 == 0:
        make_one(num // 3, cnt + 1)
    make_one(num - 1, cnt + 1)
    return

N = int(input())
min_cnt = float('inf')
make_one(N, 0)
print(min_cnt)