array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    length_a = len(array1)
    length_b = len(array2)
    merge_array = []

    array1_index = 0
    array2_index = 0
    
    while array1_index < length_a and array2_index < length_b:
        if array1[array1_index] < array2[array2_index]:
            merge_array.append(array1[array1_index])
            array1_index +=1
        else:
            merge_array.append(array2[array2_index])
            array2_index +=1

    while array1_index < length_a:
        merge_array.append(array1[array1_index])
        array1_index +=1
        
    while array2_index < length_b:
        merge_array.append(array2[array2_index])
        array2_index +=1
    
    return merge_array

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))