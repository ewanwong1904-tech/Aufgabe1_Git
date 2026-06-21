import random
import time

import matplotlib.pyplot as plt


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


def measure_runtime(input_size):
    """
    Measure how long merge sort takes for a randomly generated list.
    """
    numbers = [random.randint(0, 10000) for _ in range(input_size)]

    start_time = time.perf_counter()
    merge_sort(numbers)
    end_time = time.perf_counter()

    return end_time - start_time


def plot_runtime():
    """
    Plot the runtime of merge sort for different input sizes.
    """
    input_sizes = [10, 50, 100, 500, 1000, 2000]
    runtimes = [measure_runtime(size) for size in input_sizes]

    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, runtimes, marker="o", label="Merge sort runtime")

    plt.title("Runtime of Merge Sort for Different Input Sizes")
    plt.xlabel("Input size")
    plt.ylabel("Runtime in seconds")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


def main():
    example_numbers = [5, 3, 8, 1, 2]
    sorted_numbers = merge_sort(example_numbers)

    print("Original list:", example_numbers)
    print("Sorted list:", sorted_numbers)
    plot_runtime()


if __name__ == "__main__":
    main()
