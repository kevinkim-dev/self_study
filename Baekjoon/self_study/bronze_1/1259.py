###########################
#  BaekJoon 1259번
#  by 김승현                
###########################

# Q. 펠린드롬수

num = input()

while num != '0':
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
    num = input()