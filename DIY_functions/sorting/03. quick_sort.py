import sys

sys.stdin = open('input.txt')
num_list = list(map(int, sys.stdin.readline().split()))
N = len(num_list)

# quick sort
def quick_sort(n_list):
    if len(n_list) <= 1:
        return n_list
    pivot = n_list[len(n_list)//2]
    small_list, big_list, equal_list = list(), list(), list()
    for n in n_list:
        if n < pivot:
            small_list.append(n)
        elif n > pivot:
            big_list.append(n)
        else:
            equal_list.append(n)
    return quick_sort(small_list) + equal_list + quick_sort(big_list)
print(quick_sort(num_list))


# 시간복잡도: 최악 O(n^2), 평균의 경우 O(nlogn)
# 공간복잡도: O(n)
# 안정정렬 여부: False