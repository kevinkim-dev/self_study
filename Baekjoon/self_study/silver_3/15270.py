###########################
#  BaekJoon 15270번
#  by 김승현                
###########################

# Q. 친구 팰린드롬

def make_friend(idx, cnt):
    global ans
    if idx == M:
        if cnt == N:
            ans = N
        else:
            ans = max(ans, cnt+1) 
        return
    make_friend(idx+1, cnt)

    # 선택 함
    a, b = friends[idx]
    if not visited[a] and not visited[b]:
        visited[a] = 1
        visited[b] = 1
        make_friend(idx+1, cnt + 2)
        visited[a] = 0
        visited[b] = 0
    return

        

N, M = map(int, input().split())

friends = []

for _ in range(M):
    friends.append(list(map(int, input().split())))

visited = [0]*(N+1)
ans = 1
if M:
    make_friend(0, 0)

print(ans)