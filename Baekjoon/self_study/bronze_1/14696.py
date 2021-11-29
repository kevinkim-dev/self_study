###########################
#  BaekJoon 14696번
#  by 김승현                
###########################

# Q. 딱지놀이

for _ in range(int(input())):
    A_list, B_list = list(map(int, input().split()))[1:], list(map(int, input().split()))[1:]
    A_list.sort()
    B_list.sort()
    flag = 1
    for _ in range(min(len(A_list), len(B_list))):
        a, b = A_list.pop(), B_list.pop()
        if a > b:
            print('A')
            flag = 0
            break
        elif a < b:
            print('B')
            flag = 0
            break
    if flag:
        if len(A_list):
            print('A')
        elif len(B_list):
            print('B')
        else:
            print('D')
    