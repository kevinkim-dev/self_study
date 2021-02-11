###########################
#  BaekJoon 2839번
#  by 김승현                
###########################

# Q. 설탕 배달

# 1. 5로 최대한 나눈다
# 2. 남은 수가 3으로 나눠지나 본다
# 3. 되면 5와 3으로 나눠진 몫 합해서 출력.
# 4. 안되면 5 갯수를 하나 빼고 3으로 나눠지나 확인

weight = int(input())

flag = 0
div_5 = weight // 5

for q_5 in range(div_5, -1, -1):
    left = weight - q_5 * 5
    if left % 3 == 0:
        q_3 = left // 3
        print(q_5 + q_3)
        flag = 1
        break 

if flag == 0:
    print(-1)