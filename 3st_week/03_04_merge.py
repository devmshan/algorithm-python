array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    length_a = len(array1)
    length_b = len(array2)
    merge_array = []

    last_i = 0
    last_j = 0
    
    for i in range(length_a):
        for j in range(length_b):
            if j < last_j:
                continue
            #print(f"i={i}, j={j}")
            if array1[i] < array2[j]:
                merge_array.append(array1[i])
                last_i += 1
                break
            elif array1[i] >= array2[j]:
                merge_array.append(array2[j])
                last_j += 1

    if last_i < length_a:
        for i in range(last_i,length_a):
            merge_array.append(array1[i])
    elif last_j < length_b:
        for j in range(last_j,length_b):
            merge_array.append(array2[j])
    
    return merge_array

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))