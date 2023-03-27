"""This module uses user-defined functions in Lab1_bai1, as well as functions in scipy library
This module includes the following user-defined functions:
1. Tranpose(arr) function
2. Mul(arr_x,arr_y) function for multiplication of two matrices
3. find_beta(x,y) to return beta_0, beta_1, beta_2.
All the codes are written in Python 3"""

import Lab1_bai1 as Lb1
from scipy.linalg import inv

def Transpose(arr):
    row = Lb1.Len(arr)
    col = Lb1.Len(arr[0])
    new_matrix = [[0 for x in range(row)] for y in range(col)]
    for i in range(row):
        for j in range(col):
            new_matrix[j][i] = arr[i][j]
    return new_matrix

def Mul(arr_x,arr_y):
    # To multiply matrix arr_x: mxn and arr_y: nxk
    if len(arr_x[0]) != len(arr_y):
        print("Wrong input")
    #row = Lb1.Len(arr_x)
    #col = Lb1.Len(arr_y[0])
    new_matrix = []
    for i in range(len(arr_x)):
        k = 0
        temp_outside = []
        while k < len(arr_y[0]):
            temp = 0
            for j in range(len(arr_x[0])):
                temp += arr_x[i][j] * arr_y[j][k]
            k += 1
            temp_outside += [temp]
        new_matrix += [temp_outside]
    return new_matrix

def find_beta(x,y):
    """Input:
        1. x: matrix with dimension k * 3
        2. y: matrix with dimension k * 1
       Output: vector (list) beta with dimension 3x1"""
    XT = Transpose(x)

    XTX = Mul(XT,x)
    XTY = Mul(XT,y)
    inv_XTX = inv(XTX)
    beta = Mul(inv_XTX, XTY)

    return beta


if __name__ == "__main__":
    #Find beta 1
    x = [[1,-2,5],[1,-2,-5],[1,2,5],[1,2,-5]]
    y = [[25], [19], [33], [23]]
    test2 = find_beta(x,y)
    print(test2)