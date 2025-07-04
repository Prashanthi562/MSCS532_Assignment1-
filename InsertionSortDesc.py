def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

      
# Get input from user
input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.strip().split()))

print("Original array:", arr)

insertion_sort_desc(arr)

print("Sorted in decreasing order:", arr)