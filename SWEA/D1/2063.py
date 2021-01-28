#########################
#  SWEA number 2063  
#  by 김승현                
#########################

# Q. 중간값 찾기

# number의 갯수 받아오기
num_num = int(input())

# number의 string을 공백을 기준으로 나눠서 list에 저장
num_list = list(map(int, input().split()))

# list를 sort한 후 중앙에 해당하는 index값을 print
print(sorted(num_list)[num_num//2])

