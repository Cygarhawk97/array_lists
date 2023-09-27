def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

if __name__ == "__main__":
    arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

    # Using Linear Search on unsorted array
    index = linear_search(arr, 9)
    # This algorithm is a good choice for unsorted arrays because it doesn't require any arrangement beforehand.
    print(f"Linear Search: Number 9 found at index {index}.")

    # Sorting the array using Insertion Sort
    sorted_arr = insertion_sort(arr.copy())  # using a copy to keep the original array unchanged
    print(f"Sorted Array: {sorted_arr}")

    # Using Binary Search on sorted array
    index = binary_search(sorted_arr, 9)
    # Binary search is efficient for large sorted datasets as it divides the search interval in half repetitively.
    # It's widely used in real-world applications where time complexity matters, e.g., in databases.
    print(f"Binary Search: Number 9 found at index {index}.")
