###########################
#  BaekJoon 3460번
#  by 김승현                
###########################

# Q. 이진수 

for _ in range(int(input())):
    num = int(input())
    ans = []
    i = 0
    while num:
        if num % 2:
            ans.append(str(i))
        num //= 2
        i += 1
    print(' '.join(ans))