###########################
#  BaekJoon 14681번
#  by 김승현                
###########################

# Q. 사분면 고르기

x = int(input())
y = int(input())

if x > 0:
    print('1') if y>0 else print('4')
else:
    print('2') if y>0 else print('3')
