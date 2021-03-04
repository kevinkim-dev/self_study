#########################
#  SWEA number 1258
#  by 김승현                
#########################

# Q. 행렬찾기

# for t in range(1, int(input())+1):
#     N = int(input())
#     dan = [list(input().split()) for n in range(N)]
    
#     danger = [0]*(N+1)
#     danger_size = []
#     print(dan_box)
    #     for bottle in row:
    #         if bottle:
    #             danger[len(bottle)] += 1
    # for i in range(N+1):
    #     if danger[i]:
    #         danger_size.append([i, danger[i], i*danger[i]])
    # for i in range(len(danger_size)-1, -1, -1):
    #     for j in range(i):
    #         if danger_size[j][2] > danger_size[j+1][2]:
    #             danger_size[j], danger_size[j+1] = danger_size[j+1], danger_size[j]
    # print("#%d %d" %(t, len(danger_size)), end=' ')
    # for dangers in danger_size:
    #     print("%d %d" %(dangers[1], dangers[0]), end=' ')
    # print()
        
for t in range(1, int(input())+1):
    N = int(input())
    danger = [0]*(N+1)
    danger_size = []
    for r in range(N):
        row = ''.join(list(input().split())).split('0')
        for bottle in row:
            if bottle:
                danger[len(bottle)] += 1
    for i in range(N+1):
        if danger[i]:
            danger_size.append([i, danger[i], i*danger[i]])
    danger_size = sorted(sorted(danger_size, key=lambda x: x[1]), key=lambda x: x[2])
    print("#%d %d %s" %(t, len(danger_size), ' '.join(' '.join(map(str, dan[1::-1])) for dan in danger_size)))
                

