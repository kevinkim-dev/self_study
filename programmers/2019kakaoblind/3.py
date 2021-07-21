import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    
    def preorder(node):
        pre.append(node)
        for child in child_info[node]:
            if not child:
                continue
            preorder(child[0])
        return

    def postorder(node):
        for child in child_info[node]:
            if not child:
                continue
            postorder(child[0])
        post.append(node)
        return

    l = len(nodeinfo)
    child_info = [[0,0] for _ in range(l+1)]
    pre, post = [], []
    for i in range(l):
        nodeinfo[i] = [i+1, nodeinfo[i][0], nodeinfo[i][1]]
    nodeinfo.sort(key=lambda x: x[2], reverse=True)
    r_num, r_x, r_y = nodeinfo[0]
    for node in nodeinfo:
        node_num, x, y = node
        p_num, p_x, p_y = r_num, r_x, r_y
        if node_num == p_num:
            continue
        else:
            while True:
                if x > p_x:
                    if child_info[p_num][1]:
                        p_num, p_x, p_y = child_info[p_num][1]
                    else:
                        child_info[p_num][1] = (node_num, x, y)
                        break
                else:
                    if child_info[p_num][0]:
                        p_num, p_x, p_y = child_info[p_num][0]
                    else:
                        child_info[p_num][0] = (node_num, x, y)
                        break
    preorder(r_num)
    postorder(r_num)
    return [pre, post]

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

print(solution(nodeinfo))