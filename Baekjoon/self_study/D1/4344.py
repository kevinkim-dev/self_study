###########################
#  BaekJoon 4344번
#  by 김승현                
###########################

# Q. 평균은 넘겠지

T = int(input())
for t in range(1, T+1):
    input_list = list(map(int, input().split()))
    _sum = 0
    for i in range(1, input_list[0]+1):
        _sum += input_list[i]
    avg = _sum / input_list[0]

    count = 0
    for i in range(1, input_list[0]+1):
        if input_list[i] > avg:
            count += 1

    ans = format(round(count/input_list[0]*100, 3), ".3f")
    print(ans + '%')