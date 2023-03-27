"""This module uses user-defined functions in Lab1_bai1, Lab3_bai2.
This module includes the following user-defined functions:
1. Tranpose(arr) function
2. Mul(arr_x,arr_y) function for multiplication of two matrices
3. ANOVA(x,mty) to return the ANOVA table for Simple Linear Regression.
   All the codes are written in Python 3"""
import Lab1_bai1 as Lb1
import Lab3_bai2 as Lb6

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
def ANOVA(x,mty):

    """This function perform ANOVA for Simple Linear Regression
    Input:
    x: a list of int/float
    mty: a list of int/float
    Output:
    A string which represents ANOVA table for linear regression
    """
    y = []
    for i in mty:
        y += [[i]]

    beta0, beta1 = Lb6.Regression(x,mty)
    n = Lb1.Len(x)

    y_hat = [0 for i in range(n)]
    for i in range(n):
        y_hat[i] = beta0 + beta1*x[i]
    YT = Transpose(y)
    Eyi = 0
    for i in mty:
        Eyi += i
    Eyi2 = Eyi**2
    Exiyi = 0
    for i in range(n):
        Exiyi += x[i]*mty[i]

    Exi = 0
    for i in x:
        Exi += i
    Exi2_each = 0
    for i in x:
        Exi2_each += i*i
    YTy = Mul(YT,y)

    SST = YTy[0][0] - 1/n * Eyi2
    SSE = SST - beta1 * (Exiyi - 1/n * Exi*Eyi)
    SSR = SST - SSE
    MSR = SSR
    MSE = SSE/(n - 2)
    F_value = MSR/MSE
    return f'*Tổng bình phương: \n  SSR = {SSR}\n  SSE = {SSE}\n  SST = {SST}\n'\
           f'*Bậc tự do của: SSR = 1; SSE = {n-2}; SST = {n-1}\n'\
           f'*Trung bình bình phương:\n  MSR = {MSR}\n  MSE = {MSE}\n'\
           f'  F_value = {F_value}'
if __name__ == "__main__":
    #Data test 1
    x1 = [40,44,46,48,52,58,60,68,74,80]
    y1 = [6,10,12,14,16,18,22,24,26,32]
    a = ANOVA(x1,y1)
    print('DATA TEST 1:\n',a)

    #Data test 2
    x2 = [0,2,3,4,6,8,12,35]
    y2 = [18,32,64,45,91,127,164,541]
    b = ANOVA(x2,y2)
    print('*********************************************\nDATA TEST 2: \n',b)

    # Data test 3

    x3 = [49, 145, 57, 153, 92, 83, 117, 142, 69, 106, 109, 121]
    y3 = [12210, 17590, 13215, 19200, 14600, 14100,
          17100, 18400, 14100, 15500, 16300, 17020]
    test3 = ANOVA(x3, y3)
    print('*********************************************\nDATA TEST 3: ', test3)