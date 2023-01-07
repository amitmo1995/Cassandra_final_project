import random


class select_query(object):
    def __init__(self,table):
        self.table_name=table.name
        self.keyspace_name=table.key_space_name
        self.table_columns=table.columns
        self.selected_cols=[]
        self.query=self.generate_select_query()
    # select query example
    # SELECT id, lastname, teams
    # FROM cycling.cyclist_career_teams
    # WHERE id=5b6962dd-3f90-4c93-8f61-eabfa4a803e2;
    def generate_select_query(self):
        query="SELECT "
        rand=random.randint(0,len(self.table_columns)-1)
        if rand==0:
            query+="*"
            self.selected_cols=self.table_columns
        else :
            for i in range(rand) :
                if i>0 :
                    query+=", "
                col=self.table_columns[random.randint(0,len(self.table_columns)-1)]
                while col in self.selected_cols :
                    col = self.table_columns[random.randint(0, len(self.table_columns) - 1)]
                self.selected_cols.append(col)
                query += self.selected_cols[len(self.selected_cols) - 1]
        query+=" FROM "
        query+=self.keyspace_name
        query+="."
        query+=self.table_name
        query+=";"
        return query