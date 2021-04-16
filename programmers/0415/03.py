def solution(a, edges):
    N = len(a)
    if sum(a) != 0:
        return -1
    edge_list = [[] for _ in range(N)]
    edge_num_list = list(range(N))
    for edge in edges:
        edge_list[edge[0]].append(edge[1])
        edge_list[edge[1]].append(edge[0])
    for i in range(N):
        if len(edge_list[i]) == 1:
            root = i
            break
    tree = [[root]]
    q, visited = [root], [root]
    while q:
        l = len(q)
        floor = []
        for _ in range(l):
            node = q.pop(0)
            for leaf in edge_list[node]:
                if leaf not in visited:
                    floor.append(leaf)
                    q.append(leaf)
                    visited.append(leaf)
        if floor:
            tree.append(floor)
    answer = 0
    while len(tree) > 1:
        leaves = tree.pop()
        for leaf in leaves:
                parent = edge_list[leaf][0]
                answer += abs(a[leaf])
                a[parent] += a[leaf]
                a[leaf] = 0
                edge_list[leaf].pop()
                edge_list[parent].remove(leaf)
                edge_num_list.remove(leaf)
    return answer

a = list(map(int, input().split()))
edges = []
for i in range(6):
    edges.append(list(map(int, input().split())))
print(solution(a, edges))


    # answer = 0
    # for _ in range(5):
    #     for i in edge_num_list:
    #         if len(edge_list[i]) == 1:
    #             j = edge_list[i][0]
    #             answer += abs(a[i])
    #             a[j] += a[i]
    #             a[i] = 0
    #             edge_list[i].pop()
    #             edge_list[j].remove(i)
    #             edge_num_list.remove(i)
    #             break
    # return answer