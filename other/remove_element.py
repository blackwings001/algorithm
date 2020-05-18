def remove_element(array, k):
    i = 0
    j = 0
    n = len(array)

    while j < n:
        if i == j or array[j] == k:
            j += 1
        else:
            array[i], array[j] = array[j], array[i]

        if array[i] != k:
            i += 1

    return array[:i], i









if __name__ == '__main__':
    array = [0, 1, 2, 3, 2, 0, 3]
    k = 2
    removed_array, removed_length = remove_element(array, k)

    print(removed_array, removed_length)