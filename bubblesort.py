def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -45, -5])
    [-45, -5, -2]

    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]

    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    """
    length = len(collection)
    for i in range(length):
        for j in range(i+1,length):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]
    return collection


if __name__ == "__main__":
    import time

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time: {time.process_time() - start}")
