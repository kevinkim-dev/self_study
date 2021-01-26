#########################
#  SWEA number 2027
#  by 김승현                
#########################

# Q. 대각선 출력하기

# 첫번째 방법
line = ['+'] * 5
lines = []

for i in range(5):
    lines.append(line[:])   # line[:] 대신에 list(line)도 가능
    lines[i][i] = '#'       # 어제 배운 list 심화!
    print("".join(lines[i]))

# 두번째 방법
line = ['+'] * 5

for i in range(5):
    line = ['+'] * 5
    line[i] = '#'
    print("".join(line))

# 세번째 방법
line = ['+'] * 4
lines = []
for i in range(5):
    lines.append(line[:])
    lines[i].insert(i, '#')
    print("".join(lines[i]))