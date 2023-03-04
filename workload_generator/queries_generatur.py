"""
generate 100 random select(read) and insert(write) queries for one table and one keyspace
amount of select is 40% and the amount of insert is 60%
the order of the queries is random
"""
import math
import random

from keyspace_query import  key_space
from create_table_query import create_table_query
from strings_generator import strings_generator
from select_query import select_query
from insert_query import insert_query
from update_query import update_query

write_percentage=60
read_percentage=40
num_of_queries=100

keyspace_name=strings_generator(5)
key_space_query=key_space(3,keyspace_name.name)
table_name=strings_generator(5)
table_query=create_table_query(key_space_query.name, 5, table_name.name)

num_to_read=math.ceil(num_of_queries*read_percentage/100)
num_to_write=math.ceil(num_of_queries*write_percentage/100)
read_queries=[]
write_queries=[]

for i in range(num_to_read) :
    read_queries.append(select_query(table_query).query)
for i in range(num_to_write) :
    write_queries.append(insert_query(table_query).query)

queries=[]
for i in range(num_to_write+num_to_read):
    if len(read_queries)==0 :
        queries.append(write_queries[0])
        write_queries = write_queries[1:]
        continue
    if len(write_queries)==0 :
        queries.append(read_queries[0])
        read_queries = read_queries[1:]
        continue
    if random.randint(1,100)>write_percentage:
        queries.append(read_queries[0])
        read_queries=read_queries[1:]
    else:
        queries.append(write_queries[0])
        write_queries=write_queries[1:]

print(queries)
print(read_queries)
print(write_queries)

file = open("100queries60%write40%read.txt", "w")
file.write(key_space_query.query+"\n"+table_query.query)
for i in queries :
    file.write(i)
    file.write("\n")
print()


