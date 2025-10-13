import time
import random
import copy
# here we using Bubble Sort
def bubble_sort_analysis(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    start_time = time.time()    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1 
    end_time = time.time()
    time_taken = end_time - start_time
    return arr, time_taken, comparisons, swaps, "O(1) (In-place)"

#  here Selection Sort
def selection_sort_analysis(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    start_time = time.time()
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the element at position i
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1 
    end_time = time.time()
    time_taken = end_time - start_time
    return arr, time_taken, comparisons, swaps, "O(1) (In-place)"

#Insertion Sort
def insertion_sort_analysis(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0     
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        swaps += 1
        j = i - 1
     
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j] 
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key 
        swaps += 1
    end_time = time.time()
    time_taken = end_time - start_time
    return arr, time_taken, comparisons, swaps, "O(1) (In-place)"

# Main Execution and Comparison
ARRAY_SIZE = 1000 
original_list = [random.randint(1, 10000) for _ in range(ARRAY_SIZE)]
print(f"--- Empirical Analysis for Array Size N={ARRAY_SIZE} ---")
print("\nNote: Time taken is system-dependent and will vary.")
print("      Swap/Move count is a measure of data manipulation operations.")
print("------------------------------------------------------------------")

algorithms = {
    "Bubble Sort": bubble_sort_analysis,
    "Selection Sort": selection_sort_analysis,
    "Insertion Sort": insertion_sort_analysis
}

results = {}

for name, func in algorithms.items():
    # We must use a copy so all algorithms run on the same UN-SORTED data
    test_list = copy.deepcopy(original_list)

    _, time_taken, comparisons, swaps, space = func(test_list)    
    results[name] = {
        "Time Taken (s)": time_taken,
        "Comparisons": comparisons,
        "Swaps/Moves": swaps,
        "Auxiliary Space": space
    }
    
for name, data in results.items():
    print(f"\nAlgorithm: {name}")
    print(f"  Time Taken: {data['Time Taken (s)']:.6f} seconds")
    print(f"  Comparisons: {data['Comparisons']}")
    print(f"  Swaps/Moves: {data['Swaps/Moves']}")
    print(f"  Auxiliary Space: {data['Auxiliary Space']}")

# Print Theoretical Complexity (Your request)
print("\n-------------------------------------------------------")
print("--- Theoretical Big O Complexity (Worst Case) ---")
print("Bubble Sort: O(N^2) Time, O(1) Space")
print("Selection Sort: O(N^2) Time, O(1) Space")
print("Insertion Sort: O(N^2) Time, O(1) Space")