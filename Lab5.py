"""This module uses user-defined functions in Lab1_bai1 as well as functions in scipy library
This module has 1 function: Independent_Sample_test(x,y,sigma_x = None,nx=None, my=None,sigma_y = None,option="diff",alpha = 0.05)
All the codes are written in Python 3"""

import Lab1_bai1 as Lb1
import scipy.stats as ss
def Independent_Sample_test(x,y,sigma_x = None,nx=None, my=None,sigma_y = None,option="diff",alpha = 0.05):

    """This function performs  Independent Sample test between two groups
    Input:
    1. x: list of data in group x or if x is not a list, x is a float/int (known/hypothesized average of group x)
    2. y: list of data in group y, y is a float/int (known/hypothesized average of group y)
    3. sigma_x, sigma_y:
              + if sigma_x = '0' and sigma_y = '0' which means sigma_x = sigma_y and they are both not known yet,
              the function then calculates std of x and std of y
              + if sigma_x = '1' and sigma_y = '1' which means sigma_x ≠ sigma_y and they are both not known yet,
              the function then calculates std of x and std of y
              + if sigma_x and sigma_y ∉ {0,1} then sigma_x and sigma_y are provided, therefore
                function will use sigma_x and sigma_y for further calculating, no need to calculate
                std of x and std of y
    4. option: default is 'diff' for ≠ , other options are: 'less' for <, 'greater' for >
    5. alpha: 0.05 as a default
    6. n, m:default None or else the known length of x and y groups respectively if x and y are float/int and
        sigma_x and sigma_y are known and sigma_x = sigma_y"""


    if isinstance(x, list) and isinstance(y, list):
        not_known_sigma = ['0', '1']

        mean_x = Lb1.Mean(x)
        mean_y = Lb1.Mean(y)
        n_x = Lb1.Len(x)
        n_y = Lb1.Len(y)
        if sigma_x not in not_known_sigma and sigma_y not in not_known_sigma: #sigma_x == sigma_y

            z = (mean_x - mean_y)/Lb1.sqrt(sigma_x**2/n_x + sigma_y**2/n_y)
            if option == "diff":
                p_value = 2 * (1 - ss.norm.cdf(Lb1.Abs(z)))
            elif option == "less":
                p_value = ss.norm.cdf(z)
            else:
                p_value = 1 - ss.norm.cdf(z)
            if p_value < alpha:
                return f'p_value = {p_value}, reject H0'
            else:
                return f'p_value = {p_value}, not reject H0'

        if sigma_x in not_known_sigma and sigma_y in not_known_sigma and sigma_x != sigma_y:
            print('Wrong input')
        if sigma_x in not_known_sigma and sigma_y in not_known_sigma and sigma_x == sigma_y:

            std_x_squared = Lb1.Variance(x)
            std_y_squared = Lb1.Variance(y)
            if sigma_x == '0' and sigma_y == '0':

                sp_squared = ((n_x - 1)*std_x_squared + (n_y - 1)*std_y_squared)/(n_x + n_y - 2)
                t = (mean_x - mean_y)/(Lb1.sqrt(sp_squared) * Lb1.sqrt(1/n_x + 1/n_y))
                if option == "diff":
                    p_value = 2 * (1 - ss.t.cdf(Lb1.Abs(t),df=(n_x + n_y - 2)))
                elif option == "less":
                    p_value = ss.t.cdf(t,df=(n_x + n_y - 2))
                else:
                    p_value = 1 - ss.t.cdf(t,df=(n_x + n_y - 2))

            if sigma_x == '1' and sigma_y == '1':
                df = (std_x_squared/n_x + std_y_squared/n_y)*(std_x_squared/n_x + std_y_squared/n_y)/((std_x_squared/n_x)*(std_x_squared/n_x)/(n_x - 1) + (std_y_squared/n_y)*(std_y_squared/n_y)/(n_y - 1))
                v = int(df//1)
                t = (mean_x - mean_y)/Lb1.sqrt(std_x_squared/n_x + std_y_squared/n_y)
                if option == "diff":
                    p_value = 2 * (1 - ss.t.cdf(Lb1.Abs(t),df = v))
                elif option == "less":
                    p_value = ss.t.cdf(t, df=v)
                else:
                    p_value = 1 - ss.t.cdf(t, df=(v))

            if p_value < alpha:
                return f'p_value = {p_value}, reject H0'
            else:
                return f'p_value = {p_value}, not reject H0'
    else:

        z = (x - y) / Lb1.sqrt(sigma_x ** 2 / nx + sigma_y ** 2 / my)

        if option == "diff":
            p_value = 2 * (1 - ss.norm.cdf(Lb1.Abs(z)))
        elif option == "less":
            p_value = ss.norm.cdf(z)
        else:
            p_value = 1 - ss.norm.cdf(z)
        if p_value < alpha:
            return f'p_value = {p_value}, reject H0'
        else:
            return f'p_value = {p_value}, not reject H0'
if __name__ == "__main__":

    #Data test 1: not known sigma_x=='0' and not known sigma_y = '0'
    x1 = [187.6, 180.3, 198.6, 190.7, 196.3, 203.8, 190.2, 201.0, 194.7, 221.1, 186.7, 203.1]
    y1 = [148.1,146.2,152.8,135.3,151.2,146.3,163.5,146.6,162.4,140.2,159.4,181.8,165.1,165.0,141.6]
    sigma_x1 = '0'
    sigma_y1 = '0'
    test_1 = Independent_Sample_test(x=x1,y=y1,sigma_x=sigma_x1, sigma_y= sigma_y1,option="less")
    print("DATA TEST 1 (not known sigma_x=='0' and not known sigma_y = '0')",test_1,end='\n\n')

    # Data test 2: not known sigma_x=='1' and not known sigma_y = '1'
    x2 = [2.31, 25.23, 28.37, 14.16, 28.39, 27.94, 17.68]
    y2 = [0.85, 2.90, 2.47, 17.72, 3.82, 2.86, 13.71, 7.38]
    sigma_x2 = '1'
    sigma_y2 = '1'
    test_2 = Independent_Sample_test(x=x2, y=y2, sigma_x=sigma_x2, sigma_y=sigma_y2, option="greater")
    print("DATA TEST 2 (not known sigma_x=='1' and not known sigma_y = '1'): ",test_2,end='\n\n')

    # Data test 3: known sigma_x, mean of group x and known sigma_y, mean of group y and sigma_x = sigma_y
    x3 = 28
    y3 = 33
    sigma_x3 = 14.1
    sigma_y3 = 9.5
    n_x = 75
    n_y = 50
    alpha3 = 0.05
    test_3 = Independent_Sample_test(x=x3, y=y3, sigma_x = sigma_x3, sigma_y=sigma_y3, nx = n_x, my = n_y, option="greater",alpha=alpha3)

    print("DATA TEST 3 (known sigma_x, mean of group x and known sigma_y, mean of group y and sigma_x = sigma_y): ", test_3)


