def solution(A):
    num_set = set()
    for num in A:
        if num not in num_set:
            num_set.add(num)
        else:
            num_set.remove(num)
    return num_set.pop()

    # O(N) or O(N*log(N))