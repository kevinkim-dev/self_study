#########################
#  Programmers problem
#  Kakao internship 2021
#  by 김승현                
#########################

# Q. 4번

# def go(x, cost):
#     global answer
#     if x == end:
#         answer = min(cost, answer)
#         return
#     for i in range(1, n+1):
#         if adj_road[x][i] and visited[i] < 2:
#             visited[i] += 1
#             if i in traps:
#                 for j in range(1, n+1):
#                     adj_road[i][j], adj_road[j][i] = adj_road[j][i], adj_road[i][j]
#             go(i, cost + adj_road[x][i])
#             visited[i] -= 1
#             if i in traps:
#                 for j in range(1, n+1):
#                     adj_road[i][j], adj_road[j][i] = adj_road[j][i], adj_road[i][j]
#     return

# def solution(n, start, end, roads, traps):
#     answer = 0
#     visited = [0]*(n+1)
#     adj_road = [[0]*(n+1) for _ in range(n+1)]
#     for s, e, c in roads:
#         adj_road[s][e] = c
#     go(start, 0)
#     return answer

def solution(n, start, end, roads, traps):
    answer = 0
    visited = [0]*(n+1)
    adj_road = [[0]*n+1 for _ in range(n+1)]
    for s, e, c in roads:
        adj_road[s][e] = c
    print(adj_road)
    D = [float('inf')]*(n+1)
    
    return answer


n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
solution(n, start, end, roads, traps)