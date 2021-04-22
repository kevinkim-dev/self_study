def solution(n, lost, reserve):
    real_lost, real_reserve = [], []
    for i in range(len(lost)):
        if lost[i] not in reserve:
            real_lost.append(i)
    for i in range(len(reserve)):
        if reserve[i] not in lost:
            real_reserve.append(i)
    answer = n - len(real_lost)
    real_lost.sort()
    for l in real_lost:
        if l-1 in real_reserve:
            real_reserve.remove(l-1)
            answer += 1
        elif l+1 in real_reserve:
            real_reserve.remove(l+1)
            answer += 1
    return answer

n = 5
lost = [1, 2, 4]
reserve = [3, 4]
print(solution(n, lost, reserve))