from cassandra.cluster import Cluster
import sqlite3
import sys
from decimal import *
import csv
import threading
import random
import time
import pathlib

# MAX_THREAD = 300

# ############################################################################################################################################
# ############################################################################################################################################

# #####################################################################################################################################################################################
# #####################################################################################################################################################################################

# def threadFunctionCass(liste,pos):

#     if liste[pos][6] == 'insert':
#         # adding if it allowed by the timestamp;
#         session.execute(
#         """INSERT INTO persons(id,first_name,last_name,country,profession) VALUES (%(id)s, %(first_name)s, %(last_name)s, %(country)s, %(profession)s)""",
#         {'id' : liste[pos][0], 'first_name' : liste[pos][2], 'last_name' : liste[pos][3], 'country' : liste[pos][1], 'profession' : liste[pos][4]}
#         )

#     elif liste[pos][6] == 'delete':

#         # delete if it allowed by the timestamp;
#         session.execute(
#             """DELETE FROM persons WHERE id = %(id)s""",
#             {'id': liste[pos][0]}
#             )

#     elif liste[pos][6] == 'update':
#         #updating if it allowed by the timestamp;

#         time.sleep(0.1)
#         cassandra_temp = session.execute("""SELECT * FROM persons WHERE id = %(id)s""", {'id': liste[pos][0]})
#         #check what there is to update
#         list_temp = liste[pos][:]
#         for i in range(len(liste[pos])):
#             if liste[pos][i] == 'null' and cassandra_temp[0][i]:
#                 list_temp[i] = str(cassandra_temp[0][i])

#         session.execute(
#         """INSERT INTO persons(id,first_name,last_name,country,profession) VALUES (%(id)s, %(first_name)s, %(last_name)s, %(country)s, %(profession)s)""",
#         {'id' : list_temp[0], 'first_name' : list_temp[2], 'last_name' : list_temp[3], 'country' : list_temp[1], 'profession' : list_temp[4]}
#         )

#     elif liste[pos][6] == 'read':
#         time.sleep(0.1)
#         cassandra_temp = session.execute("""SELECT * FROM persons WHERE id = %(id)s""", {'id': liste[pos][0]})


# print("######################################## Without Timestamp Benchmark 0.3.4 ################################################")

# #------------------------Preparation-----------------------------------
# num_threads = sys.argv[2]
# count = 1
# prev_threads = 0
# #------------------Main loop for batchs---------------------------------
# while num_tasks > 0:
#     print("\n##############################################################################################")
#     msg = "####################################### Batch number: "
#     msg += str(count)
#     msg +=" ######################################"
#     print(msg)
#     print("##############################################################################################")



#     #------------------Creation of the threads-----------------------------

#     for i in range(num_threads):
#         t_Cass = threading.Thread(target=threadFunctionCass, args=(rows,i+prev_threads))
#         threads_Cass.append(t_Cass)

#     #---------------------------------initiation---------------------------
#     for x in threads_Cass:
#         x.start()
    
#     for i in range(num_threads):
#         idx = i+prev_threads

#         letter = "------------------------------------------ SQLite "
#         letter += str(idx)
#         letter += " -----------------------------------------\n"
#         # letter += str(rows[idx][0])
#         # letter += "--------------------------\n"
#         print(letter)

#         if rows[idx][6] == 'insert':
#             cur.execute("insert OR IGNORE into persons values (?, ?, ?, ?, ?)", (rows[idx][0], rows[idx][1],rows[idx][2],rows[idx][3],rows[idx][4]))
#         elif rows[idx][6] == 'delete':
#             cur.execute("delete from persons where id =%s" %rows[idx][0])
#         elif rows[idx][6] == 'update':
#             time.sleep(0.1)
#             id = rows[idx][0]
#             sql_querie = cur.execute("SELECT * FROM persons WHERE id = '%s'" % id)
#             list_temp = rows[idx][:]
#             for i in range(len(rows[idx])):
#                 if rows[idx][i] == 'null' and sql_querie[0][i]:
#                     list_temp[i] = str(sql_querie[0][i])
#             cur.execute("update persons set first_name = ?, last_name = ?, country = ?,  profession = ? where id = ?",(list_temp[1],list_temp[2],list_temp[3],list_temp[4],list_temp[0]))
#             #  (rows[idx][0], rows[idx][1],rows[idx][2],rows[idx][3],rows[idx][4]))
#         #con.commit()
#         elif rows[idx][6] == "read":
#             id = rows[idx][0]
#             sql_querie = cur.execute("SELECT * FROM persons WHERE id = '%s'" % id)


#     #--------------------------Wait for all of them to finish----------------
#     for y in threads_Cass:
#         y.join()
    
#     #------Uptdate the actual number of tasks ramaining to do for the next batch----------
#     num_tasks = num_tasks - num_threads
#     prev_threads += num_threads
#     count += 1

# check = True
# continue_output = input("Do you want to see output comparaison (y/n) ")
# while check:
#     if continue_output == 'y' or continue_output == 'n':
#         check = False
#         continue
#     continue_output = input("Please enter only 'y' or 'n' caracters !\n")

# #------------------------Part of the output compare----------------------  
# if continue_output == 'y':
#     #------------------Get all the data from the table persons in Cassandra-----------------
#     cassandra_table = session.execute("""SELECT * FROM persons""")
#     human_cass_table = []
#     for row in cassandra_table:
#         ligne = []
#         count = 0
#         for j in row:
#             if count == 0:
#                 ligne.append(int(j))
#             else:
#                 ligne.append(str(j))
#             count += 1
#         human_cass_table.append(ligne)

#     #-----------------Get all the data from the table persons in SQL-----------------------
#     sql_table = cur.execute("SELECT * FROM persons")
#     human_sql_table = []
#     for row in sql_table:
#         ligne = []
#         count = 0
#         for j in row:
#             if count == 0:
#                 ligne.append(int(j))
#             else:
#                 ligne.append(str(j))
#             count +=1
#         human_sql_table.append(ligne)

#     human_cass_table.sort(key=lambda row: row[0])
#     human_sql_table.sort(key=lambda row: row[0])

#     delete_table = []
#     update_table = []
#     #-----------------------Get the update and delete Divergents-----------------------
#     if len(human_sql_table) >= len(human_cass_table):
#         big_table = human_sql_table
#         small_table = human_cass_table
#     else:
#         big_table = human_cass_table
#         small_table = human_sql_table
    
#     for row in big_table:
#         delete_bool = True
#         id_big = row[0]
#         for row1 in small_table:
#             id_small = row1[0]
#             if id_small == id_big:
#                 delete_bool = False
#                 if row != row1:
#                     update_table.append((row,row1))
#                     break
#         if delete_bool:
#             delete_table.append(row)
#     if(big_table == human_cass_table):
#         print("\nCassandra_timestamp ---------> SQL")
#     else:
#         print("\nSQL -----------> Cassandra_timestamp")
#     # pour_cass = Decimal(len(update_table)/(len(big_table)/3))*100
#     # pour_casd = float(len(delete_table)/(len(big_table)/3))*100
#     #print(pour_cass)
#     msp = "\n=========================== Number of divergents UPTDATE action: "
#     msp += str(len(update_table))
#     # msp += ", Pourcentage are: "
#     # msp += str(pour_cass)
#     msp += " ===========================\n"
#     print(msp)

#     msp = "\n============================= Number of divergents DELETE action: "
#     msp += str(len(delete_table))
#     # msp += ", Pourcentage are: "
#     # msp += str(pour_casd)
#     msp += " =============================\n"
#     print(msp)

#     check1 = True
#     continue_output1 = input("Would you like to see the Tables of divergents errors ? (y/n) ")
#     while check1:
#         if continue_output1 == 'y' or continue_output1 == 'n':
#             check1 = False
#             continue
#         continue_output1 = input("Please enter only 'y' or 'n' caracters !\n")

#     if continue_output1 == 'y':
#         print("\n****************************** Divergents UPDATE Table **********************************\n")
#         for i in update_table:
#             print(i)
#         print("\n****************************** Divergents DELETE Table **********************************\n")
#         for i in delete_table:
#             print(i)


# Save (commit) the changes
# con.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# con.close()

if __name__ == "__main__":

#-----------------------Init Cassandra Connection------------------
    # cluster = Cluster([sys.argv[1]])
    # session = cluster.connect('barak')
    # session.execute( "CREATE TABLE IF NOT EXISTS barak.Barak (userid text PRIMARY KEY, name text, age int, last_update_timestamp timestamp)")

#-----------------------create querys-------------------  
    print(pathlib.Path().resolve())



#-----------------------create threads------------------




    # num_threads = sys.argv[2]

    # for i in range(num_threads):
    #     t_Cass = threading.Thread(target=threadFunctionCass, args=(rows,i+prev_threads))
    #     threads_Cass.append(t_Cass)


