import sys

string = sys.stdin.readline()

def summarize_string(string):
    alphabet_occurrence_array = [0]*26
    
    lower = string.lower()
    lower = lower.replace(" ", "")
    
    for char in lower :
        if not char.isalpha() :
            continue
        char_index = ord(char) - ord('a')
        alphabet_occurrence_array[char_index] += 1
        
    exist_alpha_string = []
    
    for i in range(len(alphabet_occurrence_array)) :
        if alphabet_occurrence_array[i] > 0 :
            exist_alpha_string.append(chr(i+ord('a')))
            exist_alpha_string.append(str(alphabet_occurrence_array[i]))
            exist_alpha_string.append('/')
    
    #2주차 배울예정
    exist_alpha_string.pop()
    
    return ''.join(exist_alpha_string)

result = summarize_string(string)

print(result)
