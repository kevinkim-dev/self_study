#########################
#  SWEA number 11572
#  by 김승현                
#########################

# Q. 괄호 검사 코드 제출 - 2가지 스택 구현

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
    
for t in range(1, int(input())+1):
    string = input()
    bracket = []
    flag = 1
    for char in string:
        if char == '(' or char == '{':
            push(bracket, char)
        elif char == '}':
            if pop(bracket) == '{':
                pass
            else:
                flag = 0
                break
        elif char == ')':
            if pop(bracket) == '(':
                pass
            else:
                flag = 0
                break
    if check_empty(bracket) == 0:
        flag = 0
    print("#%d 1" %t) if flag == 1 else print("#%d 0" %t)
