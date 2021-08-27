def solution(a):
    answer = []
    for s in a:
        flag = 1
        while len(s) >= 2:
            if s[0] == 'a' or s[-1] == 'a':
                s = s.strip('a')
            else:
                sc = s.count('a')
                if not sc:
                    flag = 0
                    break
                else:
                    lb, rb = len(s.split('a', 1)[0]) // sc, len(s[::-1].split('a', 1)[0]) // sc
                    if not lb or not rb:
                        flag = 0
                        break
                    else:
                        x = min(lb, rb)
                        s = s[x*sc:-x*sc]
                    
        if s == 'b':
            flag = 0
        if flag:
            answer.append(True)
        else:
            answer.append(False)
    return answer