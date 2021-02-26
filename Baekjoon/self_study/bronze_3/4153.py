###########################
#  BaekJoon 4153번
#  by 김승현                
###########################

# Q. 직각삼각형

a, b, c = sorted(list(map(int, input().split())))

while a != 0:
    print('right') if a ** 2 + b ** 2 == c ** 2 else print('wrong')
    a, b, c = sorted(list(map(int, input().split())))