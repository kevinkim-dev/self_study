###########################
#  BaekJoon 7576번
#  by 김승현                
###########################

# Q. 토마토 !미완료!


# 1. 이중 배열 생성
# 2. 모든 토마토에 대해서 1인 토마토 위아래 왼오른쪽 토마토가 0이면
#    1로 바뀐 새로운 배열 생성
# 3. 배열 생성 완료 후 전의 배열과 동일한지 확인
# 4. 동일한데, 0이 있는경우 -> 출력 -1
# 5. 동일한데, 0이 없는 경우 -> 출력 count
# 6. 이미 한번 익힌 토마토는 2로 바꿔서 또 바꾸지 않도록 한다.

import copy

def check_rotten(box, M, N):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if box[i][j] == 0:
                return False
    return True

M, N = map(int, input().split())

tomato_box = [0]*(N+2)

for n in range(N+2):
    if n == 0 or n == N+1:
        tomato_box[n] = [-1]*(M+2)
    else:
        tomato_box[n] = [-1] + list(map(int, input().split())) + [-1]

count = 0

while True:
    if check_rotten(tomato_box, M, N) is True:
        print(count)
        break
    next_box = copy.deepcopy(tomato_box)
    count += 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if tomato_box[i][j] == 1:
                if tomato_box[i-1][j] == 0:
                    next_box[i-1][j] = 1 
                if tomato_box[i+1][j] == 0:
                    next_box[i+1][j] = 1
                if tomato_box[i][j-1] == 0:
                    next_box[i][j-1] = 1 
                if tomato_box[i][j+1] == 0:
                    next_box[i][j+1] = 1
            else:
                continue
    if tomato_box == next_box:
        print(-1)
        break
    else:
        tomato_box = copy.deepcopy(next_box)

# import copy

# def check_rotten(box, M, N):
#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             if box[i][j] == 0:
#                 return False
#     return True

# M, N = map(int, input().split())

# tomato_box = [0]*(N+2)

# for n in range(N+2):
#     if n == 0 or n == N+1:
#         tomato_box[n] = [-1]*(M+2)
#     else:
#         tomato_box[n] = [-1] + list(map(int, input().split())) + [-1]

# count = 0

# while True:
#     if check_rotten(tomato_box, M, N) is True:
#         print(count)
#         break
#     next_box = copy.deepcopy(tomato_box)
#     count += 1
#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             if tomato_box[i][j] == 1:
#                 if tomato_box[i-1][j] == 0:
#                     next_box[i-1][j] = 1 
#                 if tomato_box[i+1][j] == 0:
#                     next_box[i+1][j] = 1
#                 if tomato_box[i][j-1] == 0:
#                     next_box[i][j-1] = 1 
#                 if tomato_box[i][j+1] == 0:
#                     next_box[i][j+1] = 1
#             else:
#                 continue
#     if tomato_box == next_box:
#         print(-1)
#         break
#     else:
#         tomato_box = copy.deepcopy(next_box)
    