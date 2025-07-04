# Intialize function
def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
      
# Get input from user n no inputs can be provided 
input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.strip().split()))

print("Original array:", arr)

insertion_sort_desc(arr)

print("Sorted in decreasing order:", arr)