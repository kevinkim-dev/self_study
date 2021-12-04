###########################
#  BaekJoon 1526번
#  by 김승현                
###########################

# Q. 가장 큰 금민수

def kumin(num):
    for n in num:
        if n not in ('4', '7'):
            return False
    return True

N = int(input())

while N:
    num = str(N)
    if kumin(num):
        print(num)
        break
    N -= 1