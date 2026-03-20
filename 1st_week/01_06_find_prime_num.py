import sys

a, b = map(int, sys.stdin.readline().split())

def find_prime_num(num1, num2):
    prime_num_array = []
    for num in range(num1,num2+1):
        if is_prime(num) :
            prime_num_array.append(num)
    return prime_num_array

# 첫번째 풀이는 2부터 판별하는 수 전까지 나눠보고 나머지가 0이 안나온다면 소수로 정의한다. 해당 수까지 모두 확인해야하므로 시간복잡도는 O(N)이 되고, 가장 원초적인 방법이다.
def is_prime(num):
    for i in range(2, num):
        if num % i == 0 :
            return False
    return True

prime_array = find_prime_num(a, b)

for i in range(len(prime_array)):
    print(prime_array[i])