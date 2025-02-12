import time

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        comparisons, swaps = 0, 0
        start = time.time()

        for i in range(n):
            for j in range(n - i - 1):
                comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1

        end = time.time()
        return arr, comparisons, swaps, end - start





    @staticmethod
    def insertion_sort(arr):
        comparisons, swaps = 0, 0
        start = time.time()

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                comparisons += 1
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            arr[j + 1] = key

        end = time.time()
        return arr, comparisons, swaps, end - start

    
    @staticmethod
    def merge_sort_iterative(arr):
       
        start_time = time.time()
        comparisons = 0
        swaps = 0

        width = 1
        n = len(arr)

        while width < n:
            for i in range(0, n, 2 * width):
                left = arr[i:i + width]
                right = arr[i + width:i + 2 * width]
                merged = []
                i_left, i_right = 0, 0

                while i_left < len(left) and i_right < len(right):
                    comparisons += 1
                    if left[i_left] < right[i_right]:
                        merged.append(left[i_left])
                        i_left += 1
                    else:
                        merged.append(right[i_right])
                        i_right += 1
                        swaps += 1

                merged.extend(left[i_left:])
                merged.extend(right[i_right:])
                arr[i:i + len(merged)] = merged

            width *= 2

        end_time = time.time()
        return arr, comparisons, swaps, end_time - start_time



    @staticmethod
    def merge_sort_recursive(arr):
        
        start_time = time.time()  
        comparisons = [0]  
        swaps = [0]

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    comparisons[0] += 1
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                        swaps[0] += 1
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

        end_time = time.time()  # Tiempo de finalización
        return arr, comparisons[0], swaps[0], end_time - start_time

    


    @staticmethod
    def quick_sort_recursive(arr):
        
        start_time = time.time()
        comparisons = [0]
        swaps = [0]

        def quick_sort(arr):
            if len(arr) <= 1:
                return arr

            pivot = arr[len(arr) // 2]
            left = []
            middle = []
            right = []

            for play in arr:
                comparisons[0] += 1
                if play < pivot:
                    left.append(play)
                elif play > pivot:
                    right.append(play)
                    swaps[0] += 1
                else:
                    middle.append(play)

            return quick_sort(left) + middle + quick_sort(right)

        sorted_arr = quick_sort(arr)
        end_time = time.time()
        return sorted_arr, comparisons[0], swaps[0], end_time - start_time

    
    @staticmethod
    def quick_sort_iterative(arr):

        start_time = time.time()
        comparisons = 0
        swaps = 0

        stack = [(0, len(arr) - 1)]

        while stack:
            left, right = stack.pop()
            if left >= right:
                continue

            pivot_index = (left + right) // 2
            pivot = arr[pivot_index]
            i, j = left, right

            while i <= j:
                while arr[i] < pivot:
                    comparisons += 1
                    i += 1
                while arr[j] > pivot:
                   comparisons += 1
                   j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                    i += 1
                    j -= 1

            if left < j:
                stack.append((left, j))
            if i < right:
                stack.append((i, right))

        end_time = time.time()
        return arr, comparisons, swaps, end_time - start_time 


    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
