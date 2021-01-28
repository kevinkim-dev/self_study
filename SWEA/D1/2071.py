#########################
#  SWEA number 2071
#  by 김승현                
#########################

# Q. 평균값 구하기 

T = int(input())

for i in range(1, T + 1):
    num_list = list(map(int, input().split()))
    _sum = 0
    for n in num_list:
        _sum += n
    avg = _sum / len(num_list)
    if avg - int(avg) >= 0.5:
        print(f'#{i} {int(avg) + 1}')
    else:
        print(f'#{i} {int(avg)}')