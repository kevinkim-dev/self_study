###########################
#  BaekJoon 2420번
#  by 김승현                
###########################

# Q. 사파리월드

a, b = map(int, input().split())

if a > b:
    print(a-b)
else:
    print(b-a)