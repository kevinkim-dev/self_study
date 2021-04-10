#########################
#  SWEA number 11748
#  by 김승현                
#########################

# Q. Tree 8일차 subtree


def preorder(T):
    visited.append(T)
    for i in range(len(v_list[T])):
        preorder(v_list[T][i])
    return

for t in range(1, int(input())+1):
    V, N = map(int, input().split())
    v_list = list([] for v in range(V+2))
    edge_list = list(map(int, input().split()))
    for v in range(V):
        a, b = edge_list[2*v], edge_list[2*v + 1]
        v_list[a].append(b)
    visited = []
    preorder(N)
    print("#%d %d" %(t, len(visited)))
