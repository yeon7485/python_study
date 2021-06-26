def find_same_number_1(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    number = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in number:
            return element

        # 해당 요소를 사전에 저장시킨다.
        number[element] = True


# 테스트
print(find_same_number_1([1, 4, 3, 5, 3, 2]))
print(find_same_number_1([4, 1, 5, 2, 3, 5]))
print(find_same_number_1([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
