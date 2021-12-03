###########################
#  BaekJoon 2745번
#  by 김승현                
###########################

# Q. 진법 변환

N, B = input().split()

B = int(B)

ans = 0

for i in range(len(N)):
    if N[-i-1].isalpha():
        ans += (ord(N[-i-1])-55)*B**i
    else:
        ans += int(N[-i-1])*B**i

print(ans)


