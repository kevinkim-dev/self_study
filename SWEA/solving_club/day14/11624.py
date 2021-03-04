#########################
#  SWEA number 11624
#  by 김승현                
#########################

# Q. 큐 코드 제출

def enQueue(x):
    global rear
    q.append(x)
    # rear += 1
    return

def deQueue():
    global front
    if isEmpty():
        print("Queue is Empty")
        return
    # front += 1
    return q[front]

def isEmpty():
    global rear, front
    return front == rear

for t in range(1, int(input())+1):
    q = []
    output = []
    front = -1
    rear = -1
    num_list = list(map(int, input().split()))
    for num in num_list:
        enQueue(num)
        rear += 1
    for n in q:
        output.append(deQueue())
    print("#%d " %t, end='')
    print(*output)