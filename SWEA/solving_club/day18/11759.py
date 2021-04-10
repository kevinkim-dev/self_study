#########################
#  SWEA number 11759
#  by 김승현                
#########################

# Q. 노드의 합

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        idx, node = map(int, input().split())
        tree[idx] = node
    for i in range(N-M, 0, -1):
        tree[i] = tree[i*2] 
        if i * 2 + 1 <= N:
            tree[i] += tree[i*2 + 1]
    print("#%d %d" %(t, tree[L]))