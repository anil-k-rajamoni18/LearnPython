# first way of import 
#  import modulename

# import CommonUtils

# print(CommonUtils.primeChecker(67))
# print(CommonUtils.findLength("Python Session May"))
# print(CommonUtils.evenoddchecker(56))



# 2 way alias importing
# import CommonUtils as c;
# print(c.evenoddchecker(54))

# import math as m 
# print(m.pow(2,8))


# 3 - way 
# from modulename import methodname1, methodname2

# from CommonUtils import primeChecker , evenoddchecker

# print(primeChecker(68))
# print(evenoddchecker(10))

# from math import sqrt , factorial
# print(sqrt(100))
# print(factorial(5))


# 4 way  
#  will import all methods and we can access directly 
from CommonUtils import *


