# 리스트에서 수익이 가장 큰 구간 찾기

def sublist_max_1(profits):
    max_profit = profits[0]  # 최대 수익

    for i in range(len(profits)):
        for j in range(i, len(profits)):
            # i부터 j까지 수익의 합을 계산하고 최대 수익이라면 max_profit 업데이트
            total = sum(profits[i:j + 1])
            max_profit = max(max_profit, total)

    return max_profit


# 테스트
print(sublist_max_1([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max_1([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max_1([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
