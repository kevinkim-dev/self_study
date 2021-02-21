###########################
#  BaekJoon 11721번
#  by 김승현                
###########################

# Q. 열 개씩 끊어 출력하기

string = input()

for i in range((len(string)-1)//10 + 1):
    print(string[i*10:i*10+10])