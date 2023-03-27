"""input: x or arr is an array with n elements, write functions for:
Mean, Variance, Std, Mode, Median, Quartile 1, Quartile 3, IQR, CV
All the codes in this project are written in Python 3
For descriptive statistics, this module includes:
1. The Mean function
2. The Variance function
3. The Std function
4. The Q1 function
5. The Q3 function
6. the IQR function
7. The Median function
8. The Mode function
9. The CV function
10. Other user-defined functions: Len, sqrt, Sort, Divide_Sequence, Abs, Set"""
#The Len function
def Len(x):
    count = 0
    for i in x:
        count += 1
    return count

#The square root function
def sqrt(n):
    root = n/2
    for k in range(20):
        root = (1/2)*(root + (n / root))
    return root

#The Mean function
def Mean(x):
    result = 0
    len_x = Len(x)
    for i in x:
        result += i
    return result/len_x

#The variance function - s^2
def Variance(x):
    mean_x = Mean(x)
    n_1 = Len(x) - 1 #n minus 1
    #Sum of all (xi - mean)^2 saved in temp
    temp = 0
    for i in x:
        temp += (i - mean_x)**2
    result = 1/(n_1) * temp
    return result

#The standard variation function
def Stand(x):
    s2 = Variance(x)
    s = sqrt(s2)
    return s

#The sort function
def Sort(arr):
    """Bubble sort"""
    array = arr[:]
    n = Len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#The Median function
def Median(arr):
    """Return the Median for even and odd numbers of elements in an array
    the len of the array must be greater than 1"""

    n = Len(arr)
    if n == 1:
        print('Wrong input')

    array = Sort(arr)#To sort the array into ascending order

    if n % 2 == 0:
        # Even numbers of elements
        Middle = n // 2 #the position of the median number is in the n//2th
        result = (array[Middle-1] + array[Middle])/2#minus 1 because of the Python indexing rule (start from 0)
    else:
        # Odd numbers of elements
        Middle = n // 2
        result = array[Middle]

    return result


def Divide_Sequence(arr):
    """This function is used for dividing an array into two equal parts
    which is then used for Q1 and Q3"""
    middle = Len(arr)//2
    if Len(arr) % 2 == 0:
        lower = arr[0:middle]
        upper = arr[middle:Len(arr)]
    else:
        lower = arr[0:middle]
        upper = arr[middle+1:Len(arr)]
    return lower, upper

#The quartile 1 function
def Q1(x):

    arr = Sort(x)#To sort the array into ascending order
    Lower, Upper = Divide_Sequence(arr)#Divide the array into 2 equal parts
    result = Median(Lower)#The Q1 is the Median of the smaller part.
    return result

#The quartile 3 function
def Q3(x):
    arr = Sort(x) #To sort the array into ascending order
    Lower, Upper = Divide_Sequence(arr)#Divide the array into 2 equal parts
    result = Median(Upper)#The Q3 is the Median of the larger part.
    return result

#The Interquartile Range function
def IQR (arr):
    result = Q3(arr) - Q1(arr)
    return result

#The absolute value function
def Abs(num):
    if num < 0:
        return -1 * num
    else:
        return num
#The user-defined set function, which returns a set
def Set(arr):
    result = []
    for i in arr:
        if i not in result:
            result += [i]
    return result


def Mode(arr):
    """This function returns the value(s) that appears most frequently in a data set
    There are <=2 modes in a data set, if the same most frequent values >=3 => there is no mode"""
    all_variables = Set(arr)#To sort the array into ascending order

    # create a container the 0th position is the value and the 1st is its corresponding number of occurrences
    list_variables = [[x, 0] for x in all_variables]


    for i in range(Len(all_variables)):
        for j in arr:
            if all_variables[i] == j:
                list_variables[i][1] += 1

    max_position = [list_variables[0]]
    for i in list_variables:
        if i[1] >= max_position[0][1]:
            max_position = [i]

    for i in list_variables:
        if i[1] == max_position[0][1] and i[0] != max_position[0][0]:
            max_position += [i]

    if Len(max_position) >= 3:
        return None #There is no Mode
    else:
        if Len(max_position) == 2:
            return max_position[0][0],max_position[1][0]#If there are 2 modes
        else:
            return max_position[0]#If there is 1 mode


#The CV function
def CV(arr):
    std = Stand(arr)
    mean = Mean(arr)
    return std/mean

#Testing the functions above
if __name__ == "__main__":
    import random

    random.seed(10)
    #File data_bai1.txt will contain the same set of data and can be coppied for further testing
    data_bai1 = []
    for i in range(1000):
        data_bai1 += [random.randint(-1000, 1000)]
    with open('data_bai1.txt', 'w') as f:
        for i in data_bai1:
            f.write(str(i))
            f.write(',')

    Variance_of_x = Variance(data_bai1)
    Std_of_x = Stand(data_bai1)
    Mean_of_x = Mean(data_bai1)
    Median_of_x = Median(data_bai1)
    CV_of_x = CV(data_bai1)
    Mode_of_x = Mode(data_bai1)
    Q1_of_x = Q1(data_bai1)
    Q3_of_x = Q3(data_bai1)
    IQF_of_x = IQR(data_bai1)
    print(f'Variance = {Variance_of_x}\nStd = {Std_of_x}\nMean = {Mean_of_x}\nMedian = {Median_of_x}\n'
          f'CV = {CV_of_x}\nMode = {Mode_of_x}\nQ1 = {Q1_of_x}\nQ3 = {Q3_of_x}\nIQR = {IQF_of_x}')


