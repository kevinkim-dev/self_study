#########################
#  SWEA number 4789
#  by 김승현                
#########################

# Q. 성공적인 공연 기획

for t in range(1, int(input())+1):
    clap = []
    clap.extend(input())
    clap = list(map(int, clap))
    stand = list(range(len(clap)))
    for i in range(len(clap)-1):
        stand[i+1] -= sum(clap[:i+1]) 
    print("#%d %d" %(t, max(stand)))