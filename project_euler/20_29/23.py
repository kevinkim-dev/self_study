# ##########################
#  project_euler number 23
#  by 김승현                
# ##########################

# Q. 두 과잉수의 합으로 나타낼 수 없는 모든 양의 정수의 합은?

def divisor_sum(x):
    _sum = 0
    for i in range(1, x):
        if x % i == 0:
            _sum += i
    return _sum

excess_num = []
for n in range(1, 28123):
    if divisor_sum(n) > n:
        excess_num.append(n)

excess_num_cant = list(range(1, 28123))
for i in range(len(excess_num)):
    for j in range(i, len(excess_num)):
        if excess_num[i] + excess_num[j] > 28123:
            break
        elif excess_num[i] + excess_num[j] in excess_num_cant:
            excess_num_cant.remove(excess_num[i] + excess_num[j])
    print(f"{i}번째 과잉수 {excess_num[i]}가 끝났습니다")
print(excess_num_cant, sum(excess_num_cant))