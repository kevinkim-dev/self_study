def solution(nums):
    answer = 0
    l = len(nums)
    prime = [1]*3000
    for i in range(2, 3000):
        if prime[i]:
            for j in range(2*i, 3000, i):
                prime[j] = 0
                
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if prime[nums[i] + nums[j] + nums[k]]:
                    answer += 1
                
    return answer