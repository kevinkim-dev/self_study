import sys

sys.stdin = open('input.txt')
num_list = list(map(int, sys.stdin.readline().split()))
N = len(num_list)

# bubble sort
for i in range(N-1, -1, -1):
    for j in range(i):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
print(num_list)


# 시간복잡도: 최선, 평균, 최악 모두 O(n^2)
# 공간복잡도: O(n)
# 안정정렬 여부: True