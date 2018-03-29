'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Function Description

Complete the diagonalDifference function described below to calculate the absolute difference between diagonal sums.
diagonalDifference( integer: a_size_rows, integer: a_size_cols, integer array: arr)
Parameters:
a_size_rows: number of rows in array
a_size_cols: number of columns in array
a: array of integers to process
Returns: integer value that was calculated

Constraints

Raw Input Format

The first line contains a single integer, denoting the number of rows and columns in the matrix .
The next lines denote the matrix 's rows, with each line containing space-separated integers describing the columns.

Sample Input 0

3
11 2 4
4 5 6
4 

Sample Output 0

15

Explanation 0

The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
'''

#function to calculate the diagonal difference 
def diagonal_difference(a,n):
    sum1, sum2 = 0,0
    
    for i in range(n):
        sum1 += a[i][i]
        sum2 += a[i][n-i-1]
    return abs(sum1-sum2)
    

if __name__ == '__main__':

    #size of matrix
    n = int(input())
    # intialize empty list
    a = []

    for _ in range(n):
            a.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(a,n)
    print(result)