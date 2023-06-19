import json
import ast
import datetime

def convert_to_dictionary(txt_file):
    data=[]
    flag=0
    with open(f'inputs/{txt_file}', 'r') as file:
        for line in file:
            txt=""
            for ch in line:
                if ch=='[':
                    flag=1
                if flag==1:
                    txt+=ch
                if ch=="]":
                    flag=0
            data.append(txt)
            txt=""
    parsed_array = []
    for string in data:
        # Use eval to evaluate the string as a Python object
        parsed = eval(string)
        parsed_array.append(parsed)
    # Access the parsed array
    dictionary={}
    for row in parsed_array:
        for item in row:
            print(item)
            dictionary[int(item[0])]=item[1].timestamp()
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict


res=convert_to_dictionary("20queries_rep3_insert6_update10_delete4_numOfThreads10_withoutTS_res.txt")
print(res)
counter=0
keys_list=list(res.keys())

prev=keys_list[0]
for i in keys_list[1:]:
    if i<prev:
        counter+=1
    prev=i
print(keys_list)
print(f'num of conflicts is: {counter}')