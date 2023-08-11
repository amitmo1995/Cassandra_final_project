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
    for i in range(len(content)):
        time=0
        str=""
        for j in range(len(content[i]['events'])):
            if content[i]['events'][j]['description'] == "Adding to barak memtable":
                # print(content[i]['events'][j]['datetime'])
                str+="("+content[i]['events'][j]['datetime']+")"
                time=content[i]['events'][j]['datetime']
        if time==0:
            str+="(not happened)"
        # print("QUERY: ",end="")
        str+=" QUERY: "
        for j in range(len(content[i]['events'])):
            if ("INSERT" in content[i]['events'][j]['description']) or ("DELETE" in content[i]['events'][j]['description']) or ("UPDATE" in content[i]['events'][j]['description']):
                # print(content[i]['events'][j]['description'])
                str+=content[i]['events'][j]['description']
                op_num = re.search(r"'\d+'", content[i]['events'][j]['description'])
                if op_num:
                    # print(op_num.group().strip("'"))
                    str=op_num.group().strip("'")+str
                    if time:
                        q_time_dict[op_num.group().strip("'")]=time
                    else:
                        q_time_dict[op_num.group().strip("'")]=None
                    print(str)
                    file_out.write(f'{str}\n')
    print("===============queries did not added to barak memtables===============")
    file_out.write("===============queries did not added to barak memtables===============\n")
    for i in q_time_dict:
        if not(q_time_dict[i]):
            print(i)
            file_out.write(f'{i}\n')
    print("======================================================================")
    file_out.write("======================================================================\n")
    q_time_dict = {key: value for key, value in q_time_dict.items() if value is not None}
    sorted_dict = dict(sorted(q_time_dict.items(), key=lambda x: x[1]))
    print(sorted_dict)
    file_out.write("dict sorted by query time:\n")
    file_out.write(f'{sorted_dict}\n')
    keys_arr=list(num for num in (int(num) for num in sorted_dict.keys()) if 30 <= num <= 79)
    # num for num in numbers if 30 <= num <= 79
    prev=keys_arr[0]
    conf_count=0
    print(keys_arr)
    for temp in keys_arr[1:]:
        if (int(temp)<int(prev)) and (int(temp)>=30) and (int(temp)<80):
            conf_count+=1
            print(f'{prev} -> {temp}')
            file_out.write(f'{prev} -> {temp}\n')
        prev=temp
    print(conf_count)
    file_out.write(f'conflicts counter: {conf_count}\n')
file_out.close()