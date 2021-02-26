#########################
#  SWEA number 1223
#  by 김승현  
#########################

# Q. 계산기2


def check_op(op):     
    if op ==  '+':
        while stack:
            new_string.append(stack.pop())
    else:
        while stack and stack[-1] == '*':
            new_string.append(stack.pop())
    stack.append(op)
    return

def calculate(new_string):
    for char in new_string:
        if type(char) is int:
            stack.append(char)
        elif char == '+':
            stack.append(stack.pop()+stack.pop())
        else :
            stack.append(stack.pop()*stack.pop())
    return

for t in range(1, 11):
    length = int(input())
    string = input()
    new_string = []
    stack = []
    for char in string:
        if char.isdigit():
            new_string.append(int(char))
        else:
            check_op(char)
    while stack:
        new_string.append(stack.pop())
    calculate(new_string)
    print("#%d %d" %(t, stack[0]))


# def check_op(op):
#     if op == '(':
#         pass        
#     elif op ==  '+' or char == '-' or char == '*' or char == '/':
#         while not check_pri(op, stack[-1]):
#             new_string.append(stack.pop())
#     else:
#         while stack[-1] != '(':
#             new_string.append(stack.pop())
#         stack.pop()
#     stack.append(char)
#     return