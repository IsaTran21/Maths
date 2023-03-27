"""This module uses user-defined functions in Lab1_bai1 as well as functions in scipy library.
This module has 1 function: Variance_test(x,sigma_0,option="less",alpha=0.05)
All the codes are written in Python 3"""

import Lab1_bai1 as Lb1
from scipy.stats import chi2

def Variance_test(x,sigma_0,option="less",alpha=0.05):
    """This function performs Chi-Square Test for the Variance
    Input:
    1. x: a list of data
    2. sigma: known/hypothesized sigma
    3. option: default is 'less' for < , other options are: 'diff' for ≠, 'greater' for >
    4. alpha = 0.05
    Output: a string which states p-value and whether accept or reject H0 hypothesis based on p-value"""


    s2 = Lb1.Variance(x)# The variance of x
    sigma2 = sigma_0 * sigma_0
    n = Lb1.Len(x)
    X2 = (n - 1)*s2/sigma2

    if option == "diff":
        p_value_1 = 1 - chi2.cdf(x=X2, df=n - 1)
        p_value_2 = chi2.cdf(x=X2, df=n - 1)
        min = p_value_1
        if p_value_2 < min:
            min = p_value_2
        p_value = 2 * min
    elif option == "greater":
        p_value = 1 - chi2.cdf(x=X2, df=n - 1)
    else:
        p_value = chi2.cdf(x=X2, df=n - 1)

    if p_value <= alpha:
        return f'p_value = {p_value}, reject H0'
    else:
        return f'p_value = {p_value}, accept  H0'
if __name__ == "__main__":

    #Data test 1
    x1 = [501.4, 498.0, 498.6, 499.2, 495.2, 501.4, 509.5, 494.9, 498.6, 497.6,
    505.5, 505.1, 499.8, 502.4, 497.0, 504.3, 499.7, 497.9, 496.5, 498.9,
    504.9, 503.2, 503.0, 502.6, 496.8, 498.2, 500.1, 497.9, 502.2, 503.2]
    sigma1 = 4
    test1 = Variance_test(x1,sigma_0=sigma1,option="less")
    print('DATA TEST 1: ',test1)

    #Data test 2
    x2 = [64.37, 64.26, 64.22, 64.42, 64.13, 64.44, 64.64, 64.19, 63.85, 64.17, 64.21,
          64.23, 64.64, 64.12, 63.98, 64.34, 64.20, 64.31, 64.15, 64.09, 64.33, 64.19, 64.57, 64.19]
    sigma2 = 0.15
    test2 = Variance_test(x=x2, sigma_0=sigma2,option='greater')
    print('*****************************************************\nDATA TEST 2: ',test2)