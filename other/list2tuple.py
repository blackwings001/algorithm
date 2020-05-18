def transform(element):
    if isinstance(element, int):
        return element
    if isinstance(element, list):
        element = [transform(ele) for ele in element]
    return tuple(element)

if __name__ == '__main__':
    list_ = [[1], 2, [3, [4]], [[5]]]
    tuple_ = transform(list_)
    print(tuple_)
