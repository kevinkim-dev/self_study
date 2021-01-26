#########################
#  SWEA number 1936  
#  by 김승현                
#########################

# Q. 1대1 가위바위보

ab = input().split()
a = int(ab[0])
b = int(ab[1])

if a - b % 3 == 1:
    print('A')
elif b - a % 3 == 1:
    print('B')
else:
    print('tie')