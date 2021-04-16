###########################
#  BaekJoon 9095번
#  by 김승현                
###########################

# Q. 1, 2, 3 더하기

ways = [0, 1, 2, 4]
for _ in range(int(input())):
    N = int(input())
    while len(ways) < N + 1:
        ways.append(ways[-1] + ways[-2] + ways[-3])
    print(ways[N])
