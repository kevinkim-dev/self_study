#########################
#  SWEA number 1225
#  by 김승현                
#########################

# Q. 암호생성기

# 사이클 함수 return값은 0 혹은 1
def cycle():
    for i in range(1, 6):
        x = num_list.pop(0) - i
        if x <= 0:
            num_list.append(0)
            return 0
        else:
            num_list.append(x)
    return 1

for t in range(1, 11):
    a = int(input())
    num_list = list(map(int, input().split()))
    while cycle():
        pass
    print("#%d" %t, end=' ')
    print(*num_list)