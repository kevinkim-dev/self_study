#########################
#  SWEA number 1219
#  by 김승현                
#########################

# Q. 길찾기

def visit(s, t):
    if v_list1[s] == t or v_list2[s] == t:
        return 1
    elif v_list1[s] == -1 and v_list2[s] == -1:
        return 0
    else:
        return visit(v_list1[s], t) + visit(v_list2[s], t)

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
    print("#%d %d" %(t, bool(visit(0, 99))))