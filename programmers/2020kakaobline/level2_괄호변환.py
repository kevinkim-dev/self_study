###########################
#  Kakao blind 2020 
#  Level2_괄호변환
#  by 김승현                
###########################

def solution(p):

    def check(st):
        stack = []
        for s in st:
            if s == '(':
                stack.append(s)
            elif not stack:
                return False
            else:
                stack.pop()
        return True

    def divide(st):
        if not st:
            return ''
        q = [0, 0]
        for s in st:
            if s == '(':
                q[0] += 1
            else:
                q[1] += 1
            if q[0] == q[1]:
                break
        u, v = st[:q[0] + q[1]], st[q[0] + q[1]:]
        if check(u):
            return u + divide(v)
        if not check(u):
            u = u[1:-1]
            nu = ''
            for c in u:
                if c == '(':
                    nu += ')'
                else:
                    nu += '('
            return '(' + divide(v) + ')' + nu
    
    if not check(p):
        return divide(p)
    return p

p = "()))((()"
print(solution(p))