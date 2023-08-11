
import matplotlib.pyplot as plt
import numpy as np

def remove_insert_delete(arr):
    toRem=[]
    res=[]
    for i in range(len(arr)):
        if int(arr[i]) <= 30 or int(arr[i]) > 80:
            toRem.append(arr[i])
    for i in toRem:
        arr.remove(i)
    for i in arr:
        res.append(int(i))
    return res

coor1=remove_insert_delete(['1', '8', '17', '26', '28', '31', '37', '44', '47', '57', '58', '62', '67', '69'])
coor2=remove_insert_delete(['3', '6', '11', '14', '12', '19', '20', '21', '29', '36', '41', '49', '52', '55', '59', '63', '65', '66', '72', '74', '79'])
coor3=remove_insert_delete(['2', '5', '9', '10', '13', '18', '23', '24', '27', '34', '32', '35', '38', '43', '45', '51', '54', '61', '64', '70', '71', '73', '75', '78'])
coor4=remove_insert_delete(['0', '4', '7', '15', '16', '22', '25', '30', '33', '39', '40', '42', '46', '48', '53', '50', '56', '60', '68', '76', '77'])



print(coor1)
print(coor2)
print(coor3)
print(coor4)


plt.plot(range(len(coor1)), coor1, label = "coordinator1")
plt.plot(range(len(coor2)), coor2, label = "coordinator2")
plt.plot(range(len(coor3)), coor3, label = "coordinator3")
plt.plot(range(len(coor4)), coor4, label = "coordinator4")
plt.legend()
plt.show()