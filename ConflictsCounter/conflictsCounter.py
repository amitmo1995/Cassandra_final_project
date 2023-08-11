import json

original=[]
file_name=input("enter file name: ")
with open(f'{file_name}', 'r') as file:
    original = file.readlines()
print("original")
for i,j in enumerate(original):
    if i>1:
        print(f'{i-2}) {j}',end='')
    else:
        print(j,end='')
print("\nnon original")

non_original=[]
non_original_lines=[]
full_duration=0
insert_duration=0
update_duration=0
delete_duration=0
in_len=0
up_len=0
del_len=0
res_file_name=input("enter file name: ")
with open(f'{res_file_name}', 'r') as file:
    traces = json.load(file)
    for trace in traces:
        # print(trace['started_at'])
        # print(trace['duration'])
        # print(trace['query'])
        full_duration+=(float(trace['duration'][5:]))
        # non_original.append(trace['query'])
        executed=trace['query']
        if executed[0:6]=='DELETE':
            delete_duration+=(float(trace['duration'][5:]))
            del_len+=1
        elif executed[0:6]=='UPDATE':
            up_len+=1
            update_duration += (float(trace['duration'][5:]))
        elif executed[0:6]=='INSERT':
            in_len+=1
            insert_duration += (float(trace['duration'][5:]))
        for i in range(len(original)):
            if executed[0:6]=='DELETE' or executed[0:6]=='UPDATE':
                temp1=original[i][:-1]
                temp2=executed
                if original[i][:-1] == executed:
                    # print(original[i + 2][:-1])
                    # print(non_original[i])
                    non_original.append(i)
                    non_original_lines.append(original[i])

print(non_original)
print(original[32:])

counter=0
lines_conflict=[]
for i in range(len(non_original)-1):
    if not (non_original[i]<non_original[i+1]):
        if i+32<=81:
            lines_conflict.append(i+32)
        counter+=1
#
# counter=0
# tracer=non_original[0]
# for i in range(len(non_original[1:])):
#     if not(non_original[i]==tracer+1):
#         counter+=1
#     tracer=non_original[i]

print("\nresults")
print(f'conflicts with delete included: {counter}')
print(f'conflicts without delete included: {len(lines_conflict)}')
print(f'full duration: {full_duration}')
print(f'duration per query AVG time: {full_duration/len(original)}')
print(f'update query AVG duration: {update_duration/up_len}')
print(f'delete query AVG duration: {delete_duration/del_len}')
print(f'insert query AVG duration: {insert_duration/in_len}')

file=open(f'{file_name}_results','w')

file.write(f'Original:\n{str(original[32:])}\n')
file.write(f'Non-original:\n{str(non_original)}\n')

for i in range(len(non_original)):
    file.write(f'line {32+i})\n{non_original_lines[i]}{original[i+32]}\n')
file.write(f'conflicts with delete included: {counter}\n')
file.write(f'conflicts without delete included: {len(lines_conflict)}\n')
file.write(f'full duration: {full_duration}\n')
file.write(f'duration per query AVG time: {full_duration/len(original)}\n')
file.write(f'update query AVG duration: {update_duration/up_len}\n')
file.write(f'delete query AVG duration: {delete_duration/del_len}\n')
file.write(f'insert query AVG duration: {insert_duration/in_len}\n')
file.write(f'{str(lines_conflict)}\n')
file.write(f'{str(non_original)}\n')
tmp=[]
for i in non_original:
    if i<=81:
        tmp.append(i)
file.write(f'{str(tmp)}')

file.close()

# counter=0
# for i in range(len(non_original)):
#     if not original[i+2][:-1]==non_original[i]:
#         print(original[i+2][:-1])
#         print(non_original[i])
#         counter+=1
#
#
# print(f'Number of conflicts : {counter}\nFully doration time : {full_duration}')