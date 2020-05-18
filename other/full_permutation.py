def full_permutation(array):
    permutation_array = [[]]
    for i in array:
        permutation_array = permutation(permutation_array, i)
    return permutation_array

def permutation(array, ele):
    if array == [[]]:
        return [[ele]]

    augment_array = []

    for sub_array in array:

        length = len(sub_array)
        sub_augment_array = []

        for index in range(length + 1):
            tmp_array = sub_array.copy()
            tmp_array.insert(index, ele)
            sub_augment_array.append(tmp_array)

        augment_array.extend(sub_augment_array)

    return augment_array





if __name__ == '__main__':
    origin_array = [1, 2, 3, 4]
    permutation_array = full_permutation(origin_array)
    print(permutation_array)
    print(len(permutation_array))
