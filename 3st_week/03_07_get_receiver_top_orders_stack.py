input = [6, 9, 5, 7, 4]

# 인덱스
# 0 1 2 3 4
# v v v v

# 0 1 2 3 4
# v v v

# 0 1 2 3 4
# v v

# 0 1 2 3 4
# v

# 3210 4
# 210 3
# 10 2
# 0 1

        
def get_receiver_top_order(heights):
    answer = [0] * len(heights) # [0,0,0,0,0]
    
    while heights: # 해당 stack이 비어있지 않다면 계속 반복
        height = heights.pop() #4
        #[6,9,5,7]
        for idx in range(len(heights)-1,-1,-1):
            if height <= heights[idx]:
                answer[len(heights)] = idx + 1
                break
            
    return answer

print(get_receiver_top_order(input))