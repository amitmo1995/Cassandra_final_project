import random
from strings_generator import strings_generator

class update_query(object):
    def __init__(self,table):
        self.keyspace_updated=table.key_space_name
        self.updated_table=table.name
        self.table_columns=table.columns
        self.updated_columns=[]
        self.vals_inserted=[]
        self.query=self.generate_update_query()
    # UPDATE cycling.cyclist_id SET age = 28 WHERE lastname = 'WELTEN' and firstname = 'Bram' IF EXISTS;
    def generate_update_query(self):
        query="UPDATE "
        query+=self.keyspace_updated
        query+="."
        query+=self.updated_table
        query+=" SET "
        rand=random.randint(0,len(self.table_columns)-1)
        query+=self.table_columns[rand]
        query+=" = '"
        str=strings_generator(3)
        query+=str.name
        query+="' WHERE "
        rand = random.randint(0, len(self.table_columns) - 1)
        query+=self.table_columns[rand]
        query+="="
        str = strings_generator(3)
        query+="'"
        query+=str.name
        query+="';"
        return query




