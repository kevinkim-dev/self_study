###########################
#  BaekJoon 2675번
#  by 김승현                
###########################

# Q. 문자열 반복

for _ in range(int(input())):
    repeat, string = input().split()
    repeat = int(repeat)
    for char in string:
        print(char*repeat, end='')
    print()