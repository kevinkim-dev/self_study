###########################
#  BaekJoon 2798번
#  by 김승현                
###########################

# Q. 블랙잭

n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x = num_list[i] + num_list[j] + num_list[k]
            if x > m:
                break
            ans = max(ans, x)

print(ans)