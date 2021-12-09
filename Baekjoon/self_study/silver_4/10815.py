###########################
#  BaekJoon 10815번
#  by 김승현                
###########################

# Q. 숫자 카드

def find(num):
    s, e = 0, N-1
    while True:
        m = (s + e) // 2
        if num_list[m] == num:
            return True
        elif num_list[m] > num:
            e = m
        else:
            if s == m:
                s += 1
                continue
            s = m
        if s == e:
            return False


N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
check_list = list(map(int, input().split()))

ans = []

for check in check_list:
    ans.append(str(int(find(check))))

print(' '.join(ans))