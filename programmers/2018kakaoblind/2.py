def solution(str1, str2):
    def to_lower(string):
        new_string = ''
        for a in string:
            if 65 <= ord(a) <= 90:
                new_string +=  chr(ord(a) + 32)
            else:
                new_string += a
        return new_string
    answer = 0
    str1, str2 = to_lower(str1), to_lower(str2)
    dic1, dic2 = dict(), dict()
    for i in range(len(str1)-1):
        two = str1[i:i+2]
        if 97 <= ord(two[0]) <= 122 and 97 <= ord(two[1]) <= 122:
            dic1[two] = dic1.get(two, 0) + 1
    for i in range(len(str2)-1):
        two = str2[i:i+2]
        if 97 <= ord(two[0]) <= 122 and 97 <= ord(two[1]) <= 122:
            dic2[two] = dic2.get(two, 0) + 1
    intersec = 0
    for key in dic1.keys():
        intersec += min(dic1[key], dic2.get(key, 0))
    union = sum(dic1.values()) + sum(dic2.values()) - intersec
    if union == 0:
        answer = 65536
    else:
        answer = int(intersec * 65536 / union)
    return answer

str1, str2 = 'FRANCE', 'french'
solution(str1, str2)