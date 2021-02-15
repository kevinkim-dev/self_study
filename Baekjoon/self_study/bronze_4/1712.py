###########################
#  BaekJoon 1712번
#  by 김승현                
###########################

# Q. 손익분기점

# n개 팔았으면 
# 비용 = fixed + n*unfixed
# 수익 = sell*n
# fixed + n*unfixed < sell*n
# (sell-unfixed)*n > fiexed

fixed, unfiexd, sell = map(int, input().split())

if unfiexd >= sell:
    print(-1)
else:
    break_even = fixed / (sell - unfiexd)
    print(int(break_even)+1)