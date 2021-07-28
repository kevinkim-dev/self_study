###########################
#  BaekJoon 2460번
#  by 김승현                
###########################

# Q. 지능형 기차2


num, max_num = 0, 0

for _ in range(10):
    a, b = map(int, input().split())
    num = num-a+b
    max_num = max(max_num, num)

print(max_num)
