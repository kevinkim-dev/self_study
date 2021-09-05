###########################
#  Kakao blind 2020 
#  Level3_기둥과 보설치
#  by 김승현                
###########################

def solution(n, build_frame):

    def build_row(x, y):
        # 바로밑에, 혹은 오른쪽 아래에 col이 있는 경우
        if [x, y-1, 0] in built or [x+1, y-1, 0] in built:
            built.append([x, y, 1]) 
        # 좌 우에 row가 있는 경우
        elif ([x-1, y, 1] in built and [x+1, y, 1] in built):
            built.append([x, y, 1]) 
        return

    def build_col(x, y):
        # 바닥이거나, 그자리에 혹은 왼쪽에 row가 있거나 밑에 col이 있는 경우
        if y == 0 or [x, y, 1] in built or [x-1, y, 1] in built or [x, y-1, 0] in built:
            built.append([x, y, 0]) 
        return

    def boom_row(x, y):
        # 내 위의 기둥이 내가 사라지면 못버티는 경우
        if ([x, y, 0] in built and [x, y-1, 0] not in built and [x-1, y, 1] not in built) or ([x+1, y, 0] in built and [x+1, y-1, 0] not in built and [x+1, y, 1] not in built):
            return
        # 내 왼쪽에 row가 있는데 양쪽 row로 버티고 있는 경우
        elif [x-1, y, 1] in built and [x-1, y-1, 0] not in built and [x, y-1, 0] not in built:
            return
        # 내 오른쪽에 row가 있는데 양쪽 row로 버티고 있는 경우
        elif [x+1, y, 1] in built and [x+1, y-1, 0] not in built and [x+2, y-1, 0] not in built:
            return
        built.remove([x, y, 1])
        return

    def boom_col(x, y):
        # 내 왼쪽 위에 row가 있는데 버티지 못하면
        if ([x-1, y+1, 1] in built and [x-1, y, 0] not in built and ([x-2, y+1, 1] not in built or [x, y+1, 1] not in built)):
            return
        # 내 오른쪽 위에 row가 있는데 버티지 못하면
        elif ([x, y+1, 1] in built and [x+1, y, 0] not in built and ([x-1, y+1, 1] not in built or [x+1, y+1, 1] not in built)):
            return
        # 내 위에 col이 있는데 버티지 못하면
        elif ([x, y+1, 0] in built and [x, y+1, 1] not in built and [x-1, y+1, 1] not in built):
            return
        built.remove([x, y, 0])
        return

    built = []
    for work in build_frame:
        if work[-1]:
            if work[-2]:
                build_row(work[0], work[1])
            else:
                build_col(work[0], work[1])
        else:
            if work[-2]:
                boom_row(work[0], work[1])
            else:
                boom_col(work[0], work[1])
    built.sort(key=lambda x: (x[0], x[1], x[2]))
    return built



n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))