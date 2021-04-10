#########################
#  SWEA number 1231
#  by 김승현                
#########################

# Q. 중위순회

def inorder(T):
    if len(v_list[T]) >= 2:
        inorder(v_list[T][1])
    visited.append(v_list[T][0])
    if len(v_list[T]) == 3:
        inorder(v_list[T][2])
    return

for t in range(1, 11):
    V = int(input())
    v_list = list([] for v in range(V+1))
    for v in range(V):
        node_info = input().split()
        for i in range(len(node_info)):
            if i == 1:
                continue
            node_info[i] = int(node_info[i])
        v_list[node_info[0]] = node_info[1:]
    visited = []
    inorder(1)
    ans = ''.join(visited)
    print("#%d %s" %(t, ans))