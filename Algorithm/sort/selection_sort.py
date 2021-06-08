# 선택 정렬

def selection_sort(some_list):
    for i in range(len(some_list)):
        min_idx = i

        # 최솟값 찾기
        for j in range(i + 1, len(some_list)):
            if some_list[min_idx] > some_list[j]:
                min_idx = j

        # 찾은 최솟값과 첫 번째 요소를 교체
        some_list[i], some_list[min_idx] = some_list[min_idx], some_list[i]

    return some_list


# 테스트
print(selection_sort([9, 8, 1, 2, 3]))
print(selection_sort([4, 2, 7, 1, 9, 3]))
print(selection_sort([6, 5, 3, 1, 8, 7, 2, 4]))
