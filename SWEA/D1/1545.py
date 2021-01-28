#########################
#  SWEA number 1545 
#  by 김승현                
#########################

# Q. 거꾸로 출력해 보아요

n = int(input())
num_string = f'{n} '

# 1씩 빼면서 string에 추가
while n:
    n -= 1
    num_string += f'{n} '

# 마지막 공백을 제외하고 출력
print(num_string[:-1])

