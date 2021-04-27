#########################
#  SWEA number 3282
#  by 김승현                
#########################

# Q. 0/1 Knapsack


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    stuffs = [list(map(int, input().split())) for _ in range(N)]
    values = [0]*(K+1)
    for size, value in stuffs:
        if size > K:
            continue
        for i in range(K, size, -1):
            if not values[i-size]:
                continue
            values[i] = max(values[i], values[i - size] + value)
        values[size] = max(values[size], value)
    print("#%d %d" %(t, max(values)))