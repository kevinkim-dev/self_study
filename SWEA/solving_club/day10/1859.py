#########################
#  SWEA number 1859
#  by 김승현                
#########################

# Q. 백만 장자 프로젝트

# 1. 가장 큰 수를 찾는다
# 2. 그 수 왼쪽으로 차액만큼을 모두 더한다
# 3. 그 수 오른쪽에서 가장 큰 수를 찾는다
# 4. 반복...
# 5. 어떻게 끝낼 것인가?
# 6. break 사용

for t in range(1, int(input())+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    length = len(num_list)
    from_idx = 0
    max_idx = 0
    money = 0
    while from_idx < n:
        max_cost = 0
        for l in range(from_idx, length):
            if num_list[l] >= max_cost:
                max_idx = l
                max_cost = num_list[l]
        for i in range(from_idx, max_idx):
            money += num_list[max_idx] - num_list[i]
        from_idx = max_idx + 1
    print("#%d %d" %(t, money))