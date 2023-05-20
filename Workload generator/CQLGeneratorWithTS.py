import random
from strings_generator import strings_generator

primary_key_values=[]

def create_keyspace_query(name,replication_factor):
     query = "CREATE KEYSPACE IF NOT EXISTS "
     query += name
     query += " WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '"
     query += str(replication_factor)
     query += "' };"
     return query

def create_table_query(table_name,keyspace_name):
     columns=[]
     query = "CREATE TABLE IF NOT EXISTS "
     query += keyspace_name
     query += "."
     query += table_name
     query += " ("

     columns.append('A')
     query += columns[len(columns)-1]
     query += " text, "
     columns.append('B')
     query += columns[len(columns) - 1]
     query += " text, "
     columns.append('C')
     query += columns[len(columns) - 1]
     query += " text, "
     columns.append('toTS')
     query += columns[len(columns) - 1]
     query += " text, "
     columns.append('currTS')
     query += columns[len(columns) - 1]
     query += " text, "

     query += "PRIMARY KEY ("
     key=columns[0]
     query += key
     query += "));"
     return query,key,columns

def create_insert_query(keyspace_name,table_name,columns) :
    # INSERT INTO mfrmv.iazqu (rrmq) VALUES('cmx');
    query="INSERT INTO "
    query+=f'{keyspace_name}.{table_name} ({columns[0]}'
    for i in range(len(columns)):
        if i==0:
            continue
        query+=", "
        query+=columns[i]
    query+=") VALUES('"
    keyVal=strings_generator(3).name
    query+=keyVal
    primary_key_values.append(keyVal)
    query+="'"
    for i in range(len(columns)):
        if i==0:
            continue
        query+=", '"
        query+=strings_generator(3).name
        query+="'"
    query+=");"
    return query

def create_update_query(keyspace_name,table_name,columns,primary_key,num_of_insert) :
    # UPDATE cycling.cyclist_id SET age = 28 WHERE lastname = 'WELTEN' and firstname = 'Bram' IF EXISTS;
    query=f'UPDATE {keyspace_name}.{table_name} SET {columns[1]} = '
    query+="'"
    new_key=strings_generator(3).name
    query+=new_key
    query+="' WHERE "
    query+=f'{primary_key} = '
    query+="'"
    # added
    temp_percentage=int(num_of_insert*20/100)
    if temp_percentage==0:
        temp_percentage=1
    random_number = random.randint(1, temp_percentage)
    # if not work, delete random number and put zero instead
    query+=primary_key_values[random_number]
    primary_key_values[random_number]=new_key
    query+="';"
    return query

def create_delete_query(keyspace_name,table_name,primary_key) :
    # DELETE FROM cycling.cyclist_name WHERE id=e7ae5cf3-d358-4d99-b900-85902fda9bb0 IF EXISTS;
    query=f'DELETE FROM {keyspace_name}.{table_name} WHERE {primary_key}='
    query+="'"
    query+=primary_key_values[0]
    query+="';"
    return query



keyspace_name="amit"
table_name="barak"

insert=[]
update=[]
delete=[]

while 1:
    num_of_queries=int(input("num of queries: "))
    num_of_insert=int((int(input("percentage of insert queries: "))/100)*num_of_queries)
    num_of_update=int((int(input("percentage of update queries: "))/100)*num_of_queries)
    num_of_delete=int((int(input("percentage of delete queries: "))/100)*num_of_queries)
    repfactor=int(input("replication factor: "))
    threads = int(input("num of threads: "))
    if (num_of_delete+num_of_insert+num_of_update)==num_of_queries and repfactor>0:
        break
    else:
        print("wrong input, try again...")


keyspaceQuery=create_keyspace_query(keyspace_name,repfactor)
tableQuery,primary_key,columns=create_table_query(table_name,keyspace_name)



dup_in=[]
dup_up=[]
dup_del=[]




for i in range(num_of_queries):
    if i<num_of_insert :
        temp=create_insert_query(keyspace_name,table_name,columns)
        dup_in.append(temp)
        insert.append(temp[:-1]+f' USING TIMESTAMP {i+1};')
    elif i<num_of_insert+num_of_update :
        temp=create_update_query(keyspace_name,table_name,columns,primary_key,num_of_insert)
        dup_up.append(temp)
        update.append(temp[:17]+f' USING TIMESTAMP {i+1}'+temp[17:])
    else :
        temp=create_delete_query(keyspace_name,table_name,primary_key)
        dup_del.append(temp)
        delete.append(temp[:22]+f' USING TIMESTAMP {i+1}'+temp[22:])
        primary_key_values = primary_key_values[1:]



file1 = open(f'workloads/{num_of_queries}queries_rep{repfactor}_insert{num_of_insert}_update{num_of_update}_delete{num_of_delete}_numOfThreads{threads}_withTS.txt', "w")
file2 = open(f'workloads/{num_of_queries}queries_rep{repfactor}_insert{num_of_insert}_update{num_of_update}_delete{num_of_delete}_numOfThreads{threads}_withoutTS.txt', "w")
print("[.",end='')
file1.write(keyspaceQuery+'\n')
file2.write(keyspaceQuery+'\n')
print(".",end='')
file1.write(tableQuery+'\n')
file2.write(tableQuery+'\n')
print("..",end='')
for i in insert :
    file1.write(i+'\n')
for i in dup_in:
    file2.write(i + '\n')
print("..", end='')
for i in update :
    file1.write(i+'\n')
for i in dup_up:
    file2.write(i + '\n')
print("..", end='')
for i in delete :
    file1.write(i+'\n')
for i in dup_del:
    file2.write(i + '\n')
print(f'..]100% done!\nfiles pathes is: \n'
      f'workloads/{num_of_queries}queries_rep{repfactor}_insert{num_of_insert}_update{num_of_update}_delete{num_of_delete}_numOfThreads{threads}_withTS.txt\n'
      f'workloads/{num_of_queries}queries_rep{repfactor}_insert{num_of_insert}_update{num_of_update}_delete{num_of_delete}_numOfThreads{threads}_withoutTS.txt')



