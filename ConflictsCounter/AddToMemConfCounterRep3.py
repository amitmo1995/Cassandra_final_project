import json
import re
import datetime

path=input("enter file full path: ")
file_out=open(f'{path}_counted_results','w')
rep1=[]
rep2=[]
rep3=[]
repsIp=[]
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
                if not(content[i]['events'][j]['source'] in repsIp):
                    repsIp.append(content[i]['events'][j]['source'])
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
                        q_time_dict[op_num.group().strip("'")]=(time,content[i]['events'][j]['source'])
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
    sorted_dict = dict(sorted(q_time_dict.items(), key=lambda x: x[1][0]))
    print(sorted_dict)
    file_out.write("dict sorted by query time:\n")
    file_out.write(f'{sorted_dict}\n')
    keys_arr=list(num for num in (int(num) for num in sorted_dict.keys()) if 30 <= num <= 79)
    # num for num in numbers if 30 <= num <= 79


    ip_29_keys = []
    ip_39_keys = []
    ip_27_keys = []
    ip_28_keys = []

    # Split and sort the keys based on value[1]
    for key, (date_time, ip_address) in sorted_dict.items():
        if ip_address == '62.90.89.29':
            ip_29_keys.append(key)
        elif ip_address == '62.90.89.39':
            ip_39_keys.append(key)
        elif ip_address == '62.90.89.27':
            ip_27_keys.append(key)
        elif ip_address == '62.90.89.28':
            ip_28_keys.append(key)

    print("Keys for IP 62.90.89.29:", ip_29_keys)
    print("Keys for IP 62.90.89.39:", ip_39_keys)
    print("Keys for IP 62.90.89.27:", ip_27_keys)
    print("Keys for IP 62.90.89.28:", ip_28_keys)

    prev = ip_27_keys[0]
    conf_count27 = 0
    print(ip_27_keys)
    for temp in ip_27_keys[1:]:
        if (int(temp) < int(prev)) and (int(temp) >= 30) and (int(temp) < 80):
            conf_count27 += 1
            print(f'{prev} -> {temp}')
            file_out.write(f'{prev} -> {temp}\n')
        prev = temp
    prev = ip_28_keys[0]
    conf_count28 = 0
    print(ip_28_keys)
    for temp in ip_28_keys[1:]:
        if (int(temp) < int(prev)) and (int(temp) >= 30) and (int(temp) < 80):
            conf_count28 += 1
            print(f'{prev} -> {temp}')
            file_out.write(f'{prev} -> {temp}\n')
        prev = temp
    prev = ip_29_keys[0]
    conf_count29 = 0
    print(ip_29_keys)
    for temp in ip_29_keys[1:]:
        if (int(temp) < int(prev)) and (int(temp) >= 30) and (int(temp) < 80):
            conf_count29 += 1
            print(f'{prev} -> {temp}')
            file_out.write(f'{prev} -> {temp}\n')
        prev = temp
    prev = ip_39_keys[0]
    conf_count39 = 0
    print(ip_39_keys)
    for temp in ip_39_keys[1:]:
        if (int(temp) < int(prev)) and (int(temp) >= 30) and (int(temp) < 80):
            conf_count39 += 1
            print(f'{prev} -> {temp}')
            file_out.write(f'{prev} -> {temp}\n')
        prev = temp

    file_out.write(f'{ip_27_keys}\n')
    file_out.write(f'{ip_28_keys}\n')
    file_out.write(f'{ip_29_keys}\n')
    file_out.write(f'{ip_39_keys}\n')
    conf_count=conf_count39+conf_count29+conf_count27+conf_count28
    print(conf_count)
    file_out.write(f'conflicts counter: {conf_count}\n')
    print(repsIp)
file_out.close()



"""
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i]['events'][j]['description']=="Adding to barak memtable"
            """