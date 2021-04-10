#########################
#  SWEA number 11758
#  by 김승현                
#########################

# Q. 이진 힙

def insert(node, idx):
    tree[idx] = node
    while tree[idx//2] > node and idx != 1:
        tree[idx//2], tree[idx] =  tree[idx], tree[idx//2]
        idx //= 2
    return


for t in range(1, int(input())+1):
    N = int(input())
    node_list = list(map(int, input().split()))
    tree = [0]*(N+1)
    for i in range(N):
        insert(node_list[i], i+1)
    ans = 0
    while N != 1:
        ans += tree[N//2]
        N //= 2
    print("#%d %d" %(t, ans))