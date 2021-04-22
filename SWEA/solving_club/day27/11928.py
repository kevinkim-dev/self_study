#########################
#  SWEA number 11928
#  by 김승현                
#########################

# Q. DFS

def add_node(s, e):
    if s not in adj_list.keys():
        adj_list[s] = [e]
    else:
        if e not in adj_list[s]:
            adj_list[s].append(e)
    return


def DFS(x):
    for node in adj_list[x]:
        if node not in visited:
            visited.append(node)
            DFS(node)
    return


for t in range(1, int(input())+1):
    N, V = map(int, input().split())
    adj_list = dict()
    for i in range(V):
        s, e = map(int, input().split())
        add_node(s, e)
        add_node(e, s)
    visited = [1]
    DFS(1)
    ans = '-'.join(list(map(str, visited)))
    print("#%d %s" %(t, ans))