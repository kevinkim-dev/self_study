#########################
#  Programmers problem kit 
#  summer 05월
#  by 김승현                
#########################

# Q. 4번

def solution(values, edges, queries):
    answers = []
    N = len(values)
    values = [0] + values
    root = [0]*(N+1)
    sum = values[:]
    leaf = [[] for _ in range(N+1)]
    for s, e in edges:
        root[e] = s
        leaf[s].append(e)
    temp_leaf = leaf[:]
    while temp_leaf.count(-1) < (N - 1):
        for i in range(1, N+1):
            if temp_leaf[i] == []:
                sum[root[i]] += sum[i]
                temp_leaf[root[i]].remove(i)
                temp_leaf[i] = -1
    # sum 완료
    for a, b in queries:
        if b == -1:
            answers.append(sum[a])
            continue
        while a != 1:
            dif = values[root[a]] - values[a]
            sum[a] += dif
            values[a] = values[root[a]]
            x = a
            while x != 1:
                x = root[x]
                sum[x] += dif
            a = root[a]
        sum[a] += b - values[a]
        values[a] = b
    return answers

values = [1,10,100,1000,10000]
edges = [[1,2],[1,3],[1,4],[2,5]]
queries = [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]
print(solution(values, edges, queries))