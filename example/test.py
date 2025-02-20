import numpy as np

MAX_BUFFER_SIZE = 1024

class Status:
    OK = 0
    ERROR = 1
    INPROGRESS = 2
    TEST = 10
    TEST2 = 11

def example_function1(arg1, arg2):
   pass

def example_function2(arg1, arg2):
   pass


class test:
   structure = np.dtype([
    ("id", np.int16),
    ("value", np.int16),
    ("array", np.int16, (10,)),
   ])

   id = None 
   value = None 
   array = None 

   def serialize(self):
       self.structure["id"] = self.id 
       self.structure["value"] = self.value 
       self.structure["array"] = self.array 
       return self.structure.tobytes()

   def deserialize(self, data):
       deserialized_struct = np.frombuffer(data, dtype=test.struct)
       self.id = deserialized_struct["id"] 
       self.value = deserialized_struct["value"] 
       self.array = deserialized_struct["array"] 

   def example_function3(self, arg1, arg2):
       pass

   def example_function4(self, arg1, arg2):
       pass


class system:
   structure = np.dtype([
    ("id", np.int16),
    ("voltage0", np.int16),
    ("voltage1", np.int16),
    ("voltage2", np.int16),
   ])

   id = None 
   voltage0 = None 
   voltage1 = None 
   voltage2 = None 

   def serialize(self):
       self.structure["id"] = self.id 
       self.structure["voltage0"] = self.voltage0 
       self.structure["voltage1"] = self.voltage1 
       self.structure["voltage2"] = self.voltage2 
       return self.structure.tobytes()

   def deserialize(self, data):
       deserialized_struct = np.frombuffer(data, dtype=system.struct)
       self.id = deserialized_struct["id"] 
       self.voltage0 = deserialized_struct["voltage0"] 
       self.voltage1 = deserialized_struct["voltage1"] 
       self.voltage2 = deserialized_struct["voltage2"] 

   def example_function(self, arg1, arg2):
       pass

