###########################
#  BaekJoon 9295번
#  by 김승현                
###########################

# Q. 주사위

N = int(input())

for i in range(1, N+1):
    a, b = map(int, input().split())
    print(f'Case {i}: {a+b}')