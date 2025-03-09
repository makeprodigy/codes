def binary_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1


def recursive_binary_search(arr, target):
  low, high = 0, len(arr) - 1
  if low > high:
    return - 1
  mid = (low + high) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return recursive_binary_search(arr, mid+1, high, target)
  else:
    return recursive_binary_search(arr, low, mid-1, target)
  

# bubble sort: repeatedly swaps adjacent elements if they are in the wrong order; the largest element bubbles up to the correct position in each pass

# iterate through the array, compare adjacent element and swap if needed, the largest element moves to the end after each pass, Repeat for remaining elements (total n-1 passes) until the array is sorted

def bubble_sort_unoptimized(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_optimized_earlyExit(arr):
  n = len(arr)
  for i in range(n-1):
    swap_count = 0
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] #highest element bubbling up, means moving up till it reaches its position
        swap_count += 1
    if swap_count == 0:
      break

def bubble_sort_optimized(arr):
  n = len(arr)
  for i in range(n-1):
    swap_count = 0
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap_count += 1
    if swap_count==0:
      break

# selection sort is a comparision-based algorithm, it repeatedly finds the smallest element and places it in the correct position, works by selecting the minimum element in each iteration
# it iterates through the array, finds the minimum element from the unsorted part, swap it with the first element of the unsorted part, repeat the process for the remaining elements

def selection_sort(arr):
  n = len(arr)
  for i in range(n): #taking the length of whole array in the range
    min_index = i #setting the minimum index equals to i to check later that the element at min_index which is i is greater than the elements from range i+1 to n
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
# insertion sort, this is also a comparison-based, in-place sorting algorithm, builds the sorted array one element at a time by inserting each element into its correct position, efficient for small and nearly sorted datasets
# start from the second element (index = 1), treating the first as sorted, compare it with the previous elements in the sorted part, shift larger elements into its correct position, repeat for all elements until the array is fully sorted

# performs better than bubble and selection sort for small datasets
def insertion_sort(arr):
  n = len(arr)
  for i in range(n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

# recursion
# base case - stops recursion, recursive case - calls itself, used for problems that can be broken into smaller subproblems, reduced redundant code but may increase space complexity due to function call stack

# Factorial of a Number
def factorial(n):
  if n==0 or n==1:
    return 1
  return n * factorial(n-1)

# Fibonacci Series
def fibonacci(n):
  if n==0 or n==1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

# Sum of Digits
def sum_of_digits(n):
  if n==0:
    return 0
  return (n%10) + sum_of_digits(n//10)

# Reverse a String
def reverse_string(s):
  if len(s) == 0:
    return ""
  return s[-1] + reverse_string(s[:-1])
# note: if i want to include all the elements, i can use s[:] or s[:len(s)]

# Check if a string is Palindrome
def is_Palindrome(s):
  if len(s) <= 1: # covers the case when the length of the string will become after getting sliced off in the call stack
    return True
  if s[0] != s[-1]: #checks if the first and the last element of the sliced off string are equal or not
    return False
  return is_Palindrome(s[1:-1])

# Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
  if n==1:
    print(f"Move disk {n} from {source} to {target}")
    return
  tower_of_hanoi(n-1, source, target, auxiliary)
  print(f"Move disk {n} from {source} to {target}")
  tower_of_hanoi(n-1, auxiliary, source, target)

# Climbing Stairs (Dynamic Recursion)
def climb_stairs(n):
  if n==0 or n==1:
    return 1
  return climb_stairs(n-1) + climb_stairs(n-2)

# Frog Jump (Optimized Dynamic Recursion)
def frog_jump(cost, n):
  if n==0:
    return 0
  if n==1:
    return abs(cost[1] - cost[0])
  return min(abs(cost[n] - cost[n-1] + frog_jump(cost, n-1)),
             abs(cost[n] - cost[n-2]) + frog_jump(cost, n-2))  


# Prefix Sum
def prefix_sum_unoptimized(arr):
  n = len(arr)
  prefix = [0] * n
  prefix[0] = arr[0]

  for i in range(1,n):
    prefix[i] = prefix[i-1] + arr[i]
  
  return prefix

def range_sum(prefix, L, R):
  if L == 0:
    return prefix[R]
  return prefix[R] - prefix[L-1]


# Prefix Sum Optimized, in this we directly modify the array instead of creating a new array of zeroes
def inplace_prefix_sum(arr):
  for i in range(1, len(arr)):
    arr[i] += arr[i-1] # Modify array directly
  return arr


# Two Pointers 
def has_pair_with_sum(arr, target):
  left, right = 0, len(arr) - 1
  while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
      return True
    elif current_sum < target:
      left += 1
    else:
      right -= 1
  return False



t = int(input())
def half_sorted(t):
    result = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        temp_arr = arr[:]
        for i in range(1,n):
            key = temp_arr[i]
            j = i-1
            while j >= 0 and temp_arr[j] > key:
                temp_arr[j+1] = temp_arr[j]
                j -= 1
            temp_arr[j+1] = key
        
        count = 0
        for i in range(n):
            if temp_arr[i] == arr[i]:
                count += 1
        if count == n//2:
            result.append("True")
        else:
            result.append("False")
    return result

        
    

ress = half_sorted(t)
for res in ress:
    print(res)



def bubble_sort_with_swap_check(arr, max_swaps):
    n = len(arr)
    total_swaps = 0  # Tracks total swaps across all iterations
    
    for i in range(n - 1):
        swap_count = 0  # Tracks swaps in the current iteration
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
        
        total_swaps += swap_count  # Add current iteration swaps to total swaps

        
        if swap_count == 0:
            break  # Optimization: stop if already sorted
    
    return True, total_swaps  # Total swaps are within limit

# Example usage
arr = [5, 3, 8, 4, 2]
max_swaps = 5
result, total_swaps = bubble_sort_with_swap_check(arr, max_swaps)