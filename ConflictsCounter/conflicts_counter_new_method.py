import json
import ast
import datetime

def convert_to_dictionary(txt_file):
    data=[]
    flag=0
    with open(f'{txt_file}', 'r') as file:
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


path= "C:\Users\Amit\PycharmProjects\pythonProjects\cassandra_final_project\Cassandra_final_project-main\ConflictsCounter\Comp_repFac3_all_methods\ONE\NOTUSINGTS\100queries_rep3_insert30_update50_delete20_numOfThreads10_withoutTS_ONE_res.json"
res=convert_to_dictionary(path)

print(res)
counter=0
keys_list=list(res.keys())

prev=keys_list[0]
for i in keys_list[1:]:
    if i<prev:
        print(f'conflict on: {prev}->{i}')
        counter+=1
    prev=i
print(keys_list)
print(f'num of conflicts is: {counter}')