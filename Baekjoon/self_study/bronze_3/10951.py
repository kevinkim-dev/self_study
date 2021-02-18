###########################
#  BaekJoon 10951번
#  by 김승현                
###########################

# Q. A+B - 4

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break