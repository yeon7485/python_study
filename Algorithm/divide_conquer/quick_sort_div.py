# 퀵 정렬 - 분할 정복

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            my_list[i], my_list[b] = my_list[b], my_list[i]
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    my_list[b], my_list[p] = my_list[p], my_list[b]
    p = b

    # pivot의 최종 인덱스를 리턴해 준다
    return p


# 퀵 정렬 (파라메터로 리스트만 받아도 start, end 초기값 설정)
def quicksort(my_list, start=0, end=None):
    # end 설정해주기
    if end == None:
        end = len(my_list) - 1

    # base case
    if end - start < 1:
        return

    # my_list를 두 부분으로 나누어주고 (Divide)
    # partition 이후 pivot의 인덱스를 리턴받는다.
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)  # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)  # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)  # start, end 파라미터 없이 호출
print(list3)
