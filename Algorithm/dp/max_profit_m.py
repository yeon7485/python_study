# 새꼼달꼼 장사 분석
# count를 팔아서 가능한 최대 수익을 리턴시켜 주는 함수
# memoization 방법으로 풀기

def max_profit_memo(price_list, count, cache):
    # base case
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]

    # 이미 계산한 값이라면 cache에 저장한 값을 리턴한다.
    if count in cache:
        return cache[count]

    # profit : count개를 팔아서 가능한 최대 수익을 저장하는 변수
    # 팔려고 하는 총 개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    # 팔려고 하는 총 개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        memo = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache)
        profit = max(profit, memo)

    cache[count] = profit

    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
