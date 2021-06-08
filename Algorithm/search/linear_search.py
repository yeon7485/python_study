# 선형 탐색 알고리즘

def linear_search_f(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None


def linear_search_w(element, some_list):
    i = 0
    b = len(some_list)

    while i < b:
        if some_list[i] == element:
            return i
        i += 1

    return -1


print(linear_search_f(2, [2, 3, 5, 7, 11]))  # 0
print(linear_search_f(0, [2, 3, 5, 7, 11]))  # None
print(linear_search_w(5, [2, 3, 5, 7, 11]))  # 2
print(linear_search_w(3, [2, 3, 5, 7, 11]))  # 1
print(linear_search_w(11, [2, 3, 5, 7, 11]))  # 4
