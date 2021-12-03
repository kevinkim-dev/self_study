###########################
#  BaekJoon 11866번
#  by 김승현                
###########################

# Q. 요세푸스 문제 0

N, K = map(int, input().split())

queue = list(range(1, N+1))
K -= 1

ans = []
idx = K
while len(queue) > 1:
    ans.append(str(queue.pop(idx)))
    idx = (idx + K) % len(queue)

ans.append(str(queue.pop()))

print('<' + ', '.join(ans) + '>')