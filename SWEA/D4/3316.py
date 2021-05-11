#########################
#  SWEA number 3316
#  by 김승현                
#########################

# Q. 동아리실 관리하기

for t in range(1, int(input())+1):
    big = 1000000007
    totem_list = list(input())
    day = len(totem_list)
    situation = [[0]*16 for _ in range(len(totem_list))]
    for n in range(1, 16):
        if n & 1 and n & (1 << (ord(totem_list[0]) - 65)):
            situation[0][n] = 1
    for i in range(day-1):
        totem = totem_list[i+1]
        for j in range(1, 16):
            for k in range(1, 16):
                if k & (1 << (ord(totem) - 65)) and k & j:
                    situation[i+1][k] = (situation[i+1][k] + situation[i][j]) % big
    print("#%d %d" %(t, sum(situation[-1]) % big))

