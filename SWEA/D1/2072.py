#########################
#  SWEA number 2072 
#  by 김승현                
#########################

# Q. 홀수만 더하기

T = int(input())

for i in range(T+1):
    num_list = map(int, input().split())
    _sum = 0
    for n in num_list:
        if n % 2 == 1:
            _sum += n
    print(f'#{i} {_sum}')