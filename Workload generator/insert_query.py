import random
from strings_generator import strings_generator

class insert_query(object):
    def __init__(self,table):
        self.table_name = table.name
        self.keyspace_name = table.key_space_name
        self.table_columns = table.columns
        self.cols_to_insert_to=[]
        self.inserted_values=[]
        self.query=self.generate_instert_query()
    # query example
    # INSERT INTO cycling.cyclist_categories (id,lastname,categories)
    #   VALUES(
    #     '6ab09bec-e68e-48d9-a5f8-97e6fb4c9b47',
    #     'KRUIJSWIJK',
    #     {'GC', 'Time-trial', 'Sprint'});
    def generate_instert_query(self):
        query="INSERT INTO "
        query+=self.keyspace_name
        query+="."
        query+=self.table_name
        query+=" ("
        rand=random.randint(1,len(self.table_columns))
        for i in range(rand) :
            if i>0 :
                query+= ", "
            col=self.table_columns[random.randint(0,len(self.table_columns)-1)]
            while col in self.cols_to_insert_to :
                col = self.table_columns[random.randint(0, len(self.table_columns) - 1)]
            self.cols_to_insert_to.append(col)
            query+=self.cols_to_insert_to[len(self.cols_to_insert_to)-1]
        query+=") VALUES("
        for i in range(len(self.cols_to_insert_to)) :
            val = strings_generator(3)
            if i>0 :
                query+=", "
            query+="'"
            query+=val.name
            query+="'"
            self.inserted_values.append(val.name)
        query+=");"
        return query


