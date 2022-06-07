"""
You are given an array (ARR) of length N, consisting of integers.
You have to find the sum of the subarray (including empty subarray)
having maximum sum among all sub-arrays.
A subarray is a contiguous segment of an array. In other words,
a subarray can be formed by removing 0 or more integers from the
beginning, and 0 or more integers from the end of an array.
"""


#   Approach #1:

def max_subarray_sum(arr, n):
    max_sum = arr[0]
    max_so_far = 0
    for i in range(n):
        max_so_far += arr[i]
        max_sum = max(max_so_far, max_sum)
        if max_so_far < 0:
            max_so_far = 0
    return max_sum
