#########################
#  SWEA number 5648
#  by 김승현                
#########################

# Q. 원자 소멸 시뮬레이션 미완료!

# 같은 방향끼린 안부딪힘
# 반대 방향끼린 0.5단위로 부딪힘
# 아예 좌표평면을 만들자!

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

global atom_map, atom_list
atom_map = [[0]*4001 for _ in range(4001)]
atom_list = [0]*1001

for t in range(1, int(input())+1):
    N = int(input())
    # atom_map = [[0]*4001 for _ in range(4001)]
    # atom_list = [[0, 0, 0, 0, 0]]
    for i in range(1, N+1):
        atom = list(map(int, input().split()))
        atom[0], atom[1] = (-atom[1]+1000)*2, (atom[0]+1000)*2
        atom_list[i] = atom+[1]
        atom_map[atom[0]][atom[1]] = i
    cnt = 0
    energy = 0
    while cnt < N:
        # for a in range(13):
        #     print(''.join(map(str, atom_map[a])))
        # print()
        colide_loc = []
        for i in range(1, N+1):
            if atom_list[i][4]:
                at = atom_list[i]
                atom_map[at[0]][at[1]] = 0
                d_r = at[0] + dxy[at[2]][0]
                d_c = at[1] + dxy[at[2]][1]
                if not 0 <= d_r <= 4000 or not 0 <= d_c <= 4000:
                    cnt += 1
                    atom_list[i][4] = 0
                elif atom_map[d_r][d_c] == 0:
                    if (d_r, d_c) in colide_loc:
                        energy += at[3]
                        atom_list[i][4] = 0
                        cnt += 1
                    else:
                        atom_map[d_r][d_c] = i
                        atom_list[i][0], atom_list[i][1] = d_r, d_c
                else:
                    energy += at[3] + atom_list[atom_map[d_r][d_c]][3]
                    atom_list[atom_map[d_r][d_c]][4] = 0
                    atom_map[d_r][d_c] = 0
                    colide_loc.append((d_r, d_c))
                    atom_list[i][4] = 0
                    cnt += 2
    print("#%d %d" %(t, energy))

# dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# for t in range(1, int(input())+1):
#     N = int(input())
#     atom_map = [[0]*4001 for _ in range(4001)]
#     atom_list = [[0, 0]]
#     for i in range(1, N+1):
#         atom = list(map(int, input().split()))
#         atom_list.append(atom[2:])
#         atom_map[(atom[0]+1000)*2][(atom[1]+1000)*2] = i
#         print((atom[0]+1000)*2, (atom[1]+1000)*2)
#     cnt = 0
#     energy = 0
#     while cnt < N:
#         colide_loc = []
#         for r in range(4001):
#             for c in range(4001):
#                 at = atom_map[r][c]
#                 if at != 0:
#                     atom_map[r][c] = 0
#                     d_r = r + dxy[atom_list[at][0]][0]
#                     d_c = c + dxy[atom_list[at][0]][1]
#                     if not 0 <= d_r <= 4000 or not 0 <= d_c <= 4000:
#                         cnt += 1
#                     elif atom_map[d_r][d_c] == 0:
#                         if (d_r, d_c) in colide_loc:
#                             energy += atom_list[at][1]
#                             cnt += 1
#                         else:
#                             atom_map[d_r][d_c] = at
#                     else:
#                         energy += atom_list[at][1] + atom_list[atom_map[d_r][d_c]][1]
#                         atom_map[d_r][d_c] = 0
#                         colide_loc.append((d_r, d_c))
#                         cnt += 2
#     print("#%d %d" %(t, energy))

# 같은 방향끼린 안부딪힘
# 반대 방향끼린 0.5단위로 부딪힘
# 더느림! 샹...^^%
# dxy = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]

# for t in range(1, int(input())+1):
#     N = int(input())
#     atom_list = [[] for _ in range(4)]
#     energy = 0
#     for _ in range(N):
#         atom = list(map(int, input().split()))
#         atom_list[atom[2]].append(atom[0:2] + [atom[3]]) 
#     flag = 0
#     while atom_list[0] or atom_list[1] or atom_list[2] or atom_list[3]:
#         colide = [[] for _ in range(4)]
#         for i in range(4):
#             for j in range(len(atom_list[i])):
#                 atom_list[i][j][0] += dxy[i][0]
#                 atom_list[i][j][1] += dxy[i][1]
#         if flag:
#             for i in range(4):
#                 for j in range(4):
#                     if i != j:
#                         for ii in range(len(atom_list[i])):
#                             for jatom in atom_list[j]:
#                                 if atom_list[i][ii][0:2] == jatom[0:2]:
#                                     colide[i].append(ii)
#         else:
#             for i in [0, 2]:
#                 for ii in range(len(atom_list[i])):
#                     for jatom in atom_list[i+1]:
#                         if atom_list[ii][0:2] == jatom[0:2]:
#                             energy += atom_list[ii][2]
#                             colide[i].append(ii)
#         for i in range(4):
#             for j in range(len(atom_list[i])-1, -1, -1):
#                 if not -1000 <= atom_list[i][j][0] <= 1000 or not -1000 <= atom_list[i][j][1] <= 1000:
#                     del atom_list[i][j]
#                 elif j in colide[i]:
#                     energy += atom_list[i][j][2]
#         flag = (flag+1)%2
#     print("#%d %d" %(t, energy))

# dxy = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]

# for t in range(1, int(input())+1):
#     N = int(input())
#     atom_list = [list(map(int, input().split())) for _ in range(N)]
#     energy = 0
#     while atom_list:
#         loc_info = []
#         collide = set()
#         for i in range(len(atom_list)):
#             atom_list[i][0] += dxy[atom_list[i][2]][0]
#             atom_list[i][1] += dxy[atom_list[i][2]][1]
#             for j in range(i-1):
#                 if ((atom_list[i][0], atom_list[i][1])) == (atom_list[j][0], atom_list[j][1]):
#                     collide.add(i)
#                     collide.add(j)
#         for k in sorted(list(collide), reverse=True):
#             energy += atom_list[k][3]
#             del atom_list[k]
#         for l in range(len(atom_list)):
#             atom = atom_list.pop(0)
#             if -1000 <= atom[0] <= 1000 and -1000 <= atom[1] <= 1000:
#                 atom_list.append(atom)
#     print("#%d %d" %(t, energy))
