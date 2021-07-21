def solution(nodeinfo):
    
    def recursion(node):
        pass
    
    answer = [[]]
    node_dic = dict()
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        if y in node_dic.keys():
            node_dic[y].append(x)
        else:
            node_dic[y] = [x]
        nodeinfo[i] = [i+1, nodeinfo[i]]
    nodeinfo.sort(key=lambda x: (x[1][1], -x[1][0]), reverse=True)
    root = nodeinfo[0][0]
    print(node_dic)
    # for i in range(len(nodeinfo)):
        
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

solution(nodeinfo)