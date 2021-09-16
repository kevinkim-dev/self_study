###########################
#  BaekJoon 4504번
#  by 김승현                
###########################

# Q. 배수 찾기

n = int(input())

while True:
    a = int(input())
    if a:
        if a % n:
            print(f'{a} is NOT a multiple of {n}.')
        else:
            print(f'{a} is a multiple of {n}.')
    else:
        break