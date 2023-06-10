import random
class strings_generator :
    def __init__(self,length) :
        self.length=length
        self.name=self.generate_name(self.length)
    def generate_name(self,length):
      name = ""
      for i in range(length) :
        rand = random.randint(97, 122)
        name += chr(rand)
      return name