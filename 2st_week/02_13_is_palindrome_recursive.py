#abcba
#문자열 맨 앞 맨 뒤 잘라서 검사
#a a 같으면 그 다음 검사
#b b 같으면 그 다음 검사

def is_palindrome_recursive(string): #소주만병만주소
    # 문자열 길이가 0 또는 1이면 팰린드롬
    # 문자열이 ''(짝수 완전 소진) 또는 '병'(홀수 가운데 문자) 이 되면 True 반환하고 재귀 종료합니다.
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome_recursive(string[1:-1]) #주만병만주

print(is_palindrome_recursive('소주만병만주소'))