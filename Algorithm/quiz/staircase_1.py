def staircase_1(n):
    previous, current = 1, 1

    for i in range(n):
        previous, current = current, previous + current
    return previous


# 테스트
print(staircase_1(0))
print(staircase_1(6))
print(staircase_1(15))
print(staircase_1(25))
print(staircase_1(41))
