# 버블 정렬

def bubble_sort(some_list):
    length = len(some_list) - 1
    for i in range(length):
        for j in range(length - i):
            if some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]

    return some_list


# 테스트
print(bubble_sort([9, 8, 1, 2, 3]))
print(bubble_sort([4, 2, 7, 1, 9, 3]))
print(bubble_sort([6, 5, 3, 1, 8, 7, 2, 4]))
