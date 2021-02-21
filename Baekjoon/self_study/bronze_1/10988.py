###########################
#  BaekJoon 10988번
#  by 김승현                
###########################

# Q. 펠린드롬인지 확인하기

string = input()

if string == string[::-1]:
    print('1')
else:
    print('0')