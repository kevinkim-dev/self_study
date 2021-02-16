#########################
#  SWEA number 11555
#  by 김승현                
#########################

# Q. 색칠하기

# 빨간색이면 1
# 파란색이면 2
# 둘다 되었으면 3
# 3이면 pass

def color_red(color_box, color):
    for row in range(color[0], color[2]+1):
        for col in range(color[1], color[3]+1):
            if color_box[row][col] == 0 or color_box[row][col] == 2:
                color_box[row][col] += 1
    return color_box

def color_blue(color_box, color):
    for row in range(color[0], color[2]+1):
        for col in range(color[1], color[3]+1):
            if color_box[row][col] == 0 or color_box[row][col] == 1:
                color_box[row][col] += 2
    return color_box

for t in range(1, int(input())+1):
    length = int(input())
    color_list = [0]*length
    color_box = [0]*10
    for n in range(10):
        color_box[n] = [0]*10
    for i in range(length):
        color_list[i] = list(map(int, input().split()))
    for color in color_list:
        if color[4] == 1:
            color_box = color_red(color_box, color)
        else:
            color_box = color_blue(color_box, color)
    purple = 0
    for r in range(10):
        for c in range(10):
            if color_box[r][c] == 3:
                purple += 1
    print("#%d %d" %(t, purple))
