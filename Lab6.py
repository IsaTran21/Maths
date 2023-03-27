"""This module uses user-defined functions in Lab1_bai1 as well as functions in scipy library.
This module has 1 function which is Regression (x, y,option=1)
All the codes are written in Python 3"""
from scipy import linalg
import Lab1_bai1 as Lb1

def Regression(x, y,option=1):
    """This function has two options for Simple Linear Regression (option=1)
       and 2nd Degree Polynomial Regression (option=2).
       Input:
       x, y: lists
       option: 1 (default) or 2.
       Output:
            + option = 1: β0, β1
            + option = 2: β0, β1, β2
     """
    # sum of xi
    n = Lb1.Len(x)
    Exi = 0
    for i in x:
        Exi += i
    # sum of y1
    Eyi = 0
    for i in y:
        Eyi += i
    # xum of xi and yi
    Exiyi = 0
    for i in range(n):
        temp = x[i] * y[i]
        Exiyi += temp
    # sum of xi^2
    Exi2 = 0
    for i in x:
        temp = i * i
        Exi2 += temp
    Exi3 = 0
    for i in x:
        temp = i * i * i
        Exi3 += temp
    Exi4 = 0

    for i in x:
        temp = i * i * i * i
        Exi4 += temp
    Exi2yi = 0
    for i in range(n):
        temp = x[i] * x[i] * y[i]
        Exi2yi += temp
    if option == 1:
        beta1 = (Exiyi - 1 / n * Exi * Eyi) / (Exi2 - 1 / n * ((Exi) ** 2))
        beta0 = 1 / n * Eyi - beta1 * 1 / n * Exi
        return beta0, beta1
    if option == 2:
        l1 = [n, Exi, Exi2]
        l2 = [Exi, Exi2, Exi3]
        l3 = [Exi2, Exi3, Exi4]
        l4 = [Eyi, Exiyi, Exi2yi]
        a = [l1, l2, l3]
        b = l4
        result = linalg.solve(a, b)
        return result
if __name__ == "__main__":
    #Data set 1: option = 1
    age = [0,2,3,4,6,8,12]
    weight = [18,32,64,45,91,127,164]
    a = Regression(x=age,y=weight)
    print('DATA SET 1: ',a)

    #Data set 2: option = 2

    weight_pig = [10,20,30,40,50,60,70,80,90]
    lean_meat = [18.4,20,23.7,25,26,26.6,24,23.8,19.4]
    b = Regression(x=weight_pig,y=lean_meat,option=2)
    print('DATA SET 2: ',b)