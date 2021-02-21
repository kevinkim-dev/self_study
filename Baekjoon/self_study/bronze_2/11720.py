###########################
#  BaekJoon 11720번
#  by 김승현                
###########################

# Q. 숫자의 합

_sum = 0
length = int(input())
num = int(input())
for _ in range(length):
    _sum += num % 10
    num //= 10
print(_sum)
    