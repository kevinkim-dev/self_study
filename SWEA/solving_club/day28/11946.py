#########################
#  SWEA number 11946
#  by 김승현                
#########################

# Q. 그룹 나누기

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x
 
 
def kruskal():
    cnt = 0
    for s, e, w in edges:
        rs, re = find_set(s), find_set(e)
        if rs != re:
            cnt += w
            p[re] = rs
    return cnt
 
 
for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges = sorted(edges, key = lambda x: x[2])
    p = [i for i in range(V + 1)]
    print('#%d %d' % (t, kruskal()))