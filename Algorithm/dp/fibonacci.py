# Memoization으로 피보나치 수 구하기
def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    # 이미 n번째 피보나치를 계산했으면 저장된 값을 바로 리턴
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면 계산한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    # 계산한 값 리턴
    return cache[n]


def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))


#
# Tabulation으로 피보나치 수 구하기
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트. 0번 피보나치 수는 그냥 0이라고 가정
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1], fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(50))


#
# Tabulation - 공간 최적화
def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 최근 두 값을 업데이트한다.
    # 이미 current = 1로 설정해주었기 때문에 반복문은 n-1번만 돌면 된다.
    for i in range(1, n):
        current, previous = current + previous, current

    # n번째 피보나치 수를 리턴한다.
    return current


# 테스트
print(fib_optimized(1))  # 1을 출력
print(fib_optimized(2))  # 1을 출력
print(fib_optimized(3))  # 2을 출력
print(fib_optimized(4))  # 3을 출력
print(fib_optimized(5))  # 5을 출력
