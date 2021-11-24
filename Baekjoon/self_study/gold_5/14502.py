#########################
#  SWEA number 14502
#  by 김승현                
#########################

# Q. 연구소

import copy

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs():
    t_lab = copy.deepcopy(lab)
    for vr, vc in virus:
        q = [(vr, vc)]
        while q:
            r, c = q.pop()
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not t_lab[nr][nc]:
                    t_lab[nr][nc] = 2
                    q.append((nr, nc))
    tmp = 0
    for r in range(R):
        for c in range(C):
            if t_lab[r][c]:
                continue
            tmp += 1
    return tmp


R, C = map(int, input().split())

lab = []
virus = []
for r in range(R):
    lab_row = list(map(int, input().split()))
    for c in range(C):
        if lab_row[c] == 2:
            virus.append((r, c))
    lab.append(lab_row)

ans = 0

for i in range(R*C-2):
    ir, ic = i//C, i%C
    if lab[ir][ic]:
        continue
    for j in range(i+1, R*C-1):
        jr, jc = j//C, j%C
        if lab[jr][jc]:
            continue
        for k in range(j+1, R*C):
            kr, kc = k//C, k%C
            if lab[kr][kc]:
                continue
            lab[ir][ic], lab[jr][jc], lab[kr][kc] = 1, 1, 1
            ans = max(dfs(), ans)
            lab[ir][ic], lab[jr][jc], lab[kr][kc] = 0, 0, 0

print(ans)

