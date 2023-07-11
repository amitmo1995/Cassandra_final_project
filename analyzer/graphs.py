import matplotlib.pyplot as plt
import numpy as np
from analyze_functions import analyze_functions

any_without=[35, 41, 43, 45, 47, 49, 56, 58, 60, 62, 64, 66, 72, 74, 77, 79]
any_with=[34, 36, 39, 45, 47, 52, 54, 57, 59, 61, 65, 68, 69, 72, 74, 78]
one_without=[33, 37, 39, 41, 42, 47, 51, 53, 58, 60, 64, 67, 71, 74, 75, 81]
one_with=[33, 35, 38, 45, 48, 52, 54, 60, 64, 67, 69, 76, 77, 79]
quarum_without=[32, 34, 37, 40, 43, 46, 50, 54, 57, 60, 62, 65, 67, 68, 71, 74, 76, 78, 79]
quarum_with=[34, 40, 42, 45, 47, 51, 53, 57, 59, 62, 64, 65, 69, 71, 73, 74, 76, 77, 78]
plt.subplot(121)
plt.title("using")
plt.bar(["ONE","ANY","QUARUM"], [len(one_with),len(any_with),len(quarum_with)],width=0.4)
plt.subplot(122)
plt.title("not_using")
plt.bar(["ONE","ANY","QUARUM"], [len(one_without),len(any_without),len(quarum_without)],width=0.4)
plt.show()

any_without=[32, 33, 34, 36, 35, 37, 38, 39, 40, 43, 41, 46, 44, 47, 42, 49, 48, 50, 45, 51, 52, 53, 55, 56, 60, 57, 59, 54, 65, 58, 62, 61, 64, 63, 67, 66, 68, 69, 70, 71, 74, 73, 80, 75, 76, 78, 72, 79, 77, 81]
any_with=[32, 34, 39, 35, 37, 33, 38, 40, 36, 41, 42, 43, 45, 46, 44, 48, 47, 49, 50, 52, 54, 51, 56, 53, 55, 58, 57, 62, 60, 63, 59, 61, 65, 66, 64, 67, 70, 69, 68, 72, 73, 71, 77, 74, 75, 76, 80, 78, 79, 81]
one_without=[33, 35, 32, 34, 36, 39, 37, 41, 38, 43, 42, 40, 44, 45, 46, 49, 47, 48, 51, 54, 52, 53, 50, 55, 56, 58, 60, 57, 62, 61, 64, 65, 66, 59, 63, 68, 67, 69, 70, 72, 71, 74, 76, 75, 73, 77, 78, 79, 80, 81]
one_with=[32, 34, 33, 39, 35, 36, 38, 37, 40, 41, 42, 44, 45, 47, 43, 46, 51, 49, 50, 52, 53, 48, 55, 54, 56, 57, 59, 60, 63, 58, 61, 62, 66, 64, 65, 70, 67, 71, 68, 69, 72, 75, 76, 77, 80, 78, 73, 81, 74, 79]
quarum_without=[33, 32, 36, 34, 35, 38, 37, 40, 42, 39, 41, 44, 43, 49, 52, 46, 47, 50, 51, 48, 53, 54, 57, 45, 55, 59, 58, 61, 66, 60, 63, 62, 64, 69, 67, 68, 65, 56, 71, 73, 70, 72, 77, 76, 80, 75, 79, 78, 74, 81]
quarum_with=[32, 33, 35, 34, 36, 37, 38, 39, 41, 40, 43, 42, 44, 46, 45, 50, 47, 48, 49, 52, 51, 57, 53, 54, 56, 58, 55, 61, 59, 60, 65, 62, 67, 64, 63, 66, 68, 77, 70, 75, 73, 78, 76, 69, 81, 80, 72, 71, 74, 79]

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

plt.subplot(325)
plt.title("QUARUM")
plt.plot(range(len(quarum_without)), quarum_without)
plt.subplot(326)
plt.title("QUARUM_using")
plt.plot(range(len(quarum_with)), quarum_with)


plt.show()