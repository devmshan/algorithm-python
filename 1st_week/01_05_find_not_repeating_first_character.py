def find_not_repeating_first_character(string):
    # 반복되지 않는 첫번째 알파벳
    # 반복되는지 아닌지 판단
    # alphabet_occurrence_array
    # ??
    low_string = string.lower()
    low_string = low_string.replace(" ", "")

    alphabet_occurrence_array = [0]*26
    occurrence_index = 0

    for char in low_string:
        if not char.isalpha():
            continue
        occurrence_index = ord(char) - ord('a')
        alphabet_occurrence_array[occurrence_index] += 1

    for char in low_string:
        if alphabet_occurrence_array[ord(char) - ord('a')] == 1:
            return char

    return '_'

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = C 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaa"))