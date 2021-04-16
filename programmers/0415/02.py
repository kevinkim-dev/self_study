def push(stk, item):
    stk.append(item)

def pop(stk):
    if len(stk) == 0:
        return
    else:
        return stk.pop(-1)

def check_empty(stk):
    if len(stk) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    l = len(s)
    open = ['(', '{', '[']
    close = [')', '}', ']']
    for i in range(l):
        if s[i] not in open + close:
            return 0
    for n in range(l):
        string = s[n:] + s[:n]
        flag = 1
        stack = []
        for i in range(l):
            if string[i] in open:
                push(stack, string[i])
            elif string[i] == ')':
                if pop(stack) == '(':
                    pass
                else:
                    flag = 0
                    break
            elif string[i] == '}':
                if pop(stack) == '{':
                    pass
                else:
                    flag = 0
                    break
            elif string[i] == ']':
                if pop(stack) == '[':
                    pass
                else:
                    flag = 0
                    break
        if flag and not stack:
            answer += 1      
    return answer






def solution(s):
    answer = 0
    l = len(s)
    open = ['(', '{', '[']
    close = [')', '}', ']']
    for i in range(l):
        if s[i] not in open + close:
            return 0
    for n in range(l):
        string = s[n:] + s[:n]
        stack = []
        for i in range(l):
            flag = 1
            if string[i] in open:
                stack.append(string[i])
            else:
                if stack:
                    top = stack.pop()
                    if open.index(top) != close.index(string[i]):
                        flag = 0
                        break
                else:
                    flag = 0
                    break
        if flag:
            answer += 1      
    return answer