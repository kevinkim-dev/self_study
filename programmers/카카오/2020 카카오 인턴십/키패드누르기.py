#########################
#  Programmers problem
#  Kakao internship 2020
#  by 김승현                
#########################

# Q. 키패드 누르기

def solution(numbers, hand):
    answer = ''
    num_loc = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    left_thumb, right_thumb = (3, 0), (3, 2)
    for number in numbers:
        if number in (1, 4, 7):
            left_thumb = num_loc[number]
            answer += 'L'
        elif number in (3, 6, 9):
            right_thumb = num_loc[number]
            answer += 'R'
        else:
            left_thumb_dis = abs(left_thumb[0] - num_loc[number][0]) + abs(left_thumb[1] - num_loc[number][1])
            right_thumb_dis = abs(right_thumb[0] - num_loc[number][0]) + abs(right_thumb[1] - num_loc[number][1])
            if left_thumb_dis < right_thumb_dis:
                left_thumb = num_loc[number]
                answer += 'L'
            elif right_thumb_dis < left_thumb_dis:
                right_thumb = num_loc[number]
                answer += 'R'
            else:
                if hand == 'left':
                    left_thumb = num_loc[number]
                    answer += 'L'
                else:
                    right_thumb = num_loc[number]
                    answer += 'R'
    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))