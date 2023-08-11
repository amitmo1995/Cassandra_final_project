import matplotlib.pyplot as plt
import numpy as np
from analyze_functions import analyze_functions

analyzerObj=analyze_functions()

randomNumsArr100= np.random.randint(1,101,100)
randomNumsArr500= np.random.randint(1,101,500)
randomNumsArr1000= np.random.randint(1,101,1000)
randomNumsArr10000= np.random.randint(1,101,10000)

y=[]
y.append((analyzerObj.count_conflicts_by_mergeSort(randomNumsArr100)/(len(randomNumsArr100)*len(randomNumsArr100)))*100)
y.append((analyzerObj.count_conflicts_by_mergeSort(randomNumsArr500)/(len(randomNumsArr500)*len(randomNumsArr500)))*100)
y.append((analyzerObj.count_conflicts_by_mergeSort(randomNumsArr1000)/(len(randomNumsArr1000)*len(randomNumsArr1000)))*100)
y.append((analyzerObj.count_conflicts_by_mergeSort(randomNumsArr10000)/(len(randomNumsArr10000)*len(randomNumsArr10000)))*100)

x=[str(float('%.2f' % (y[0])))+"%\n100 queries",str(float('%.2f' % (y[1])))+"%\n500 queries",str(float('%.2f' % (y[2])))+"%\n1000 queries",str(float('%.2f' % (y[3])))+"%\n10000 queries"]


x = np.array(x)
y = np.array(y)

plt.subplot(221)
plt.title("conflict percentage")
plt.bar(x, y, color='hotpink',width=0.6)
plt.ylim(top=100)
plt.subplot(222)
plt.title("conflicts graph")
yPoints=y
xPoints=[100,500,1000,10000]
plt.plot(xPoints,yPoints,'-o',color='hotpink')
plt.ylim(top=100)
plt.subplot(223)
plt.title("time score(queries/ms)")
y=[]
y.append(analyzerObj.analyze_time_score(np.random.randint(1,100),100))
y.append(analyzerObj.analyze_time_score(np.random.randint(1,500),500))
y.append(analyzerObj.analyze_time_score(np.random.randint(1,1000),1000))
y.append(analyzerObj.analyze_time_score(np.random.randint(1,10000),10000))
plt.bar(["100","500","1000","10000"], y, color='red',width=0.6)
plt.subplot(224)
plt.title("time score(queries/ms) graph")
yPoints=y
xPoints=[100,500,1000,10000]
plt.plot(xPoints,yPoints,'-o',color='red')
plt.suptitle("generated without timestamp")
plt.show()