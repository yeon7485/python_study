def power(x, y):
    if y == 0:
        return 1

    subresult = power(x, y // 2)

    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# 테스트
print(power(2, 5))
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
