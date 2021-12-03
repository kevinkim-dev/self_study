###########################
#  BaekJoon 1476번
#  by 김승현                
###########################

# Q. 날짜 계산

E, S, M = map(int, input().split())

ans = 1

while True:
    if ans % 15 == E % 15 and ans % 28 == S % 28 and ans % 19 == M % 19:
        print(ans)
        break
    ans += 1
