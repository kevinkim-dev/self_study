###########################
#  BaekJoon 10569번
#  by 김승현                
###########################

# Q. 다면체 

for _ in range(int(input())):
    V, E = map(int, input().split())
    print(2-V+E)