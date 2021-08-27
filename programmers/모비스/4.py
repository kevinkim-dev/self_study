from itertools import combinations

def solution(p, q):
    answer = []
    for i in range(len(p)):
        x = sorted(p[i])
        y = q[i]
        for j in range(len(x)-1, -1, -1):
            num = x[j]
            if num in y:
                x.remove(num)
                y.remove(num)
        sum_cnt = len(x) - len(y)
        w_flag = 1
        while x:
            flag = 0
            for i in range(2, sum_cnt + 2):
                for com in list(combinations(list(range(len(x))), i)):
                    _sum = 0
                    for c in com:
                        _sum += x[c]
                    if _sum not in y:
                        continue
                    y.remove(_sum)
                    for c in com[::-1]:
                        x.remove(x[c])
                    flag = 1
                    break
                if flag:
                    break
            if not flag:
                w_flag = 0
                break
        if w_flag:
            answer.append(True)
        else:
            answer.append(False) 
    return answer



p = [[10, 11, 12, 13]]
q = [[11, 10, 10, 12]]
print(solution(p, q))