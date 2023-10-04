# TODO сортировка пузырьком


def myBubbleSort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] < myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

def default_sort(source: list[int]):
    return sorted(source)

def bubble_sort(source: list[int]):
    new_source = source
    length = len(new_source)
    for i in range(1, length):
        for j in range(0, length - i):
            if new_source[j] > new_source[j + 1]:
                # temp = data[j]  # временное хранилище для пузырька
                # data[j] = data[j+1]
                # data[j+1] = temp
                new_source[j], new_source[j + 1] = new_source[j + 1], new_source[j]  # поменяли местами
    return new_source

def selection_sort(arr: list[int]):
    for i in range(1, len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]  # поменяли местами
    return arr

def insertion_sort(source):
    for cur_idx in range(1, len(source)):
        prev_idx = cur_idx - 1
        val = source[cur_idx]
        while prev_idx > 0 and source[prev_idx] > val:
            source[prev_idx + 1] = source[prev_idx]
            prev_idx -= 1
        source[prev_idx + 1] = val
    return source

    def sort_sorted(_source: list[int], _reverse=False) -> list[int]:
        # _source.sort(reverse=_reverse)  # сортирует прям этот массив, но ничего не возвращает
        new_sorted_array = sorted(_source, reverse=_reverse)  # сортирует и возвращает отсортированный массив
        return new_sorted_array

def sort_bubble(_src: list[int], _reverse=False) -> list[int]:
    # https://vk.com/@bookflow-naglyadnaya-vizualizacii-algoritmov-sortirovki
    length = len(_src)
    for i in range(0, length - 1):
        already_sorted = True
        for j in range(0, length - 1 - i):
            if _reverse:
                if _src[j] < _src[j + 1]:
                    # a = 15
                    # b = 17

                    # c = b
                    # b = a
                    # a = c

                    # a, b = b, a
                    # print(a, b)

                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
                    already_sorted = False
            else:
                if _src[j] > _src[j + 1]:
                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
                    already_sorted = False
        if already_sorted:
            break
    return _src

def sort_insertion(_src: list[int], _reverse=False) -> list[int]:
    length = len(_src)
    for i in range(1, length):
        key_item = _src[i]
        j = i - 1
        if _reverse:
            while j >= 0 and _src[j] < key_item:
                _src[j + 1] = _src[j]
                # j -= 1  # decrement
                j = j - 1  # decrement
        else:
            while j >= 0 and _src[j] > key_item:
                _src[j + 1] = _src[j]
                j = j - 1
        _src[j + 1] = key_item

    return _src

def sort_quicksort(_src: list[int], is_reversed=False) -> list[int]:
    def start_quicksort(__src: list[int], _is_reversed=False) -> list[int]:
        length = len(__src)
        if length < 2:
            return __src
        low, same, high = [], [], []
        pivot = __src[random.randint(0, length - 1)]
        for item in __src:
            if _is_reversed:
                if item > pivot:
                    low.append(item)
                elif item == pivot:
                    same.append(item)
                elif item < pivot:
                    high.append(item)
            else:
                if item < pivot:
                    low.append(item)
                elif item == pivot:
                    same.append(item)
                elif item > pivot:
                    high.append(item)
        return start_quicksort(low, is_reversed) + same + start_quicksort(high, is_reversed)

    return start_quicksort(_src, is_reversed)

def sort_merge(_src: list[int], is_reversed=False) -> list[int]:
    def start_merge(__src: list[int], _is_reversed=False) -> list[int]:
        def merge(left, right):
            if len(left) == 0:
                return right
            if len(right) == 0:
                return left
            result = []
            index_left = index_right = 0
            if _is_reversed:
                while len(result) < len(left) + len(right):
                    if left[index_left] >= right[index_right]:
                        result.append(left[index_left])
                        index_left += 1
                    else:
                        result.append(right[index_right])
                        index_right += 1
                    if index_right == len(right):
                        result += left[index_left:]
                        break
                    if index_left == len(left):
                        result += right[index_right:]
                        break
            else:
                while len(result) < len(left) + len(right):
                    if left[index_left] <= right[index_right]:
                        result.append(left[index_left])
                        index_left += 1
                    else:
                        result.append(right[index_right])
                        index_right += 1
                    if index_right == len(right):
                        result += left[index_left:]
                        break
                    if index_left == len(left):
                        result += right[index_right:]
                        break

            return result

        if len(__src) < 2:
            return __src
        midpoint = len(__src) // 2
        return merge(
            left=start_merge(__src[:midpoint], _is_reversed),
            right=start_merge(__src[midpoint:], _is_reversed)
        )

    return start_merge(__src=_src, _is_reversed=is_reversed)


if __name__ == '__main__':
    numbers_orig = [5, 2, 6, 7, 8, 12, 15, 111]
    print("Original list:")
    print(numbers_orig)
    myBubbleSort(numbers_orig)
    print("Sorted list:")
    print(numbers_orig)
