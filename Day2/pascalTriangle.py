"""
PASCAL TRIANGLE
-----------------------------
You are given an integer N. Your task is to return a 2-D ArrayList
containing the pascal’s triangle till the row N.
A Pascal's triangle is a triangular array constructed by summing
adjacent elements in preceding rows. Pascal's triangle contains the
values of the binomial coefficient.

For example, given integer N= 4 then you have to print.
1
1 1
1 2 1
1 3 3 1

Here for the third row, you will see that the second element is the
summation of the above two-row elements i.e. 2=1+1, and similarly
for row three 3 = 1+2 and 3 = 1+2.

"""

#   There can be 2 more variations to this Question
#   1. Print the nth row of Pascal's Triangle
#   2. Print the element at ith row, jth column
#
#   We'll be coding for all the 3 variations of the problem.


def printPascal(numRows):

    rows = [[1]]
    for r in range(1, numRows):
        rows.append([1] * (r+1))
        for c in range(1, r):
            rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
    return rows
