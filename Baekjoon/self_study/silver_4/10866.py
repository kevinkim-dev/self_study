###########################
#  BaekJoon 10866번
#  by 김승현                
###########################

# Q. 덱

deque = []
answer = []

for _ in range(int(input())):
    command_list = input().split()
    command = command_list[0]
    if command == 'front':
        answer.append(deque[0] if deque else -1)
    elif command == 'back':
        answer.append(deque[-1] if deque else -1)
    elif command == 'size':
        answer.append(len(deque))
    elif command == 'empty':
        answer.append(0 if deque else 1)
    elif command == 'push_front':
        deque = [command_list[1]] + deque
    elif command == 'push_back':
        deque += [command_list[1]]
    elif command == 'pop_front':
        if deque:
            answer.append(deque.pop(0))
        else:
            answer.append(-1)
    elif command == 'pop_back':
        if deque:
            answer.append(deque.pop())
        else:
            answer.append(-1)

for ans in answer:
    print(ans)

