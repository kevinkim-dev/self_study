# ##########################
#  project_euler number 30
#  by 김승현                
# ##########################

# Q. 각 자리 숫자를 5제곱해서 더했을 때 자기 자신이 되는 수들의 합은?

total = 0

for i in range(2, 9**5 * 6):
    num = i
    _sum = 0
    while num > 0:
        _sum += (num % 10) ** 5
        num //= 10
    if _sum == i:
        print(i)
        total += i

print(total)
