# 길이 5000의 list를 사용한 풀이
T = int(input())

for t in range(1, T+1):
    N = int(input())
    all_stop_list = [0]*5000

    for n in range(N):
        a, b = map(int, input().split())
        for stop in range(a-1, b):
            all_stop_list[stop] += 1
    P = int(input())
    stop_list = [0]*P
    for p in range(P):
        stop_list[p] = str(all_stop_list[int(input())-1])
    ans = " ".join(stop_list)
    print("#%d %s" %(t, ans))

# # 이중배열을 이용한 풀이
# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     all_stop_list = [0]*N

#     for n in range(N):
#         all_stop_list[n] = list(map(int, input().split()))
#     P = int(input())
#     stop_list = [0]*P
#     for p in range(P):
#         stop = int(input())
#         count = 0
#         for stops in all_stop_list:
#             if stop >= stops[0] and stop <= stops[1]:
#                 count += 1
#         stop_list[p] += count
#     stop_list = map(str, stop_list)
#     ans = " ".join(stop_list)
#     print("#%d %s" %(t, ans))
