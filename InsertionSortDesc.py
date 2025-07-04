# Get input from user
input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.strip().split()))

print("Original array:", arr)

insertion_sort_desc(arr)

print("Sorted in decreasing order:", arr)