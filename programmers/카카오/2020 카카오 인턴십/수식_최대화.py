#########################
#  Programmers problem
#  Kakao internship 2020
#  by 김승현                
#########################

# Q. 수식 최대화

def solution(expression):
    answer = 0
    queue = []
    operand = ('+', '-', '*')
    i = 0
    for j in range(len(expression)):
        if expression[j] not in operand:
            continue
        queue.append(expression[i:j])
        queue.append(expression[j])
        i = j + 1
    queue.append(expression[i:])
    operand_order = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    for order in operand_order:
        new_queue = queue[:]
        for op in order:
            stack = []
            while new_queue:
                x = new_queue.pop(0)
                if x == operand[op]:
                    stack.append(str(eval(stack.pop() + x + new_queue.pop(0))))
                else:
                    stack.append(x)
            new_queue = stack
        answer = max(abs(int(new_queue[0])), answer)    
    return answer


expression = "50*6-3*2"
print(solution(expression))