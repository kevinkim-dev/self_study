###########################
#  BaekJoon 3034번
#  by 김승현                
###########################

# Q. 앵그리 창영

N, R, C = map(int, input().split())

max_len = (R**2 + C**2)**0.5

for _ in range(N):
    match = int(input())
    if match > max_len:
        print('NE')
    else:
        print('DA')