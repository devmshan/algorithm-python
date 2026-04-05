# 1번괄호 ) 면 False
# (()(
# 닫는 괄호가 나오면 바로 직전에 열렸었던 괄호를 없앤다
# stack에 넣고 넣고 빼고 넣는데 있으면 False
# 빼는데 없으면 false

def is_correct_parenthesis(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True



print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))