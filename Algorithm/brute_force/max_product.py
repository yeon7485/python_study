# 카드 뭉치 최대 조합
# 두 카드를 뽑아 가장 큰 두 수의 곱 구하기
def max_product(left_cards, right_cards):
    # 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
    max_product = left_cards[0] * right_cards[0]

    # 가능한 모든 조합을 보기 위한 중첩 반복문
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값 값과 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다.
            max_product = max(max_product, left * right)

    return max_product


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
