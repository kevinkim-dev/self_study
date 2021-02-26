#########################
#  SWEA number 1974
#  by 김승현                
#########################

# Q. 스도쿠 검증

def check_row(square):
    for row in range(9):
        row_list = []
        for col in range(9):
            check = square[row][col]
            if check in row_list:
                return False
            else:
                row_list.append(check)
    return True

def check_col(square):
    for col in range(9):
        col_list = []
        for row in range(9):
            check = square[row][col]
            if check in col_list:
                return False
            else:
                col_list.append(check)
    return True

def check_box(square):
    row = 0
    col = 0
    for _ in range(9):
        box_list = []
        for i in range(3):
            for j in range(3):
                check = square[row+i][col+j]
                if check in box_list:
                    return False
                else:
                    box_list.append(check)
        row += 3
        if row == 9:
            col += 3
            row -= 9
    return True

for t in range(1, int(input())+1):
    square = [0]*9
    for i in range(9):
        square[i] = list(map(int, input().split()))

    if check_row(square) and check_col(square) and check_box(square):
        print("#%d 1" %t)
    else:
        print("#%d 0" %t)