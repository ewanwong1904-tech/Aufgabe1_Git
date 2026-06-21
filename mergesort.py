import random
import time

import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def measure_runtime(input_size):
    numbers = [random.randint(0, 10000) for _ in range(input_size)]

    start_time = time.perf_counter()
    merge_sort(numbers)
    end_time = time.perf_counter()

    return end_time - start_time


def plot_runtime():
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


print(merge_sort([5, 3, 8, 1, 2]))
plot_runtime()
