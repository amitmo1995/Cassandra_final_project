import random
from strings_generator import strings_generator
class create_table_query(object):
  def __init__(self,key_space_name,num_of_cols,name):
      self.name=name
      self.columns=[]
      self.key_space_name=key_space_name
      self.primary_keys=[]
      self.query=self.create_table_query(self.name,num_of_cols)




  def create_table_query(self,table_name,num_of_cols):
      query = "CREATE TABLE "
      query += self.key_space_name
      query += "."
      query += table_name
      query += " ("
      for i in range(num_of_cols):
          name=strings_generator(4)
          while name in self.columns :
              name=strings_generator(4)
          self.columns.append(name.name)
          query += self.columns[len(self.columns)-1]
          rand = random.randint(0, 1)
          query += " text, "
      query += "PRIMARY KEY ("
      rand = random.randint(1, len(self.columns))
      for i in range(rand):
          if i > 0:
              query += ", "
          key=self.columns[random.randint(0,num_of_cols-1)]
          while key in self.primary_keys :
              key = self.columns[random.randint(0, num_of_cols - 1)]
          self.primary_keys.append(key)
          query += self.primary_keys[len(self.primary_keys)-1]
      query += "));"
      return query