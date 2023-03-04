import random
class key_space(object):
  def __init__(self,replication_factor,name):
    self.replication_factor = replication_factor
    self.name = name
    self.query=self.create_keyspace_query(self.name)
  def create_keyspace_query(self,name):
      query = "CREATE KEYSPACE IF NOT EXISTS "
      query += name
      query += " WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '"
      query += str(self.replication_factor)
      query += "' };"
      return query