#########################
#  SWEA number 2068  
#  by 김승현                
#########################

# Q. 최대수 구하기

# 첫 input만큼 반복할 것
# index를 통해 test_case number를 출력
for index in range(int(input())):
    num_max = 0
    # 받아온 str을 공백을 기준으로 잘라서 mapping
    for n in map(int, input().split()):
        # 현재까지 최대값보다 크면 최대값 교체
        if n > num_max:
            num_max = n
    print(f"#{index+1} {num_max}")

