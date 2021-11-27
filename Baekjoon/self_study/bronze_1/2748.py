###########################
#  BaekJoon 2748번
#  by 김승현                
###########################

# Q. 피보나치 수 2

f_0 = 0
f_1 = 1

index = int(input())

for i in range(index-1):
    f_2 = f_0 + f_1
    f_0, f_1 = f_1, f_2

print(f_1)