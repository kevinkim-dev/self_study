###########################
#  BaekJoon 11025번
#  by 김승현                
###########################

# Q. 요세푸스 문제 3

N, K = map(int, input().split())
people = list(range(1, N+1))
while len(people) > 1:
    for _ in range(K-1):
        people.append(people.pop(0))
    people.pop(0)
print(people[0])