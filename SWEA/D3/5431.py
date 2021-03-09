#########################
#  SWEA number 5431
#  by 김승현                
#########################

# Q. 민석이의 과제 체크하기

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    students = list(range(1, N+1))
    submit = list(map(int, input().split()))
    for sub in submit:
        students.remove(sub)
    print("#%d %s" %(t, ' '.join(map(str, students))))