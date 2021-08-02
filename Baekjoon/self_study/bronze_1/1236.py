###########################
#  BaekJoon 1236번
#  by 김승현                
###########################

# Q. 성 지키기

r, c = map(int, input().split())
castle = [list(input()) for _ in range(r)]
rx, cx = 0, 0
for i in range(r):
    if 'X' not in castle[i]:
        rx += 1
for i in range(c):
    flag = 0
    for j in range(r):
        if castle[j][i] == 'X':
            flag = 1
            break
    if not flag:
        cx += 1

print(max(rx, cx))
