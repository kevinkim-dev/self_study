def solution(N, stages):
    answer = []
    stage = [0]*(N+2)
    for st in stages:
        stage[st] += 1
    done_stage = stage[:]
    for i in range(N+1, 0, -1):
        done_stage[i-1] += done_stage[i]
    prob = []
    for i in range(1, N+1):
        p = 0
        if done_stage[i] != 0:
            p = stage[i] / done_stage[i]
        prob.append((i, p))
    prob.sort(key=lambda x: x[1], reverse=True)
    for x, y in prob:
        answer.append(x)
    return answer