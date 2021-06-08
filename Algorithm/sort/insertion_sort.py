# 삽입 정렬

def insertion_sort(some_list):
    for i in range(1, len(some_list)):
        key = some_list[i]

        j = i - 1
        # 해당 값(key)이 작으면 큰 값들을 오른쪽으로 한 칸씩 옮기기
        while j >= 0 and key < some_list[j]:
            some_list[j + 1] = some_list[j]
            j -= 1

        # 빈 칸에 최솟값 넣기
        some_list[j + 1] = key

    return some_list


# 테스트
print(insertion_sort([9, 8, 1, 2, 3]))
print(insertion_sort([4, 2, 7, 1, 9, 3]))
print(insertion_sort([6, 5, 3, 1, 8, 7, 2, 4]))
