# ##########################
#  project_euler number 26
#  by 김승현                
# ##########################

# Q. 1000 이하의 d 중에서 1/d 이 가장 긴 순환마디를 갖는 수는?

# 나눌 때 10씩 곱하고 나눗셈을 진행
# 나머지가 이전에 나왔던 수와 같은 수가 나오면 순환마디가 시작되는 것!
def cycle_len(x):
    remainder_list = [1]
    current_index = 0
    while True:
        remainder = (remainder_list[current_index] * 10) % x
        current_index += 1
        if remainder in remainder_list:
            first_index = remainder_list.index(remainder)
            return current_index - first_index
        remainder_list.append(remainder)



max_len = 0
for num in range(2, 1001):
    if cycle_len(num) > max_len:
        max_len = cycle_len(num)
        print(f"{num}의 순환마디는 {max_len}")

print(max_len)