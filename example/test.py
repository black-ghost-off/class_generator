import numpy as np

MAX_BUFFER_SIZE = 1024

class Status:
    OK = 0
    ERROR = 1
    INPROGRESS = 2
    TEST = 10

def example_function1(arg1, arg2):
   pass

def example_function2(arg1, arg2):
   pass


class test:
   structure = np.dtype([
    ("test", np.int16),
    ("vasya", np.int16),
   ])

   test = None 
   vasya = None 

   def serialize(self):
       self.structure["test"] = self.test 
       self.structure["vasya"] = self.vasya 
       return self.structure.tobytes()

   def deserialize(self, data):
       deserialized_struct = np.frombuffer(data, dtype=test.struct)
       self.test = deserialized_struct["test"] 
       self.vasya = deserialized_struct["vasya"] 

   def example_function3(self, arg1, arg2):
       pass

   def example_function4(self, arg1, arg2):
       pass


class test2:
   structure = np.dtype([
    ("test", np.int16),
    ("vasya", np.int16),
   ])

   test = None 
   vasya = None 

   def serialize(self):
       self.structure["test"] = self.test 
       self.structure["vasya"] = self.vasya 
       return self.structure.tobytes()

   def deserialize(self, data):
       deserialized_struct = np.frombuffer(data, dtype=test2.struct)
       self.test = deserialized_struct["test"] 
       self.vasya = deserialized_struct["vasya"] 

   def example_function(self, arg1, arg2):
       pass

