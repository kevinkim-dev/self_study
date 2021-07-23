#########################
#  SWEA number 2234
#  by 김승현                
#########################

# Q. 성곽

# 8 남 / 4 동 / 2 북 / 1 서
# 1. 
# 2. 
# 3. 



# def wall(n):
#     pass

# 방이 연결되어있는지 확인
# 1. 해당 방과 인접한 방의 번호를 2진수로 바꾼다.
# 2. 인접한 방의 번호의 앞 두개와 뒷 두개를 바꾼다.
# 3. 인접한 방의 방향의 index의 비트가 0인지 확인 -> 맞으면 뚫린거니까 q에 넣구

#     북
#   서방동
#     남

# 남 동 북 서
# 1  0  1  1  11
# 1  0  0  1   6
# 1  0  1  1

# 8 남 / 4 동 / 2 북 / 1 서

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(row, col, room_num):
    q = [(row, col)]
    room_nums[row][col] = room_num
    while q:
        r, c = q.pop()
        if visited[r][c]:
            continue
        visited[r][c] = 1
        now = bin(rooms[r][c])[2:].zfill(4)
        for i in range(4):
            nr, nc = r + dxy[i][0], c + dxy[i][1]
            if 0 <= nr <= m-1 and 0 <= nc <= n-1 and not visited[nr][nc] and now[i] == '0' and bin(rooms[nr][nc])[2:].zfill(4)[(i+2)%4] == '0':
                q.append((nr, nc))
                room_nums[nr][nc] = room_num
    return

n, m = map(int, input().split())

rooms = list()
for i in range(m):
    rooms.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(m)]
room_nums = [[0]*n for _ in range(m)]

room_num = 0
for i in range(m):
    for j in range(n):
        if visited[i][j]:
            continue
        bfs(i,j, room_num)
        room_num += 1

room_numbers = [0]*room_num
near_room = [set() for _ in range(room_num)]

for r in range(m):
    for c in range(n):
        room_numbers[room_nums[r][c]] += 1
        for d in dxy:
            nr, nc = r +d[0], c + d[1]
            if 0 <= nr <= m-1 and 0 <= nc <= n-1 and room_nums[r][c] != room_nums[nr][nc]:
                near_room[room_nums[r][c]].add(room_nums[nr][nc])

max_cnt = 0
for i in range(room_num):
    for j in near_room[i]:
        if max_cnt < room_numbers[i] + room_numbers[j]:
            max_cnt = room_numbers[i] + room_numbers[j]

print(room_num)
print(max(room_numbers))
print(max_cnt)






# for i in range(len(board)):
#     print(board[i])
# board = [[0]*n*3 for _ in range(m*3)]