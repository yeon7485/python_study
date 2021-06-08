# 힙 정렬

# 힙 생성 알고리즘 (Heapify Algorithm)
# 특정한 노드의 두 자식 중에서 더 큰 자식과 자신의 위치를 바꾸는 알고리즘
def heapify(some_list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and some_list[largest] < some_list[l]:
        largest = l

    if r < n and some_list[largest] < some_list[r]:
        largest = r

    if largest != i:
        some_list[i], some_list[largest] = some_list[largest], some_list[i]
        heapify(some_list, n, largest)


def heapSort(some_list):
    n = len(some_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(some_list, n, i)

    for i in range(n - 1, 0, -1):
        some_list[i], some_list[0] = some_list[0], some_list[i]
        heapify(some_list, i, 0)

    return some_list


# 테스트
print(heapSort([9, 8, 1, 2, 3]))
print(heapSort([4, 2, 7, 1, 9, 3]))
print(heapSort([6, 5, 3, 1, 8, 7, 2, 4]))
