#########################
#  SWEA number 1986  
#  by 김승현                
#########################

# Q. 지그재그 숫자

T = int(input())

for t in range(1, T+1):
    _sum = 0
    for k in range(1, int(input())+1):
        # 1부터 해당 숫자까지 짝수면 빼고 홀수면 더한다
        if k % 2 == 0:
            _sum -= k
        else:
            _sum += k
    print(f"#{t} {_sum}")