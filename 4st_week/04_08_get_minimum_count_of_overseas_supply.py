import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

#최소한의 횟수로 밀가루 최대한 많이 가져오기 하지만 재고가 바닥나기 이전
# 1. 현재 재고의 상태에 따라 최고값을 받아야 한다.
# 2. 제일 많은 값만 가져가면 된다.
# >> heap
# >> maxheap


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []
    while stock <= k: # stock 이 k 보다 크게 되면 멈출 것이다.
        
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, supplies[last_added_date_index] * -1)
            last_added_date_index += 1

        supply = heapq.heappop(max_heap) * -1
        stock += supply
        answer += 1

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))