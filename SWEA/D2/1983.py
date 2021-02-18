#########################
#  SWEA number 1983
#  by 김승현                
#########################

# Q. 조교의 성적 매기기

def bubble_sort(num_list):
    for i in range(len(num_list)-1, -1, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return

grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for t in range(1, int(input())+1):
    N, x = map(int, input().split())
    score_list = [0]*N
    for n in range(N):
        a, b, c = map(int, input().split())
        score_list[n] = 0.35*a + 0.45*b+ 0.2*c
    target = score_list[x-1]
    bubble_sort(score_list)
    for i in range(N):
        if score_list[i] == target:
            target_index = i
            break
    target_grade_index = target_index // int(N/10)
    print("#%d %s" %(t, grade[target_grade_index]))