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

def create_table_query(table_name,num_of_cols,keyspace_name):
     columns=[]
     query = "CREATE TABLE IF NOT EXISTS "
     query += keyspace_name
     query += "."
     query += table_name
     query += " ("
     for i in range(num_of_cols):
         name=strings_generator(4)
         while name in columns :
             name=strings_generator(4)
         columns.append(name.name)
         query += columns[len(columns)-1]
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

def create_update_query(keyspace_name,table_name,columns,primary_key) :
    # UPDATE cycling.cyclist_id SET age = 28 WHERE lastname = 'WELTEN' and firstname = 'Bram' IF EXISTS;
    query=f'UPDATE {keyspace_name}.{table_name} SET {columns[1]} = '
    query+="'"
    query+=strings_generator(3).name
    query+="' WHERE "
    query+=f'{primary_key} = '
    query+="'"
    query+=primary_key_values[0]
    query+="' IF EXISTS;"
    return query

def create_delete_query(keyspace_name,table_name,primary_key) :
    # DELETE FROM cycling.cyclist_name WHERE id=e7ae5cf3-d358-4d99-b900-85902fda9bb0 IF EXISTS;
    query=f'DELETE FROM {keyspace_name}.{table_name} WHERE {primary_key}='
    query+="'"
    query+=primary_key_values[0]
    query+="' IF EXISTS;"
    return query



keyspace_name="amit"
table_name="barak"

keyspaceQuery=create_keyspace_query(keyspace_name,3)
tableQuery,primary_key,columns=create_table_query(table_name,3,keyspace_name)
# insert_query=create_insert_query(keyspace_name,table_name,columns)
# update_query=create_update_query(keyspace_name,table_name,columns,primary_key)
# delete_query=create_delete_query(keyspace_name,table_name,primary_key)
# primary_key_values=primary_key_values[1:]

# print(keyspaceQuery)
# print(tableQuery)
# print(insert_query)
# print(update_query)
# print(delete_query)
# print(columns)
# print(primary_key)
# print(primary_key_values)

insert=[]
update=[]
delete=[]
for i in range(100):
    if i<40 :
        insert.append(create_insert_query(keyspace_name,table_name,columns))
    elif i<90 :
        update.append(create_update_query(keyspace_name,table_name,columns,primary_key))
    else :
        delete.append(create_delete_query(keyspace_name,table_name,primary_key))
        primary_key_values = primary_key_values[1:]

print(keyspaceQuery)
print(tableQuery)
for i in insert :
    print(i)
for i in update :
    print(i)
for i in delete :
    print(i)

print(len(primary_key_values))

