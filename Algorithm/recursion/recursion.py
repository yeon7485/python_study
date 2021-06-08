# 피보나치 수열
def fib(n):
    # base case
    if n < 3:
        return 1

    # recursive case
    return fib(n - 1) + fib(n - 2)


# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))


# 숫자 합
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n + triangle_number(n - 1)


# 테스트
for i in range(1, 11):
    print(triangle_number(i))


# 자릿수 합
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# 리스트 뒤집기
# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # base case
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    # recursive case
    return some_list[-1:] + flip(some_list[:-1])


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
