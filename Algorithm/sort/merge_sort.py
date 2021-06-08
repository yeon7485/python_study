# 합병 정렬 (병합 정렬)

def merge_sort(some_list):
    if len(some_list) > 1:
        mid = len(some_list) // 2
        left = some_list[:mid]
        right = some_list[mid:]

        # 재귀
        merge_sort(left)
        merge_sort(right)

        # left와 right 리스트 요소 비교 후 정렬하기
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                some_list[k] = left[i]
                i += 1
            else:
                some_list[k] = right[j]
                j += 1
            k += 1

        # 왼쪽 부분 리스트에 요소들이 남았을 때 (오른쪽 부분 리스트는 정렬 완료)
        while i < len(left):
            some_list[k] = left[i]
            i += 1
            k += 1

        # 오른쪽 부분 리스트에 요소들이 남았을 때 (왼쪽 부분 리스트 정렬 완료)
        while j < len(right):
            some_list[k] = right[j]
            j += 1
            k += 1
    return some_list


# 테스트
print(merge_sort([9, 8, 1, 2, 3]))
print(merge_sort([4, 2, 7, 1, 9, 3]))
print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4]))
