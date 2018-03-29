'''
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers 3,  negative numbers 2, and  zero 1 in the array. 
The proportions of occurrence are positive::  3/6  , negative: 2/6  and zeros: 0/6 .
'''

def plusMinus(arr):
    neg, pos, zero = 0,0,0
    for i in arr:   
        if i > 0:
            pos += 1 
        elif i == 0:
            zero += 1
        else:
            neg += 1
    return ([pos,neg,zero])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)
    
    for _ in result:
        print(_/n)