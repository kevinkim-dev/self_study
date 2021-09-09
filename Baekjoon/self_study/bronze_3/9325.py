###########################
#  BaekJoon 9325번
#  by 김승현                
###########################

# Q. 얼마?

for _ in range(int(input())):
    car = int(input())
    for _ in range(int(input())):
        a, b = map(int, input().split())
        car += a * b
    print(car)