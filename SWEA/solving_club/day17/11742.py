#########################
#  SWEA number 11742
#  by 김승현                
#########################

# Q. 트리의 전위순회



def preorder(T):
    visited.append(T)
    for i in range(len(v_list[T])):
        preorder(v_list[T][i])
    return


V = int(input())
v_list = list([] for v in range(V+1))
edge_list = list(map(int, input().split()))
for v in range(V-1):
    a, b = edge_list[2*v], edge_list[2*v + 1]
    v_list[a].append(b)
visited = []
q = []
preorder(1)
ans = '-'.join(map(str, visited))
print(ans)