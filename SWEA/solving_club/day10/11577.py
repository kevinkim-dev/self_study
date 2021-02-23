#########################
#  SWEA number 11577
#  by 김승현                
#########################

# Q. 종이붙이기

# 길이 10 차이 갯수 + 길이 20차이 갯수 * 3

paper = [1, 3]

for t in range(1, int(input())+1):
    n = int(input())//10
    while len(paper) <= n:
        paper.append(paper[-1] + paper[-2]*2)
    print("#%d %d" %(t, paper[n-1]))