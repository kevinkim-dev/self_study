#########################
#  SWEA number 1860
#  by 김승현  
#########################

# Q. 진기의 최고급 붕어빵

for t in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    buy_list = sorted(list(map(int, input().split())))
    status = 'Possible'
    for i in range(n):
        if (buy_list[i]//m)*k - (i+1) < 0:
            status = 'Impossible'
    print("#%d %s" %(t, status))
    