#########################
#  SWEA number 11945
#  by 김승현                
#########################

# Q. 그룹 나누기

def find_team(x):
    for node in adj_list[x]:
        if not team[node]:
            team[node] = team_num
            find_team(node)
    return

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    vote = list(map(int, input().split()))
    adj_list = [[] for n in range(N+1)]
    for v in range(M):
        s, e = vote[v*2], vote[v*2+1]
        adj_list[s].append(e)
        adj_list[e].append(s)
    team = [0]*(N+1)
    team_num = 1
    for i in range(1, N+1):
        if not team[i]:
            team[i] = team_num
            find_team(i)
            team_num += 1
    ans = max(team)
    print("#%d %d" %(t, ans))