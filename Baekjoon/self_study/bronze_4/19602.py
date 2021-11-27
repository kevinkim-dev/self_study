###########################
#  BaekJoon 19602번
#  by 김승현                
###########################

# Q. Dog Treats

a, b, c = int(input()), int(input()), int(input())

x = a + 2*b + 3*c

if x >= 10:
    print('happy')
else:
    print('sad')