# ##########################
#  project_euler number 28
#  by 김승현                
# ##########################

# Q. 1001×1001 나선모양 행렬에서 대각선 원소의 합은?

# 오른쪽 아래: 2+8n 차
# 왼쪽 아래: 4+ 8n 차이
# 왼쪽 위: 6 + 8n 차이
# 오른쪽 위: 8n 차이

N = 1001

length = int((N-1)/2)

SE = 1
SW = 1
NW = 1
NE = 1
mul = 1

for i in range(length):
    SE += 2 + 8*i
    mul += SE
    SW += 4 + 8*i
    mul += SW
    NW += 6 + 8*i
    mul += NW
    NE += 8 + 8*i
    mul += NE

print(mul)


