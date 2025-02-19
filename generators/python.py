import yaml
import sys
import os
import utils

def gen(yaml_file, header_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    classes = data.get('classes', [])
    functions = data.get('functions', [])
    defines = data.get('defines', [])
    enums = data.get('enums', [])

    with open(header_file, 'w') as file:

        file.write(f"import numpy as np\n")

        # Handle defines as class-level constants
        for define in defines:
            file.write(f"\n{define['name']} = {define['value']}\n")

        # Handle Enums
        enum_value_p = 0
        for enum in enums:
            file.write(f"\nclass {enum['name']}:\n")
            for value in enum['values']:
                enum_value = value.get('value', None)
                enum_value_p += 1
                if enum_value is not None:
                    file.write(f"    {value['name']} = {enum_value}\n")
                    enum_value_p = enum_value
                else:
                    file.write(f"    {value['name']} = {enum_value_p}\n")

        for function in functions:
            param_list = []
            for param in function['params']:
                for param_name, param_info in param.items():
                    param_list.append(f"{param_name}")

            file.write(f"\ndef {function['name']}({', '.join(param_list)}):\n")
            file.write(f"   pass\n")

        file.write(f"\n")

        # Handle class
        for class_info in classes:
            struct_name = class_info['name']
            file.write(f"\nclass {struct_name}:\n")
            file.write(f"   structure = np.dtype([\n")

            for field in class_info.get('fields', []):
                for field_name, field_info in field.items():
                    field_type = utils.yaml_name_to_lang(field_info['type'], "python")
                    file.write(f"    (\"{field_name}\", {field_type}),\n")
            file.write(f"   ])\n\n")

            for field in class_info.get('fields', []):
                for field_name, field_info in field.items():
                    file.write(f"   {field_name} = None \n")

            file.write(f"\n")
            # Add methods for serialization and deserialization
            file.write(f"   def serialize(self):\n")
            for field in class_info.get('fields', []):
                for field_name, field_info in field.items():
                    file.write(f"       self.structure[\"{field_name}\"] = self.{field_name} \n")
            file.write(f"       return self.structure.tobytes()\n")

            file.write(f"\n")

            file.write(f"   def deserialize(self, data):\n")
            file.write(f"       deserialized_struct = np.frombuffer(data, dtype={struct_name}.struct)\n")
            for field in class_info.get('fields', []):
                for field_name, field_info in field.items():
                    file.write(f"       self.{field_name} = deserialized_struct[\"{field_name}\"] \n")
            
            # Handle function prototypes
            for function in class_info.get('functions', []):
                param_list = []
                for param in function['params']:
                    for param_name, param_info in param.items():
                        param_list.append(f"{param_name}")

                file.write(f"\n   def {function['name']}(self, {', '.join(param_list)}):\n")
                file.write(f"       pass\n")
            
            file.write(f"\n")