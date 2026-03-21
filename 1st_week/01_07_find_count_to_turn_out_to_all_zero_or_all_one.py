import sys

string1 = sys.stdin.readline()

def chk_turn_out(string):

    count01 = 0
    count10 = 0
    for i in range(1, len(string)):
        if string[i] == '1' and string[i-1] == '0' :
            count01 += 1
        elif string[i] == '0' and string[i-1] == '1' :
            count10 += 1

    if int(count01) + int(count10) == 1 :
        return 1
    elif count01 < count10 :
        return count01
    else :
        return count10
    
result = chk_turn_out(string1)

print(result)