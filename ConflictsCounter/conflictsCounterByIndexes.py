def conflictCounterByIndexes(arr):
    counter=0
    for index,i in enumerate(arr):
        if not(i==index+1) :
            counter+=1
    return counter

arr = [1, 2, 4, 3]
print("Number of conflicts:", conflictCounterByIndexes(arr))
