#########################
#  SWEA number 2047  
#  by 김승현                
#########################

# 신문 헤드라인

# string = input()
# upstring = string.upper()

# print(upstring)

sentence = input()

for char in sentence:
    if char != char.upper():
        sentence = sentence.replace(char, char.upper())
print(sentence)