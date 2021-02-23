#########################
#  SWEA number 1219
#  by 김승현                
#########################

# Q. 길찾기

# 1. 갈림길에선 반대편 길을 stack에 쌓는다
# 2. 길이 없으면 stack으로
# 3. 99돌아가면 break

def push(x):
    stack.append(x)
    return

def pop():
    if len(stack):
        x = stack[-1]
        stack.remove(stack[-1])
        return x
    else:
        return 0


for _ in range(10):
    t, vertex = map(int, input().split())
    v_all = list(map(int, input().split()))
    v_list1 = [-1]*100
    v_list2 = [-1]*100
    for v in range(0, 2*vertex, 2):
        if v_list1[v_all[v]] == -1:
            v_list1[v_all[v]] = v_all[v+1]
        else:
            v_list2[v_all[v]] = v_all[v+1]
    stack = [0]
    flag = 0
    while stack:
        x = pop()
        if v_list1[x] == 99:
            flag = 1
            break
        elif v_list1[x] != -1:
            push(v_list1[x])
            v_list1[x] = -1
        if v_list2[x] == 99:
            flag = 1
            break
        if v_list2[x] != -1:
            push(v_list2[x])
            v_list2[x] = -1
    print("#%d %d" %(t, flag))
        
        
        
    