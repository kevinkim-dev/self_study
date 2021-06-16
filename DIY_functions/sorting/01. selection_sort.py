import sys

sys.stdin = open('input.txt')
num_list = list(map(int, sys.stdin.readline().split()))
N = len(num_list)

# selection sort
for i in range(N-1):
    min_num_idx = i
    for j in range(i+1, N):
        if num_list[min_num_idx] > num_list[j]:
            min_num_idx = j
    num_list[i], num_list[min_num_idx] = num_list[min_num_idx], num_list[i]
print(num_list)


# 시간복잡도: 최선, 평균, 최악 모두 O(n^2), bubble sort보단 조금 빠름
# 공간복잡도: O(n)
# 안정정렬 여부: False