import sys

sys.stdin = open('input.txt')
num_list = list(map(int, sys.stdin.readline().split()))
N = len(num_list)

# insertion sort
for i in range(1, N):
    for j in range(i):
        if num_list[i-j] < num_list[i-j-1]:
            num_list[i-j], num_list[i-j-1] = num_list[i-j-1], num_list[i-j]

print(num_list)


# 시간복잡도: 평균, 최악 모두 O(n^2), 최선의 경우 O(n)
# 공간복잡도: O(n)
# 안정정렬 여부: True