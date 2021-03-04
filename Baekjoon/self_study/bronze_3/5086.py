###########################
#  BaekJoon 5086번
#  by 김승현                
###########################

# Q. 배수와 약수

a, b = map(int, input().split())
while (a, b) != (0, 0):
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
    a, b = map(int, input().split())