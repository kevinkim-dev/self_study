#########################
#  SWEA number 11608
#  by 김승현                
#########################

# Q. 배열 최소 합 코드 제출

# 0~N-1로 이루어진 모든 순열을 생성

def get_sum(temp_sum, row, v):
    global min_sum
    for c in col_list:
        if c in v:
            continue
        else:
            v.append(c)
            temp_sum += box[row][c]
            row += 1
            if row >= N:
                min_sum = min(min_sum, temp_sum)
                v.remove(c)
                return
            else:
                get_sum(temp_sum, row, v)
                row -= 1
                v.remove(c)
                temp_sum -= box[row][c]


for t in range(1, int(input())+1):
    N = int(input())
    min_sum = float('inf')
    box = [list(map(int, input().split())) for n in range(N)]
    temp_sum = 0
    col_list = list(range(N))
    visit = []
    get_sum(temp_sum, 0, visit)
    print("#%d %d" %(t, min_sum))

# def get_sum(temp_sum, row, cols):
#     global min_sum
#     for i in range(len(cols)):
#         col = cols.pop(i)
#         temp_sum += box[row][col]
#         row += 1
#         if row >= N and temp_sum < min_sum:
#             min_sum = temp_sum
#         else:
#             get_sum(temp_sum, row, cols)
#             row -= 1
#             cols.insert(i, col)
#             temp_sum -= box[row][col]


# for t in range(1, int(input())+1):
#     N = int(input())
#     min_sum = float('inf')
#     box = [list(map(int, input().split())) for n in range(N)]
#     temp_sum = 0
#     col_list = list(range(N))
#     get_sum(temp_sum, 0, col_list)
#     print("#%d %d" %(t, min_sum))