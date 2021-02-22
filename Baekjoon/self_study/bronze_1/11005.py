###########################
#  BaekJoon 11005번
#  by 김승현                
###########################

# Q. 진법 변환 2

n, b = map(int, input().split())

trans = ''

while n > 0:
    left = n % b
    if left < 10:
        trans = str(left) + trans
    else:
        trans = chr(left+55) + trans
    n //= b
print(trans)