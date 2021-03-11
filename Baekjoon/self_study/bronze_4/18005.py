###########################
#  BaekJoon 18005번
#  by 김승현                
###########################

# Q. Even or Odd?

n = int(input())

if n % 4 == 1 or n % 4 == 3:
    print('0')
elif n % 4 == 2:
    print('1')
else:
    print('2')