#########################
#  SWEA number 1251
#  by 김승현                
#########################

# Q. 하나로

def prim(s):
    cost = 0
    visited = [0]
    not_visited = list(range(1, N))
    while not_visited:
        min_cost = float('inf')
        for i in visited:
            for j in not_visited:
                if cost_map[i][j] < min_cost:
                    min_cost = cost_map[i][j]
                    min_info = j
        visited.append(min_info)
        not_visited.remove(min_info)
        cost += min_cost
    return cost


for t in range(1, int(input())+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    cost_map = [[0]*N for _ in range(N)]
    is_list = []
    for i in range(N):
        is_list.append((x_list[i], y_list[i]))
    for i in range(N):
        for j in range(i+1, N):
            cost = (is_list[i][0] - is_list[j][0])**2 + (is_list[i][1] - is_list[j][1])**2
            cost_map[i][j] = cost_map[j][i] = cost
    print("#%d %d" %(t, round(prim(0)*E)))