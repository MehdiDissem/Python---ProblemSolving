# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    last = 0
    if integers[0] % 2==0 and integers[2]%2==0:
        for ele in integers:
            if ele % 2 !=0:
                last = ele
    else: 
        for ele in integers:
            if ele%2 ==0:
                last = ele
    return last

    #or

def find_outlier(integers):
    if integers[0] % 2 == 1 and integers[1] % 2 == 1:
        for integer in integers[2::]:
            if integer % 2 == 0:
                return integer
    elif integers[0] % 2 == 0 and integers[1] % 2 == 0:
        for integer in integers[2::]:
            if integer % 2 == 1:
                return integer
    else:
        if integers[0] % 2 == integers[2] % 2:
            return integers[1]
        else:
            return integers[0]