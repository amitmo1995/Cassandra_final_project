import json
import re
import datetime

path=input("enter file full path: ")
file_out=open(f'{path}_counted_results','w')
with open(f'{path}', 'r') as file:
    content=json.load(file)
    time=0
    q_num=0
    q_time_dict={}
    not_happened=[]
    insertDuration = []
    updateDuration = []
    deleteDuration = []
    for i in range(len(content)):
        time=0
        str=""
        print(content[i]['query'])
        if "INSERT" in content[i]['query']:
            seconds, microseconds = content[i]['duration'].split('.')
            insertDuration.append(int(microseconds))
            print(microseconds)
        elif "UPDATE" in content[i]['query']:
            seconds, microseconds = content[i]['duration'].split('.')
            updateDuration.append(int(microseconds))
            print(microseconds)
        elif "DELETE" in content[i]['query']:
            seconds, microseconds = content[i]['duration'].split('.')
            deleteDuration.append(int(microseconds))
            print(microseconds)
print("insert",insertDuration)
print("update",updateDuration)
print("delete",deleteDuration)

avgIn=sum(insertDuration) / len(insertDuration)
avgUp=sum(updateDuration) / len(updateDuration)
avgDel=sum(deleteDuration) / len(deleteDuration)

print("inAVG",avgIn)
print("upAVG",avgUp)
print("delAVG",avgDel)
file_out.close()