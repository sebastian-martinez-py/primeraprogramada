import time
from play_comparator import PlayComparator

class SortingAlgorithms:

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        start = time.time()

        for i in range(n):
            for j in range(n - i - 1):
                if PlayComparator.compare(arr[j], arr[j + 1]) > 0:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        end = time.time()
        return arr, end - start

    @staticmethod
    def insertion_sort(arr):
        start = time.time()

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and PlayComparator.compare(arr[j], key) > 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        end = time.time()
        return arr, end - start

    @staticmethod
    def merge_sort_recursive(arr):
        start_time = time.time()

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if PlayComparator.compare(left_half[i], right_half[j]) <= 0:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(arr)
        end_time = time.time()
        return arr, end_time - start_time

    @staticmethod
    def merge_sort_iterative(arr):
        start_time = time.time()
        width = 1
        n = len(arr)

        while width < n:
            left = 0
            while left < n:
                right = min(left + (2 * width) - 1, n - 1)
                mid = (left + right) // 2
                if mid + 1 <= right:
                    left_half = arr[left:mid + 1]
                    right_half = arr[mid + 1:right + 1]
                    
                    i = j = 0
                    k = left
                    while i < len(left_half) and j < len(right_half):
                        if PlayComparator.compare(left_half[i], right_half[j]) <= 0:
                            arr[k] = left_half[i]
                            i += 1
                        else:
                            arr[k] = right_half[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        arr[k] = left_half[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        arr[k] = right_half[j]
                        j += 1
                        k += 1

                left += 2 * width

            width *= 2

        end_time = time.time()
        return arr, end_time - start_time

    @staticmethod
    def quick_sort_recursive(arr):
        start_time = time.time()

        def quick_sort(arr):
            if len(arr) <= 1:
                return arr

            pivot = arr[len(arr) // 2]
            left = []
            middle = []
            right = []

            for play in arr:
                if PlayComparator.compare(play, pivot) < 0:
                    left.append(play)
                elif PlayComparator.compare(play, pivot) > 0:
                    right.append(play)
                else:
                    middle.append(play)

            return quick_sort(left) + middle + quick_sort(right)

        sorted_arr = quick_sort(arr)
        end_time = time.time()
        return sorted_arr, end_time - start_time

    @staticmethod
    def quick_sort_iterative(arr):
        start_time = time.time()
        stack = [(0, len(arr) - 1)]

        while stack:
            left, right = stack.pop()
            if left >= right:
                continue

            pivot = arr[(left + right) // 2]
            i, j = left, right

            while i <= j:
                while PlayComparator.compare(arr[i], pivot) < 0:
                    i += 1
                while PlayComparator.compare(arr[j], pivot) > 0:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1

            if left < j:
                stack.append((left, j))
            if i < right:
                stack.append((i, right))

        end_time = time.time()
        return arr, end_time - start_time
