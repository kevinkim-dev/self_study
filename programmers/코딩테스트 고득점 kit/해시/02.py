#########################
#  Programmers problem kit 
#  해쉬 # 02
#  by 김승현                
#########################

# Q. 전화번호 목록

def solution(phone_book):
    phone_book = sorted(phone_book, key = lambda x: (x[0], len(x)))
    while phone_book:
        phone = phone_book.pop(0)
        for p in phone_book:
            if phone[0] != p[0]:
                break
            if phone == p[:len(phone)]:
                return False
    return True 

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))