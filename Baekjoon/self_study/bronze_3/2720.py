###########################
#  BaekJoon 2720번
#  by 김승현                
###########################

# Q. 세탁소 사장 동혁

costs = [25, 10, 5, 1]

for _ in range(int(input())):
    N = int(input())
    ans = []
    for cost in costs:
        ans.append(str(N//cost))
        N %= cost
    print(' '.join(ans))
