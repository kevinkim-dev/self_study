def solution(d, budget):
    answer = 0
    for price in sorted(d):
        if budget < price:
            break
        answer += 1
        budget -= price
        
    return answer