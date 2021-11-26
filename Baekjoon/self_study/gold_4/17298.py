#########################
#  SWEA number 17298
#  by 김승현                
#########################

# Q. 오큰수

def find_oken():
    while prev:
        if prev[-1] > num:
            return prev[-1]
        prev.pop()
    return -1

N = int(input())

num_list = list(map(int, input().split()))

ans, prev = [], []
for _ in range(N):
    num = num_list.pop()
    ans.append(str(find_oken()))
    prev.append(num)

print(' '.join(ans[::-1]))