def is_palindrome_for(string):
    len_string = len(string)
    
    for i in range(len_string): # i: 0~n-1
        if string[i] != string[len_string - 1 - i]:
            return False
    return True

print(is_palindrome_for('abccba'))

#a a
#b b
#c c
#c c
#b b
#a a

print(is_palindrome_for('abcba'))

#a a
#b b
#c c