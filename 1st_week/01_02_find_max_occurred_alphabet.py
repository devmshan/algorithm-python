def find_max_accurred_alphabet(string):

    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h" ,"i", "j" ,"k", "l" ,"m", "n" ,"o", "p" ,"q", "r" ,"s", "t" ,"u", "v" ,"w", "x"
                      "y", "z"]
    
    max_occurence = 0
    max_alphabet = alphabet_array[0]

    

    return "a"

# 1. a, b, c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 그 알파벳으로 변환한다.
# a -> hello my name is dingcodingco -> 0 max_occurence = 0 max_alphabet = a
# b -> hello my name is dingcodingco -> 0 max_occurence = 0 max_alphabet = b
# c -> hello my name is dingcodingco -> 2 max_occurence = 2 max_alphabet = c
# a -> hello my name is dingcodingco -> 0 max_occurence = 0 max_alphabet = a

def find_alphabet_occurrence_array(string):
    low_string = string.lower()
    low_string = low_string.replace(" ", "")

    alphabet_accurrence_array = [0] * 26

    for char in low_string:
        if not char.isalpha():
            continue
        char_index = ord(char) - ord('a')
        alphabet_accurrence_array[char_index] += 1

    return alphabet_accurrence_array

# print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))

# text.strip() 양쪽 공백 제거 - 문자열 시작과 끝의 공백(스페이스, 탭, 줄바꿈 등)을 제거
# text.replace(" ", "")       # "helloworld\t!\n"  (공백만 제거) 
# "".join(text.split())       # "helloworld!"      (탭, 개행 등 모든 공백 제거)
# text.replace(" ", "")가 더 빠릅니다.
# - replace(" ", "") — 문자열을 한 번 순회하며 공백만 제거
# - "".join(text.split()) — split으로 리스트를 만들고, join으로 다시 합치는 2단계 작업

print(find_max_occurred_alphabet("hello my name is dingcodingco"))

#str.isalpha() 알파벳인지 확인 

# print(ord('a'))
# print(ord('a')-97)
# print(ord('b')-97)
# print(chr(97))

#1번째 인덱스에 무슨 알파벳?
#chr()

# a -> chr(97)
# 97 -> ord('a')

# index = ord('d') - ord('a')