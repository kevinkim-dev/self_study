###########################
#  BaekJoon 1100번
#  by 김승현                
###########################

# Q. 하얀 칸

ans = 0

for i in range(8):
    row = input()
    for j in range(i%2, 8, 2):
        if row[j] == 'F':
            ans += 1

print(ans)