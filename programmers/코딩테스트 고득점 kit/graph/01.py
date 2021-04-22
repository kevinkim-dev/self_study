def solution(n, edge):
    visited = [0]*(n+1)
    go = [[] for _ in range(n+1)]
    for s, e in edge:
        go[s].append(e)
        go[e].append(s)
    q = [(1, 0)]
    while q:
        node, l = q.pop(0)
        for i in go[node]:
            if not visited[i]:
                visited[i] = l + 1
                q.append((i, l+1))
    visited[1] = 0
    answer = visited.count(max(visited))
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))