#########################
#  SWEA number 1928  
#  by 김승현                
#########################

# Q. Base64 Decoder

# decoding 후 8개씩 잘라서 ASCII로 디코딩!

def decoding_to_bi(char_list):
    string = ''
    for i in range(len(char_list)//4):
        binary = ''
        for j in range(4):
            c = char_list[4*i+j]
        # 대문자인 경우 65~90, 소문자의 경우 97~122 이므로
        # 대문자는 65를 빼고 소문자는 71을 뺀다.
        # 48~57이 0~9이므로 숫자인 경우에는 48을 뺀다.
            if ord(c) >= 65 and ord(c) <= 90:
                binary += format(ord(c)-65, 'b').rjust(6, '0')
            elif ord(c) >= 97 and ord(c) <= 122:
                binary += format(ord(c)-71, 'b').rjust(6, '0')
            elif ord(c) >= 48 and ord(c) <= 57:
                binary += format(ord(c)+4, 'b').rjust(6, '0') 
        string += chr(int(binary[:8], 2)) + chr(int(binary[8:16], 2)) + chr(int(binary[16:24], 2))
    return string

def decoding_to_ascii(char_list):
    pass

T = int(input())

for t in range(1, T+1):
    char_list = []
    char_list.extend(input())
    print(f"#{t}", end=' ')
    print(decoding_to_bi(char_list))

# 현타가 오지만 base64를 import 하면 3줄만에 가능하다...
# import base64

# T = int(input())
# for t in range(1, T+1):
#     print(f"#{t} {base64.b64decode(input()).decode('utf-8')}")









# 10
# TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
# U3VzcGljaW9uIGZvbGxvd3MgY2xvc2Ugb24gbWlzdHJ1c3Qu
# VG8gZG91YnQgaXMgc2FmZXIgdGhhbiB0byBiZSBzZWN1cmUu
# T25seSB0aGUganVzdCBtYW4gZW5qb3lzIHBlYWNlIG9mIG1pbmQu
# QSBmdWxsIGJlbGx5IGlzIHRoZSBtb3RoZXIgb2YgYWxsIGV2aWwu

#1 Life itself is a quotation.
#2 Suspicion follows close on mistrust.
#3 To doubt is safer than to be secure.
#4 Only the just man enjoys peace of mind.
#5 A full belly is the mother of all evil.
...






 
