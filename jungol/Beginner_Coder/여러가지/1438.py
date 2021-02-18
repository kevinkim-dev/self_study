#########################
#  Jungol number 1438
#  by 김승현                
#########################

# Q. 색종이(초)

paper = [0]*100
for n in range(100):
    paper[n] = [0]*100

area = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if paper[i][j] == 0:
                paper[i][j] += 1
                area += 1

print(area)
