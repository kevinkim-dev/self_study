#########################
#  SWEA number 11749
#  by 김승현                
#########################

# Q. Tree 8일차 - 이진탐색

def insert(n, i):
    # 왼쪽으로 내려갈 수 있으면서 비어있는 경우
    if i * 2 <= N and not node_list[i * 2]:
        node_list[i * 2] = n
        return insert(n, i * 2)
    # 오른쪽으로 내려갈 수 있으면서 비어있는 경우
    elif i * 2 + 1 <= N and not node_list[i * 2 + 1]:
        node_list[i * 2 + 1] = n
        return insert(n, i * 2 + 1)
    # 밑에 두개 다 꽉참 -> 위로 올라가야 하는 경우
    else:
        if n == node_list[i]:
            return i
        if i % 2 != 0:
            return insert(n, i // 2)
        else:
            i //= 2
            node_list[i] = n
    return i
            

for t in range(1, int(input())+1):
    N = int(input())
    node_list = [0]*(N+1)
    x = 1
    for n in range(1, N+1):
        x = insert(n, x)
    print("#%d %d %d" %(t, node_list[1], node_list[N//2]))