###########################
#  BaekJoon 1357번
#  by 김승현                
###########################

# Q. 뒤집힌 덧셈

def rev(x):
    return int(str(x)[::-1])

a, b = map(int, input().split())

print(rev(rev(a) + rev(b)))