###########################
#  BaekJoon 10952번
#  by 김승현                
###########################

# Q. A+B - 5

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
