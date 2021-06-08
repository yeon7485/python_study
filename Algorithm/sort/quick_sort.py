# 퀵 정렬

# 퀵 정렬의 정렬 부분을 처리한다.
# start와 end는 각각 리스트의 첫 번째 요소와 마지막 요소다. (포인터 개념)
def partition(start, end, some_list):
    # 첫 번째 요소를 pivot으로 지정
    pivot_index = start
    pivot = some_list[pivot_index]

    # start와 end가 서로 엇갈릴 때까지 반복한다.
    while start < end:

        # 피벗보다 큰 요소를 찾을 때까지 start 포인터를 증가시킨다.
        while start < len(some_list) and some_list[start] <= pivot:
            start += 1

        # 피벗보다 작은 요소를 찾을 때까지 end 포인터를 감소시킨다.
        while some_list[end] > pivot:
            end -= 1

        # start와 end가 서로 엇갈리지 않았다면 스왑한다.
        if start < end:
            some_list[start], some_list[end] = some_list[end], some_list[start]

    # 마지막 요소를 피벗 요소로 바꾼다. 올바른 위치에 피벗을 넣는다.
    some_list[end], some_list[pivot_index] = some_list[pivot_index], some_list[end]

    # 리스트를 둘로 나누기 위해 end 포인터를 반환한다.
    return end


def quick_sort(start, end, some_list):
    if start < end:
        # 리스트를 둘로 나눠 end 포인터를 가져온다.
        p = partition(start, end, some_list)

        # 분할한 두 개의 부분 리스트를 다시 반복하여 정렬한다. (재귀)
        quick_sort(start, p - 1, some_list)
        quick_sort(p + 1, end, some_list)
    return some_list


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quick_sort(0, len(list1) - 1, list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quick_sort(0, len(list2) - 1, list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quick_sort(0, len(list3) - 1, list3)
print(list3)
