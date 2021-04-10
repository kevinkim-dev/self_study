#########################
#  SWEA number 11746
#  by 김승현                
#########################

# Q. 이진탐색트리 - 생성

def insert(tree, node):
    if tree[1] > node:
        if tree[0]:
            insert(tree[0], node)
        else:
            tree[0] = [0, node, 0]
    else:
        if tree[2]:
            insert(tree[2], node)
        else:
            tree[2] = [0, node, 0]
    return

def preorder(T):
    visited.append(T[1])
    for i in (0, 2):
        if T[i]:
            preorder(T[i])
    return

C = int(input())
node_list = list(map(int, input().split()))
nodes = [0, node_list.pop(0), 0]
while node_list:
    insert(nodes, node_list.pop(0))
visited = []
preorder(nodes)
ans = '-'.join(map(str, visited))
print(ans)

# def insert(T, node):
#     print(T, node)
#     print(nodes)
#     if T > node:
#         if nodes[T][0]:
#             insert(nodes[T][0], node)
#         else:
#             nodes[T][0], nodes[node][2] = node, T
#     else:
#         if nodes[T][1]:
#             insert(nodes[T][1], node)
#         else:
#             nodes[T][1], nodes[node][2] = node, T



# C, I, D = map(int, input().split())
# node_list = list(map(int, input().split()))
# # 좌, 우, 부모
# nodes = list([0,0,0] for _ in range(C+I+1))
# root = node_list.pop(0)