"""This module uses user-defined functions in Lab1_bai1, Lab3_bai2 as well as functions in scipy library
This module includes the following user-defined functions:
1. Tranpose(arr) function
2. Mul(arr_x,arr_y) function for multiplication of two matrices
3. KTC(x,mty,x0=None,confidence=0.99) to predict range of Beta1 and Beta0 and y0 (based on x0)
   with a certain Confidence level. All the codes are written in Python 3"""
import Lab1_bai1 as Lb1
import Lab3_bai2 as Lb6
from scipy.stats import t
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



def KTC(x,mty,x0,confidence=0.99):

    """This function calculates Confidence interval for beta0, beta1, and y0 in Simple Linear Regression
       with a certain confidence.
    Input: x: a list of numbers (int/float)
        y: a list of numbers (int/float)
        x0: the value which needed to be predicted
        confidence = 0.99 as a default
    Output:
        A string which states the Confidence interval for beta0, beta1, y0 (based on x0)."""
    y = []
    for i in mty:
        y += [[i]]

    alpha = 1 - confidence

    beta0, beta1 = Lb6.Regression(x,mty)

    n = Lb1.Len(x)

    y_hat = [0 for i in range(n)]
    for i in range(n):
        y_hat[i] = beta0 + beta1*x[i]
    YT = Transpose(y)
    mean_x = Lb1.Mean(x)
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
    Exi2 = Exi**2
    YTy = Mul(YT,y)

    SST = YTy[0][0] - 1/n * Eyi2
    SSE = SST - beta1 * (Exiyi - 1/n * Exi*Eyi)
    sigma_hat_squared = SSE/(n - 2)
    sigma_hat = Lb1.sqrt(sigma_hat_squared)
    Sxx = Exi2_each - 1/n * Exi2
    se_beta1 = sigma_hat/Lb1.sqrt(Sxx)

    se_beta0 = sigma_hat * Lb1.sqrt(1/n + mean_x*mean_x/Sxx)
    t_value = t.ppf(1-alpha / 2, n - 2)

    y0 = beta0 + beta1*x0
    epsilon_beta0 = t_value * se_beta0
    epsilon_beta1 = t_value * se_beta1

    epsilon_y = t_value*sigma_hat * Lb1.sqrt(1 + 1/n + (x0 - mean_x)**2/Sxx)

    return f'Khoảng tin cậy {confidence*100}% của :\nBeta1 = [{beta1 - epsilon_beta1},{beta1 + epsilon_beta1}]' \
           f'\nBeta0 = [{beta0 - epsilon_beta0},{beta0 + epsilon_beta0}]\n' \
           f'Dự đoán y0 ∈ [{y0 - epsilon_y};{y0 + epsilon_y}]'
if __name__ == "__main__":


    # Data test 1

    x1 = [49, 145, 57, 153, 92, 83, 117, 142, 69, 106, 109, 121]
    y1 = [12210, 17590, 13215, 19200, 14600, 14100,
          17100, 18400, 14100, 15500, 16300, 17020]
    test1 = KTC(x1, y1, x0=80, confidence=0.95)
    print('DATA TEST 1: ', test1)

    # Data test 3
    x2 = [3.3, 3.4, 3.4, 3.5, 3.6, 3.6,3.7, 3.7, 3.8, 3.8,
          3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 5.0, 5.1, 5.2]
    y2 = [17.78, 21.59, 23.84, 15.13, 23.45, 20.87,
          17.78, 20.09, 17.78, 12.46, 14.95,15.87,17.45,
          14.35,14.64,17.25,12.57,7.15,7.5,4.34]
    test2 = KTC(x2,y2,x0=4.0,confidence=0.95)
    print('\nDATA TEST 2: ',test2)


