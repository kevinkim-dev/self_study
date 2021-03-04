#########################
#  SWEA number 11634
#  by 김승현                
#########################

# Q. 피자 굽기 코드 제출

# N개의 피자치즈를 녹이고 반환한다.
def cheese_burn(cheese, idx):
    for i in range(len(oven)):
        cheese[oven[i]] //= 2
        if cheese[oven[i]] == 0:
            if idx < M:
                oven[i] = idx
                idx += 1
            else:
                oven.pop(i)
    print(cheese, oven)
    if cheese.count(0) == M:
        return oven[-1]
    elif cheese.count(0) == M-1:
        return oven.index(not 0)
    else:
        return cheese_burn(cheese, idx)

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = [n for n in range(N)]
    print("#%d %d" %(t, cheese_burn(cheese, N)))