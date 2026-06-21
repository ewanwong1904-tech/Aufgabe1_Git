def merge_sort(numbers):
    """
    Sort a list of numbers using the merge sort algorithm.

    The function returns a new sorted list and does not change
    the original input list.
    """
    if len(numbers) <= 1:
        return numbers

    middle_index = len(numbers) // 2
    left_half = merge_sort(numbers[:middle_index])
    right_half = merge_sort(numbers[middle_index:])

    return merge(left_half, right_half)


def merge(left_half, right_half):
    """
    Merge two already sorted lists into one sorted list.
    """
    sorted_numbers = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_numbers.append(left_half[left_index])
            left_index += 1
        else:
            sorted_numbers.append(right_half[right_index])
            right_index += 1

    sorted_numbers.extend(left_half[left_index:])
    sorted_numbers.extend(right_half[right_index:])

    return sorted_numbers


def main():
    example_numbers = [5, 3, 8, 1, 2]
    sorted_numbers = merge_sort(example_numbers)

    print("Original list:", example_numbers)
    print("Sorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
