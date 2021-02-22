###########################
#  BaekJoon 1652번
#  by 김승현                
###########################

# Q. 누울 자리를 찾아라

n = int(input())

room = [0]*n
row_cnt = 0
col_cnt = 0

for i in range(n):
    room[i] = input()
    row_check = room[i].split('X')
    for space in row_check:
        if len(space) >= 2:
            row_cnt += 1

for i in range(n):
    col = ''
    for j in range(n):
        col += room[j][i]
    col_check = col.split('X')
    for space in col_check:
        if len(space) >= 2:
            col_cnt += 1

print(row_cnt, col_cnt)
     