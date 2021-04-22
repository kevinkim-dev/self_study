#########################
#  SWEA number 11959
#  by 김승현                
#########################

# Q. 최소 이동 거리

for i in range(1, int(input())+1):
    N, E = map(int, input().split())
    adj_list = [[float('inf')]*N for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
