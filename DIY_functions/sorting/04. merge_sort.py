import sys

sys.stdin = open('input.txt')
num_list = list(map(int, sys.stdin.readline().split()))
N = len(num_list)

# merge sort
def merge_sort(n_list):
    l = len(n_list)
    if l == 1:
        return n_list
    return merge(merge_sort(n_list[:l//2]), merge_sort(n_list[l//2:]))


def merge(l_arr, r_arr):
    l, r = len(l_arr), len(r_arr)
    i, j = 0, 0
    new_arr = list()
    while i < l and j < r:
        if l_arr[i] < r_arr[j]:
            new_arr.append(l_arr[i])
            i += 1
        else:
            new_arr.append(r_arr[j])
            j += 1
    if i == l:
        new_arr += r_arr[j:]
    else:
        new_arr += l_arr[i:]
    return new_arr

print(merge_sort(num_list))


# 시간복잡도: 최선, 평균, 최악의 경우 nlogn의 시간복잡도.
# 공간복잡도: O(n)
# 안정정렬 여부: True