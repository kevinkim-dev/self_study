###########################
#  BaekJoon 11057번
#  by 김승현                
###########################

# Q. 오르막 수 !미완료

# u(l, num) -> 시작이 num이고 길이가 l인 오르막수의 갯수
# u(l, num) = sum(u(l-1, num), u(l-1, num+1), ..., u(l-1, 9))

def up_num(length, num):
    _sum = 0
    if length == 1:
        return 1
    else:
        for i in range(num, 10):
            _sum += up_num(length-1, i)
        return _sum % 10007
        # return _sum



length = int(input())

print(up_num(length+1, 0))