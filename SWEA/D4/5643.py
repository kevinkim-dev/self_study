#########################
#  SWEA number 5643
#  by 김승현                
#########################

# Q. [Professional] 키 순서

def find_big(i, big_list):
    big_list = list(big_list)
    while big_list:
        x = big_list.pop(0)
        big[i].add(x)
        for n in big[x]:
            if n not in big[i] and n not in big_list:
                big_list.append(n)
    return


def find_small(i, small_list):
    small_list = list(small_list)
    while small_list:
        x = small_list.pop(0)
        small[i].add(x)
        for n in small[x]:
            if n not in small[i] and n not in small_list:
                small_list.append(n)
    return


for t in range(1, int(input())+1):
    N, M = int(input()), int(input())
    big, small = [set() for _ in range(N+1)], [set() for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        big[a].add(b)
        small[b].add(a)
    ans = 0
    for i in range(1, N+1):
        find_big(i, big[i])
        find_small(i, small[i])
        if len(big[i]) + len(small[i]) == N - 1:
            ans += 1
    print("#%d %d" %(t, ans))