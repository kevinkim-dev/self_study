#########################
#  SWEA number 4366
#  by 김승현                
#########################

# Q. 정식이의 은행업무

def find_bi(x):
    for i in range(len(x)):
        x[i] = int(not x[i])
        bi_pro.append(int(''.join(list(map(str, x))), 2))
        x[i] = int(not x[i])
    return


def find_tri(x):
    bit = [0, 1, 2]
    for i in range(len(x)):
        base = x[i]
        bit.remove(base)
        for b in bit:
            x[i] = b
            tri_pro.append(int(''.join(list(map(str, x))), 3))
        bit.append(base)
        x[i] = base
    return

for t in range(1, int(input())+1):
    bi_num = list(map(int, list(input())))
    tri_num = list(map(int, list(input())))
    bi_pro, tri_pro = [], []
    find_bi(bi_num)
    find_tri(tri_num)
    for bi in bi_pro:
        if bi in tri_pro:
            ans = bi
            break
    print("#%d %d" %(t, ans))
