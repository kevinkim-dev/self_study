###########################
#  BaekJoon 2965번
#  by 김승현                
###########################

# Q. 캥거루 세마리

a, b, c = map(int, input().split())
print(max(b-a, c-b)-1)