#########################
#  SWEA number 5644
#  by 김승현                
#########################

# Q. 무선충전

dxy = [[0,0], [0, -1], [1, 0], [0, 1], [-1, 0]]

for t in range(1, int(input())+1):
    M, A = map(int, input().split())
    route_a = list(map(int, input().split())) + [0]
    route_b = list(map(int, input().split())) + [0]
    bc_list = [list(map(int, input().split())) for _ in range(A)]
    pos_a = [1, 1]
    pos_b = [10, 10]
    charge = 0
    for m in range(M+1):
        a_avail = []
        b_avail = []
        for i in range(A):
            if abs(pos_a[0]-bc_list[i][0])+abs(pos_a[1]-bc_list[i][1]) <= bc_list[i][2]:
                a_avail.append(bc_list[i]+[i+1])
            if abs(pos_b[0]-bc_list[i][0])+abs(pos_b[1]-bc_list[i][1]) <= bc_list[i][2]:
                b_avail.append(bc_list[i]+[i+1])
        a_avail = sorted(a_avail, key=lambda x: x[3], reverse=True) + [[0, 0, 0, 0, 0]]*2
        b_avail = sorted(b_avail, key=lambda x: x[3], reverse=True) + [[0, 0, 0, 0, 0]]*2
        if a_avail[0][4] == b_avail[0][4] and a_avail[0][3] != 0:
            charge += a_avail[0][3] + max(a_avail[1][3], b_avail[1][3])
        else:
            charge += a_avail[0][3] + b_avail[0][3]
        pos_a[0], pos_a[1] = pos_a[0]+dxy[route_a[m]][0], pos_a[1]+dxy[route_a[m]][1]
        pos_b[0], pos_b[1] = pos_b[0]+dxy[route_b[m]][0], pos_b[1]+dxy[route_b[m]][1]
    print("#%d %d" %(t, charge))
