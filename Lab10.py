"""This module uses user-defined functions in Lab1_bai1, Lab5_bai1 as Lb5 as well as functions in scipy library
This module includes the following user-defined functions:
1. Tranpose(arr) function
2. Mul(arr_x,arr_y) function for multiplication of two matrices
3. PREDICT(x,y,x0,confidence=0.95).
All the codes are written in Python 3"""

import Lab1_bai1 as Lb1
from scipy.linalg import inv
import scipy.stats as ss
import Lab5_bai1 as Lb5
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


def PREDICT(x,y,x0,confidence=0.95):
    """Input:
    1. x: a list (matrix with dimension k x 3)
    2. y: a list (matrix with dimension k x 1)
    3. x0: a list (matrix with dimension 1 x 3)
    4. 100(1 - α)% confidence interval (default 0.95)
    Output: a string which states the prediction interval of y0 based on x0 with
            a certain confidence interval and y0"""
    n = len(x)

    beta = Lb5.find_beta(x,y)

    y0 = Mul(x0,beta)

    y_mu_hat = Mul(x,beta)

    e = [0 for i in range(len(y))]

    k = len(x[0]) - 1
    for i in range(len(y)):
        e[i] = [y[i][0] - y_mu_hat[i][0]]

    et = Transpose(e)

    sigma_hat_squared = Mul(et,e)[0][0]/(n - (k+1))

    t = ss.t.ppf(1-(1-confidence)/2,n-(k+1))

    x0T = Transpose(x0)

    XT = Transpose(x)

    XTX = Mul(XT, x)

    XTX_ivs = inv(XTX)

    xXTX_inv = Mul(x0,XTX_ivs)
    xXTX_inv_x0T = Mul(xXTX_inv,x0T)

    epsilon = t * Lb1.sqrt(sigma_hat_squared * (1+xXTX_inv_x0T[0][0]))

    return f"y0 = {y0[0][0]}\nKhoảng tin cậy 95%CI của y0:\n[{y0[0][0] - epsilon},{y0[0][0] + epsilon}]"


if __name__ == "__main__":
    #Data test 1
    x = [[1,1.7, 10.8], [1, 6.3, 9.4],[1, 6.2, 7.2],[1,6.3, 8.5],
         [1, 10.5, 9.4],[1, 1.2, 5.4],[1, 1.3, 3.6],[1, 5.7, 10.5],
         [1, 4.2, 8.2],[1, 6.1, 7.2]]
    y = [[25], [31], [26],[38],[18],[27],[29],[17],[35],[21]]
    test1 = PREDICT(x,y,x0=[[1,2,10]])
    print('DATA TEST 1: \n',test1)

    #Data test 2
    x2 = [[1,2,50],[1,8,110],[1,11,120],[1,10,550],[1,8,295],
          [1,4,200],[1,2,375],[1,2,52],[1,9,100],[1,8,300],
          [1,4,412],[1,11,400],[1,12,500],[1,2,360],[1,4,205],
          [1,4,400],[1,20,600],[1,1,585],[1,10,540],[1,15,250],
          [1,15,290],[1,16,510],[1,17,590],[1,6,100],[1,5,400]]

    y2 = [[9.95], [24.45], [31.75], [35.0], [25.02], [16.86], [14.38],
           [9.6], [24.35], [27.5], [17.08], [37.0], [41.95], [11.66], [21.65],
           [17.89], [69.0], [10.3], [34.93], [46.59], [44.88], [54.12],
           [56.63], [22.13], [21.15]]
    test2 = PREDICT(x2,y2,x0=[[1,8,275]])
    print('*******************************************\nDATA TEST 2: \n',test2)



