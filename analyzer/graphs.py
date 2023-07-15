import matplotlib.pyplot as plt
import numpy as np
from analyze_functions import analyze_functions

any_without=10
any_with=10
one_without=9
one_with=5

plt.subplot(121)
plt.title("not_using")
plt.bar(["ONE","ANY"], [one_without,any_without],width=0.4)
plt.subplot(122)
plt.title("using")
plt.bar(["ONE","ANY"], [one_with,any_with],width=0.4)
plt.show()

any_without=[30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 40, 42, 45, 43, 44, 46, 47, 48, 50, 49, 54, 52, 51, 53, 58, 55, 57, 56, 59, 60, 61, 62, 64, 66, 65, 67, 68, 71, 69, 70, 72, 74, 73, 75, 76, 77, 78, 79]
any_with=[30, 32, 31, 33, 35, 34, 37, 36, 38, 39, 40, 41, 42, 43, 44, 46, 45, 47, 48, 50, 49, 51, 52, 54, 55, 53, 56, 57, 58, 59, 60, 61, 62, 64, 63, 65, 66, 68, 67, 70, 71, 69, 72, 74, 73, 75, 76, 77, 78, 79]
one_without=[30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 41, 43, 44, 46, 47, 45, 48, 49, 50, 52, 51, 53, 54, 55, 56, 58, 60, 57, 59, 62, 61, 63, 64, 66, 65, 67, 69, 68, 70, 72, 71, 74, 73, 75, 76, 77, 78, 79]
one_with=[30, 31, 32, 33, 34, 36, 37, 35, 38, 39, 40, 42, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 56, 60, 61, 62, 63, 64, 66, 65, 67, 69, 68, 70, 71, 72, 76, 77]

plt.subplot(321)
plt.title("ONE")
plt.plot(range(len(one_without)), one_without)
plt.subplot(322)
plt.title("ONE_using")
plt.plot(range(len(one_with)), one_with)

plt.subplot(323)
plt.title("ANY")
plt.plot(range(len(any_without)), any_without)
plt.subplot(324)
plt.title("ANY_using")
plt.plot(range(len(any_with)), any_with)

plt.show()