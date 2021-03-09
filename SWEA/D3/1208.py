#########################
#  SWEA number 1208
#  by 김승현                
#########################

# Q. Flatten

row = 100

def BubbleSort(box_state):
    for i in range(row-1, 0, -1):
        for j in range(i):
            if box_state[j] > box_state[j+1]:
                box_state[j], box_state[j+1] = box_state[j+1], box_state[j]
    return box_state

for t in range(1, 11):
    dump = int(input())
    box_state = BubbleSort(list(map(int, input().split())))
    
    for i in range(dump):
        box_state[-1] -= 1
        box_state[0] += 1
        if box_state[0] > box_state[1] or box_state[-1] < box_state[-2]:
            box_state = BubbleSort(box_state)
            
    ans = box_state[-1] - box_state[0]
    print("#%d %d" % (t, ans))
    
    
    
    
    # _sum = 0
    # for n in range(row):
    #     _sum += box_state[n]
    # avr = _sum // 100
    # remainder = _sum % 100


    
    
    
    
    
    
    
    
    
    
    
    
    
    

