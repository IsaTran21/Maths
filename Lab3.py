"""This module use user-defined functions in Lab1_bai1 as well as functions in scipy library.
This module include 1 function: OneSampleTest(x, u, option='less', sigma=None, alpha=0.05)
All the codes are written in Python 3"""

import scipy.stats as ss
import Lab1_bai1 as Lb1

def OneSampleTest(x, u, option='less', sigma=None, alpha=0.05):
    """This function performs one-sample test for average
    Input:
    1. x: a list of data
    2. u: known/hypothesized mean
    3. option: default is 'less' for <, other options are: 'diff' for ≠, 'greater' for >
    4. alpha: default is 0.05 (significance of level)
    5. sigma: default is None
    Output: a string which states p_value and whether or not accept or reject H0 hypothesis
    """
    average_x = Lb1.Mean(x)
    n = Lb1.Len(x)
    sqrt_n = Lb1.sqrt(n)


    if sigma == None:

        temp = 0  # Sum of all (xi - average_x)^2
        for i in x:
            temp += (i - average_x) ** 2
        s2 = 1 / (n - 1) * temp
        s = Lb1.sqrt(s2)
        t = (average_x - u) / (s / sqrt_n)

        if option == "greater":
            p_t = ss.t.cdf(t, n - 1)
            p_value = 1 - p_t
        elif option == "diff":
            p_t = ss.t.cdf(Lb1.Abs(t), n - 1)
            p_value = 2 * (1 - p_t)
        else:#when option='less'
            p_t = ss.t.cdf(t, n - 1)
            p_value = p_t

    if sigma != None:
        z = (average_x - u) / (sigma / sqrt_n)

        if option == "greater":
            p_z = ss.norm.cdf(z)
            p_value = 1 - p_z
        elif option == "diff":
            p_z = ss.norm.cdf(Lb1.Abs(z))
            p_value = 2 * (1 - p_z)
        else:
            p_z = ss.norm.cdf(z)
            p_value = p_z

    if p_value < alpha:
        return f'p_value = {p_value} => Bac bo gia thuyet H0'
    else:
        return f'p_value = {p_value} => Chap nhan gia thuyet H0'

#Testing for the OneSampleTest function
if __name__ == "__main__":
    
    #Data test 1
    x1 = [307, 293, 293, 283, 294, 297]
    alpha1 = 0.05
    u1 = 285
    #When sigma is not known
    test1 =  OneSampleTest(x1,u=u1,option='diff')
    print('DATA TEST 1: when sigma is not known: ', test1)
    #When sigma is known
    test1_1 = OneSampleTest(x1,u=u1,option='diff',sigma=10)
    print('DATA TEST 1: when sigma is known: ',test1_1)


    #Data test 2
    x2 = [0.593, 0.142, 0.329, 0.691, 0.231, 0.793, 0.519, 0.392, 0.418]
    u2 = 0.3
    alpha2 = 0.01
    test2 = OneSampleTest(x=x2, u=u2, alpha=alpha2, option='greater')
    print('***********************************************\nDATA TEST 2: when sigma is not known: ',test2)