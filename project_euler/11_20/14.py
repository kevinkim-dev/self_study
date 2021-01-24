###########################
#  project_euler number 14
#  by 김승현                
###########################

# Q. 백만 이하로 시작하는 우박수 중 가장 긴 과정을 거치는 것은?



# 우박수 연산 시 걸리는 절차 횟수 count
def DIY_hailstone_count(x):
    result = 0

    if x == 1:
        return 0    
    while x > 1:
        if x % 2 == 0:
            x = int(x / 2)
        elif x % 2 == 1:
            x = 3*x + 1
        else:
            print("정수가 아닙니다")
        result = result + 1
    return result

max_count = 0
max_count_hailstone = 0

for i in range(1, 1000001):
    count = DIY_hailstone_count(i)
    if count > max_count:
        max_count = count
        max_count_hailstone = i

print(max_count_hailstone)


