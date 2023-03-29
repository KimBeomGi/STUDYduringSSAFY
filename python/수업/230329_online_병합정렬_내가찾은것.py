def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx += 1
        else:
            result.append(right_arr[right_idx])
            right_idx += 1

    if left_idx < len(left_arr):
        result.extend(left_arr[left_idx:])
    else:
        result.extend(right_arr[right_idx:])

    return result


if __name__ == '__main__':
    arr = [5, 1, 6, 3, 4, 2, 7]
    print("정렬 전 : ", arr)

    arr = merge_sort(arr)

    print("정렬 후 : ", arr)