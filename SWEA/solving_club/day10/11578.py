#########################
#  SWEA number 11578
#  by 김승현                
#########################

# Q. 그래프 경로 코드 제출

def find_route(edge_list, S, G):
    if G in edge_list[S]:
        return 1
    else:
        return bool(sum([find_route(edge_list, s, G) for s in edge_list[S]]))

for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    edge_list = [[] for _ in range(v+1)]

    for _ in range(e):
        edge_start, edge_end = map(int, input().split())
        edge_list[edge_start].append(edge_end)
    S, G = map(int, input().split())
    print("#%d %d" %(t, find_route(edge_list, S, G)))