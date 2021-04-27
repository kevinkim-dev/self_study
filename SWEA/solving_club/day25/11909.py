#########################
#  SWEA number 11909
#  by 김승현                
#########################

# Q. 트리 순회

def order(node):
    if node:
        preorder.append(node)
        order(tree[node][0])
        inorder.append(node)
        order(tree[node][1])
        postorder.append(node)
    return
 
 
for t in range(1, int(input())+1):
    V = int(input())
    nodes = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(V + 1)]
    for i in range(0, len(nodes), 2):
        if tree[nodes[i]][0]:
            tree[nodes[i]][1] = nodes[i + 1]
        else:
            tree[nodes[i]][0] = nodes[i + 1]
    preorder, inorder, postorder = [], [], []
    order(nodes[0])
    print('#%d\n%s\n%s\n%s' % (t, '-'.join(map(str, preorder)), '-'.join(map(str, inorder)), '-'.join(map(str, postorder))))