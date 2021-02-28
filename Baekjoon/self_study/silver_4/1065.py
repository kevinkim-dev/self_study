###########################
#  BaekJoon 1065번
#  by 김승현                
###########################

# Q. 한수

def check(x):
    for i in range(len(x)-2):
        if x[i+2]-x[i+1] != x[i+1] - x[i]:
            return False
    return True


n = int(input())

cnt = 0
for num in range(1, n+1):
    num_check = list(map(int, list(str(num))))
    if len(num_check) > 2:
        if check(num_check):
            cnt += 1
    else:
        cnt += 1
print(cnt)