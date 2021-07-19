###########################
#  BaekJoon 2669번
#  by 김승현                
###########################

# Q. 직사각형 네개의 합집합의 면적 구하기

visited = [0]*10000

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2)-1, max(x1, x2)-1):
        for y in range(min(y1, y2)-1, max(y1, y2)-1):
            if not visited[x + y*100]:
                visited[x + y*100] = 1
print(sum(visited))

