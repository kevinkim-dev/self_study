#########################
#  SWEA number 1288
#  by 김승현                
#########################

# Q. 새로운 불면증 치료법

T = int(input())

for t in range(1, T+1):
    # 새로운 숫자를 받아온다
    num = int(input())
    # 곱할 숫자
    mul = 0
    # 어떤 숫자가 나왔는지 확인할 list
    count_num_list = []
    # 길이가 10이 되면 0 ~ 9 까지 다 나왔으므로 while 종료
    while len(count_num_list) < 10:
        # 1 더해서 곱한다.
        mul += 1
        counted = num * mul
        # 10으로 나눈 나머지가 list에 있는지 확인하고 없으면 추가
        # 그 후 수가 0이 될때까지 반복해서 모든 자리수 확인
        while counted > 0:
            n = counted % 10
            if count_num_list.count(n) == 0:
                count_num_list.append(n)
            counted //= 10
    # 결과값 출력
    # counted는 이미 10으로 나눠서 재가 되었으므로... num*mul로 출력
    print(f"#{t} {num*mul}")