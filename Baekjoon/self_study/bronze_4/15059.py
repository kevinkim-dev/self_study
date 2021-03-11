###########################
#  BaekJoon 15059번
#  by 김승현                
###########################

# Q. Hard choice

supply = list(map(int, input().split()))
need = list(map(int, input().split()))

ans = 0
for i in range(3):
    if need[i] > supply[i]:
        ans += need[i] - supply[i]

print(ans)