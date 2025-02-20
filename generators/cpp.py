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
        file.write(f"#ifndef {utils.replace_letters_with_underscore(header_file.upper())}\n")
        file.write(f"#define {utils.replace_letters_with_underscore(header_file.upper())}\n\n")
        file.write(f"#include <stdio.h>\n\n")
        
        # Handle defines
        for define in defines:
            file.write(f"#define {define['name']} {define['value']}\n")
        file.write(f"\n")
        
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
                    param_type = utils.yaml_name_to_lang(param_info['type'], 'c')
                    param_list.append(f"{param_type} {param_name}")
            file.write(f"{utils.yaml_name_to_lang(function['return_type'], 'c')} {function['name']}({', '.join(param_list)});\n")

        file.write(f"\n\n")     

        for class_info in classes:
            struct_name = class_info['name']
            file.write(f"class {struct_name} {{\n")
            file.write(f"private:\n")
            file.write(f"    #pragma pack(push, 1)\n")
            file.write(f"    struct Struct {{\n")

            for field in class_info.get('fields', []):
                for field_name, field_info in field.items():
                    field_type = utils.yaml_name_to_lang(field_info['type'], "c")
                    array_size = field_info.get('size', None)
                    if array_size is not None:
                        file.write(f"       {field_type} {field_name}[{array_size}];\n")
                    else:
                        file.write(f"       {field_type} {field_name};\n")
                        
            file.write(f"    }};\n")
            file.write(f"    #pragma pack(pop)\n\n")

            file.write(f"public:\n")
            file.write(f"    {struct_name}();\n")
            file.write(f"    ~{struct_name}();\n")

            file.write(f"\n")

            file.write(f"    void serialize(char* buffer, int buffer_size);\n")
            file.write(f"    void deserialize(const char* buffer, int buffer_size);\n")

            file.write(f"\n")

            for field in class_info.get('fields', []):
                for field_name, field_info in field.items():
                    field_type = utils.yaml_name_to_lang(field_info['type'], "c")
                    file.write(f"    {field_type} get_{field_name}();\n")
                    file.write(f"    void set_{field_name}({field_type} value);\n")

            file.write(f"\n")

            for function in class_info.get('functions', []):
                param_list = []
                for param in function['params']:
                    for param_name, param_info in param.items():
                        param_type = utils.yaml_name_to_lang(param_info['type'], 'c')
                        param_list.append(f"{param_type} {param_name}")
                file.write(f"    {utils.yaml_name_to_lang(function['return_type'], 'c')} {function['name']}({', '.join(param_list)});\n")
            
            file.write(f"}};\n\n\n")

        file.write(f"#endif // {utils.replace_letters_with_underscore(header_file.upper())}")
