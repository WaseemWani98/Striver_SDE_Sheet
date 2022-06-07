"""
You have been given an integer array/list(ARR) of size 'N'.
It only contains 0s, 1s and 2s.
Write a solution to sort this array/list.
"""


#   Approach #1:
#   Simply Sort the array.

#   T.C : O(NLogN)
#   S.C : O(1)

def approach1(arr):
    arr.sort()


#   Approach #2:
#   Use COUNTING SORT.
#   o- Since the array consists of 0s, 1s and 2s only, we can
#      count their frequencies in one pass and then populate
#      the array with their counts in another pass

#   T.C : O(n+n) = O(2n)
#   S.C : O(1)

def approach2(arr):
    count0 = count1 = count2 = 0

    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    k = 0

    while count0:
        arr[k] = 0
        count0 -= 1
        k += 1

    while count1:
        arr[k] = 0
        count1 -= 1
        k += 1

    while count2:
        arr[k] = 0
        count2 -= 1
        k += 1


#   Approach #3:
#   Using Dutch National Flag Algorithm
#   o-  Maintain 3 Pointers: low, mid and high
#       Set low = 0, mid = 0, high = len(arr)-1
#       Run a loop till mid <= high     (mid is moving pointer)
#       Check for these conditions
#       o-  if arr[mid] == 0, swap arr[low] with arr[mid], increment both
#       o-  if arr[mid] == 1, just increment mid
#       o-  if arr[mid] == 2, swap arr[low] with arr[mid], decrement high

#   T.C : O(n)      (Single pass)
#   S.C : O(1)

def approach3(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
