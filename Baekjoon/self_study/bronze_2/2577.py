###########################
#  BaekJoon 2577번
#  by 김승현                
###########################

# Q. 숫자의 개수

mul = 1
num_count = [0]*10
for _ in range(3):
    mul *= int(input())
for i in range(len(str(mul))):
    num_count[mul % 10] += 1
    mul //= 10
for num in num_count:
    print(num)