#########################
#  SWEA number 11605
#  by 김승현                
#########################

# Q. Forth 코드 제출

for t in range(1, int(input())+1):
    operator = input().split()
    stack = []
    for op in operator:
        if op.isdigit():
            stack.append(int(op))
        elif op == '.':
            break
        else:
            if len(stack) < 2:
                stack[0] = 'error'
                break
            elif op == '+':
                stack.append(stack.pop() + stack.pop())
            elif op == '-':
                stack.append(stack.pop() - stack.pop())
            elif op == '*':
                stack.append(stack.pop() * stack.pop())
            elif op == '/':
                stack.append(stack.pop() // stack.pop())
    print("#%d %s" %(t, str(stack[0])))

#  or not (type(stack[-1]) == int and type(stack[-2]) == int)