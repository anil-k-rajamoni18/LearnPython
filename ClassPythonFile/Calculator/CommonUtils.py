def findLength(string):
    return len(string)


def sumOfN(nums):
    res = 0
    for i in range(1,nums+1):
        res = res+i
    return res


def evenoddchecker(num):
    return num%2 == 0


def primeChecker(num):
    factors = 0
    for i in range(1,num+1):
        if num%i == 0:
            factors+=1
    return factors == 2