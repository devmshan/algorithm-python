numbers = [1, 1, 1, 1, 1]
target_number = 3

# 간단하게 만들기
# numbers = [2,3,1]
# target_number = 0

# +2+3+1 = 6
# +2+3-1 = 4

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다는 소리

# [2,3]을 배치하는 경우의 수에서
# 맨 마지막 원소인 1을 더하냐 빼냐에 따라서 [2,3,1]의 경우의 수를 구할 수 있다

# +2-3+1 = 0
# +2-3-1 = -2
# -2+3+1 = 2
# -2+3-1 = 0
# -2-3+1 = -4
# -2-3-1 = -6

#재귀함수

# [2,3,1]
# 0, 0
# 1, 2 or                         1, -2
# 2, 5 or         2, -1           2, 1 or         2, -5
# 3, 6 or 3, 4    3, 0 or 3, -2   3, 2 or 3, 0    3, -4 or 3, -6

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return
    
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array,0,0)
    #print(f"all_ways is {all_ways}")
    
    target_count = 0
    for way in all_ways:
        if target == way:
            target_count +=1
            
    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!