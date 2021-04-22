#########################
#  SWEA number 1486
#  by 김승현                
#########################

# Q. 장훈이의 높은 선반

def find_safe(idx, height):
    global min_height
    if height >= B:
        if height < min_height:
            min_height = height
        return
    if idx == N:
        return
    find_safe(idx+1, height)
    find_safe(idx+1, height + h_list[idx])
    return


for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    h_list = sorted(list(map(int, input().split())))
    min_height = 10000 * 21
    find_safe(0, 0)
    print("#%d %d" %(t, min_height - B))
