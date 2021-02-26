###########################
#  BaekJoon 17779번
#  by 김승현                
###########################

# Q. 게리맨더링 2

# 이중 배열은 총 두개 사용합니다
# 한 개는 각 구역의 선거인 수(input)이 담길 배열입니다
# 한 개는 조건을 만족하는 모든 x, y, d1, d2에 대해서 구역을 1~5로 나눈 배열입니다
 
# x, y, d1, d2에 대해 구역을 1~5로 나누는 함수
def area_divide(x, y, d1, d2):
    # 구역 1
    for i in range(1, x+d1+1):
        for j in range(1, y+1):
            A_area[i-1][j-1] = 1
    # 구역 2
    for i in range(1, x+d2+1):
        for j in range(y+1, N+1):
            A_area[i-1][j-1] = 2
    # 구역 3
    for i in range(x+d1, N+1):
        for j in range(1, y-d1+d2):
            A_area[i-1][j-1] = 3
    # 구역 4
    for i in range(x+d2+1, N+1):
        for j in range(y-d1+d2, N+1):
            A_area[i-1][j-1] = 4
    # 구역 5 (구역1~4를 미리 나눠놓고 위에 덮어 씌웁니다)
    for i in range(d1+d2+1):
        for j in range(-(d1-abs(i-d1)),d2+1-abs(i-d2)):
            A_area[x + i - 1][y + j - 1] = 5
    return

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
min_dif = float('inf')
# x는 1부터 N-2 까지입니다.
# x+d1+d2 <= N에서 d1, d2의 최소값이 1, 1이므로 N-2까지 가능합니다.
for x in range(1, N-1):
    # y는 2부터 N-1까지입니다
    # 1 <= y-d1에서 d1의 최소값이 1이므로 y의 최소값은 2이며
    # y+d2 <= N에서 d2의 최소값이 1이므로 y의 최대값은 N-1입니다
    for y in range(2, N):
        # d1는 1부터 y-1까지입니다
        # d1의 최소값은 1이며, 1 <= y - d1에서 d1의 최대값은 y-1입니다
        for d1 in range(1, y):
            # d2는 1부터 N-y까지입니다
            # d2의 최소값은 1이며 y + d2 <= N에서 d2의 최대값은 N-y입니다.
            for d2 in range(1, N-y+1):
                # 마지막으로 x + d1 + d2 <= N 조건을 따져주고
                # 맞지 않다면 IndexError가 발생하므로 밑의 코드를 스킵합니다
                if d1+d2 > N-x:
                    continue
                # 각 선거구의 총합이 들어갈 arr
                arr = [0]*5
                # 각 구역의 선거구에 대한 정보가 담길 이중배열
                A_area = [[0]*N for n in range(N)]
                # 이중배열에 선거구 분배
                area_divide(x, y, d1, d2)
                for i in range(N):
                    for j in range(N):
                        # 각 구역의 선거구에 해당하는 위치에 인원수를 더합니다
                        arr[A_area[i][j]-1] += A[i][j]
                # 최대값과 최소값의 차를 구해서
                # 현재까지의 차이의 최소값보다 작으면 갱신합니다
                dif = max(arr) - min(arr)
                if dif < min_dif:
                    min_dif = dif
print(min_dif)