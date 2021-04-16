def solution(n, z, roads, queries):
    sorted_roads = sorted(roads, key = lambda x : x[2])
    one_way = set()
    for road in sorted_roads:
        one_way.add(road[2])
    earn = [[[0, 0, 0]]]
    for x in range(1, z):
        q = []
        if x in one_way:
            while sorted_roads:
                road = sorted_roads.pop(0)
                if road[2] == x:
                    q.append(road[0:2] + [1])
                    break
                elif road[2] > x:
                    sorted_roads = road + sorted_roads
                    break
            earn.append(q)
        else:
            min_road = []
            min_dp = float('inf')
            for i in range(1, x):
                for road1 in earn[i]:
                    for road2 in earn[x-i]:
                        teleport = 2
                        if road1[0] == 0:
                            teleport -= 1
                        if road1[1] == road2[0]:
                            teleport -= 1
                        dp = road1[2] + road2[2] + teleport
                        if dp < min_dp:
                            min_dp = dp
                            min_road = [[0, road2[1], dp]]
                        elif dp == min_dp:
                            min_road.append([0, road2[1], dp])
            earn.append(min_road)
    earn.append([[0, 0, 1]])
    for i in range(1, z+1):
        if len(earn[-i]) == 0:
            break
    not_avail = z-i+2
    for _ in range(z-i+1):
        min_road = []
        min_dp = float('inf')
        x = len(earn)
        for i in range(1, x):
            for road1 in earn[i]:
                for road2 in earn[x-i]:
                    teleport = 2
                    if road1[0] == 0:
                        teleport -= 1
                    if road1[1] == road2[0]:
                        teleport -= 1
                    dp = road1[2] + road2[2] + teleport
                    if dp < min_dp:
                        min_dp = dp
                        min_road = [[0, road2[1], dp]]
                    elif dp == min_dp:
                        min_road.append([0, road2[1], dp])
        earn.append(min_road)
    answer = []
    for q in queries:
        stay = 0
        if q >= len(earn):
            stay += (q - not_avail) // z
            q -= stay*z
        if not earn[q]:
            answer.append(-1)
        else:
            answer.append(earn[q][0][2] + int(bool(earn[q][0][0])))
    return answer

n = int(input())
z = int(input())
roads = [list(map(int, input().split())) for _ in range(2)]
queries = list(map(int, input().split()))
print(solution(n, z, roads, queries))