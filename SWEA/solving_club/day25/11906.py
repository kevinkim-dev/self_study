#########################
#  SWEA number 11906
#  by 김승현                
#########################

# Q. 퀵 정렬


def quick_sort(A):
    if len(A) in (0, 1):
        return A
    p = i = 0
    for j in range(1, len(A)):
        if A[j] < A[p]:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
    A[i], A[p] = A[p], A[i]
    return quick_sort(A[:i]) + [A[i]] + quick_sort(A[i+1:])


for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()[:N]))
    num_list = quick_sort(num_list)
    print("#%d %d" %(t, num_list[N//2]))