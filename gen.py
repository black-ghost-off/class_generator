import yaml
import sys
import os
import numpy as np
from enum import Enum
import re

dtypes_names = {
    "yaml": [
        "bool", "int8", "uint8", "int16", "uint16", "int32", "uint32",
        "int64", "uint64", "float", "float16", "float32", "float64", "float128", "void"
    ],
    "python": [
        "np.bool_", "np.int8", "np.uint8", "np.int16", "np.uint16", "np.int32", "np.uint32", 
        "np.int64", "np.uint64", "np.float32", "np.float16", "np.float32", "np.float64", "np.float128", "None"
    ],
    "c": [
        "bool", "int8_t", "uint8_t", "int16_t", "uint16_t", "int32_t", "uint32_t", 
        "int64_t", "uint64_t", "float", "N/A", "float", "double", "long double", "void"
    ]
}


def replace_letters_with_underscore(text):
    return re.sub(r'[^a-zA-Z]', '_', text)

def yaml_name_to_lang(yaml_name, lang):
    index = dtypes_names["yaml"].index(yaml_name)
    return dtypes_names[lang][index]

def yaml_to_header(yaml_file, header_file, language):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    classes = data.get('classes', [])
    functions = data.get('functions', [])
    defines = data.get('defines', [])
    enums = data.get('enums', [])
    
    with open(header_file, 'w') as file:
        if(language == "cpp" or language == "c"):
            file.write(f"#ifndef {replace_letters_with_underscore(header_file.upper())}\n")
            file.write(f"#define {replace_letters_with_underscore(header_file.upper())}\n\n")
            file.write("#include <stdio.h>\n\n")
            
            # Handle defines
            for define in defines:
                file.write(f"#define {define['name']} {define['value']}\n")
            file.write("\n")
            
            # Handle enums
            for enum in enums:
                file.write(f"typedef enum {enum['name']} {{\n")
                for value in enum['values']:
                    enum_value = value.get('value', None)
                    if enum_value is not None:
                        file.write(f"    {value['name']} = {enum_value},\n")
                    else: 
                        file.write(f"    {value['name']},\n")
                file.write(f"}} {enum['name']};\n\n")

            for function in functions:
                param_list = []
                for param in function['params']:
                    for param_name, param_info in param.items():
                        param_type = yaml_name_to_lang(param_info['type'], 'c')
                        param_list.append(f"{param_type} {param_name}")
                file.write(f"{yaml_name_to_lang(function['return_type'], 'c')} {function['name']}({', '.join(param_list)});\n")

            file.write("\n\n")     

            if language.lower() == "c":
                for class_info in classes:
                    struct_name = class_info['name']
                    file.write(f"typedef struct {struct_name} {{\n")
                    
                    # Handle fields and getters/setters for C
                    for field in class_info.get('fields', []):
                        for field_name, field_info in field.items():
                            field_type = yaml_name_to_lang(field_info['type'], "c")
                            file.write(f"    {field_type} {field_name};\n")
                    
                    file.write(f"}} {struct_name};\n\n")

                    for field in class_info.get('fields', []):
                        for field_name, field_info in field.items():
                            file.write(f"{field_type} {struct_name}_get_{field_name}(const {struct_name}* self);\n")  
                            file.write(f"void {struct_name}_set_{field_name}({struct_name}* self, {field_type} value);\n")

                    file.write("\n")

                    for function in class_info.get('functions', []):
                        param_list = []
                        for param in function['params']:
                            for param_name, param_info in param.items():
                                param_type = yaml_name_to_lang(param_info['type'], 'c')
                                param_list.append(f"{param_type} {param_name}")
                        file.write(f"{yaml_name_to_lang(function['return_type'], 'c')} {struct_name}_{function['name']}(struct {struct_name}, {', '.join(param_list)});\n")
                    file.write("\n\n")
                                
            # C++ class part
            if language.lower() == "cpp":
                for class_info in classes:
                    struct_name = class_info['name']
                    file.write(f"class {struct_name} {{\n")
                    file.write("private:\n")
                    
                    for field in class_info.get('fields', []):
                        for field_name, field_info in field.items():
                            field_type = yaml_name_to_lang(field_info['type'], "c")
                            file.write(f"    {field_type} {field_name};\n")

                    file.write("public:\n")
                    file.write(f"    {struct_name}();\n")
                    file.write(f"    ~{struct_name}();\n")

                    file.write("\n")

                    file.write(f"    void serialize(char* buffer) const;\n")
                    file.write(f"    void deserialize(const char* buffer);\n")

                    file.write("\n")

                    for field in class_info.get('fields', []):
                        for field_name, field_info in field.items():
                            field_type = yaml_name_to_lang(field_info['type'], "c")
                            file.write(f"    {field_type} get_{field_name}();\n")
                            file.write(f"    void set_{field_name}({field_type} value);\n")

                    file.write("\n")

                    for function in class_info.get('functions', []):
                        param_list = []
                        for param in function['params']:
                            for param_name, param_info in param.items():
                                param_type = yaml_name_to_lang(param_info['type'], 'c')
                                param_list.append(f"{param_type} {param_name}")
                        file.write(f"    {yaml_name_to_lang(function['return_type'], 'c')} {function['name']}({', '.join(param_list)});\n")
                    
                    file.write("};\n\n\n")

            file.write(f"#endif // {replace_letters_with_underscore(header_file.upper())}")

        elif language.lower() == "python":
            file.write("import numpy as np\n")

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
                        field_type = yaml_name_to_lang(field_info['type'], "python")
                        file.write(f"    (\"{field_name}\", {field_type}),\n")
                file.write(f"   ])\n\n")

                for field in class_info.get('fields', []):
                    for field_name, field_info in field.items():
                        file.write(f"   {field_name} = None \n")

                file.write("\n")
                # Add methods for serialization and deserialization
                file.write(f"   def serialize(self):\n")
                for field in class_info.get('fields', []):
                    for field_name, field_info in field.items():
                        file.write(f"       self.structure[\"{field_name}\"] = self.{field_name} \n")
                file.write(f"       return self.structure.tobytes()\n")

                file.write("\n")

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

def generate_files(yaml_file):
    base_name = os.path.splitext(yaml_file)[0]
    
    yaml_to_header(yaml_file, f"{sys.argv[2]}", sys.argv[3])
    print(f"Generated {base_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input.yaml h/hpp/py")
    else:
        generate_files(sys.argv[1])
