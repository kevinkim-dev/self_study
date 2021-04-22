def solution(N, number):
    D = [set() for _ in range(9)]
    D[1] = {N}
    idx = 2
    print(D[1])
    while idx < 9:
        for i in range(1, idx//2 + 1):
            j = idx - i
            for num1 in D[i]:
                for num2 in D[j]:
                    D[idx].add(num1 + num2)
                    D[idx].add(num2 + num1)
                    D[idx].add(num1 - num2)
                    D[idx].add(num2 - num1)
                    D[idx].add(num1 * num2)
                    if num1 != 0:
                        D[idx].add(num2 // num1)
                    if num2 != 0:
                        D[idx].add(num1 // num2)
        D[idx].add(int(str(N)*idx))
        if number in D[idx]:
            return idx
        print(D[idx])
        idx += 1
    return -1

N = 5
number = 12
print(solution(N, number))