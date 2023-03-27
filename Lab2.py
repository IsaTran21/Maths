"""This module uses functions in Lab1_bai1 and is written in Python 3 only
This module include 1 function:CI(x,sigma=None,(1-alpha)100% confidence_level=0.95)"""

import Lab1_bai1 as Lb1
import scipy.stats as ss
def CI(x,sigma=None,confidence_level=0.95):
    """Input: x is a list with n elements, sigma=None and confidence_level=0.95 as default values
       Output: a tuple containing: a lower estimate and an upper estimate of mean"""
    alpha = 1 - confidence_level
    n = Lb1.Len(x)
    mean_x = Lb1.Mean(x)
    #When sigma is not known, use t-test

    if sigma == None:
        s2 = Lb1.Variance(x)
        std = Lb1.sqrt(s2)
        epsilon = ss.t.ppf(alpha/2,n-1) * std/Lb1.sqrt(n)
        return mean_x - Lb1.Abs(epsilon), mean_x + Lb1.Abs(epsilon)

    #When sigma is known beforehand, use z-test
    if sigma != None:
        epsilon = ss.norm.ppf(alpha/2)*sigma/Lb1.sqrt(n)
        return mean_x - Lb1.Abs(epsilon), mean_x + Lb1.Abs(epsilon)

#Testing the CI function
if __name__ == "__main__":

    #data set1
    x = [307, 293, 293, 283, 294, 297]
    mean = 285
    # When sigma is == None
    test1 = CI(x, confidence_level=0.95)
    print('DATA TEST 1: SIGMA==NONE',test1)
    #when sigma is != None
    sigma = 10
    test2 = CI(x,sigma=sigma,confidence_level=0.95)
    print('DATA TEST 1: SIGMA!=NONE',test1)

    #data set2
    x2 = [1.60, 1.77, 1.61, 1.08, 1.07, 1.79, 1.34, 1.07, 1.45, 1.59, 1.43, 2.07, 1.16, 0.85, 2.11]
    mean2 = 1.20

    # When sigma is == None
    test3 = CI(x2, confidence_level=0.95)
    print('************************************************************\nDATA TEST 2: SIGMA==NONE',test3)
    # when sigma is != None
    sigma2 = 0.32
    test4 = CI(x2, sigma=sigma2, confidence_level=0.95)
    print('DATA TEST 2: SIGMA!=NONE',test4)



