###########################
#  BaekJoon 15873번
#  by 김승현                
###########################

# Q. 공백 없는 A+B

string = input()

if len(string)<=2:
    print(int(string[0]) + int(string[1]))
elif len(string) == 3:
    if string[2] == '0':
        print(int(string[0]) + int(string[1:]))  
    else:
        print(int(string[0:2]) + int(string[2]))
else:
    print('20')