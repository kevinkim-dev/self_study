#########################
#  SWEA number 2805
#  by 김승현                
#########################

# Q. 농작물 수확하기

for t in range(1, int(input())+1):
    N = int(input())
    sell = 0
    for n in range(N):
        grow = input()
        for crop in grow[N//2-(N//2-abs(N//2-n)):N//2+1+(N//2-abs(N//2-n))]:
            sell += int(crop)
    print("#%d %d" %(t, sell))