#########################
#  SWEA number 2019  
#  by 김승현                
#########################

# Q. 더블더블

# 2를 곱할 횟수 받아오기
n = int(input())

num = 1
string = f'{num} '
while n:
    num *= 2
    string += f'{num} ' 
    n -= 1

print(string[:-1])