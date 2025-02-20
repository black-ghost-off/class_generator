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
        file.write("package main\n\n")
        
        for define in defines:
            file.write(f"const {define['name']} = {define['value']}\n\n")
        
        for enum in enums:
            file.write(f"type {enum['name']} int\nconst (\n")
            enum_value_p = 0
            for count, value in enumerate(enum['values']):
                enum_value = value.get('value', None)
                if(count == 0):
                    first_enum_element = f"{value['name']} {enum['name']}"
                else:
                    first_enum_element = f"{value['name']}"
                enum_value_p += 1                
                if enum_value is not None:
                    file.write(f"    {first_enum_element} = {value['value']}\n")
                    enum_value_p = enum_value
                else:
                    file.write(f"    {first_enum_element} = {enum_value_p}\n")

            file.write(")\n\n")
        
        for class_ in classes:
            file.write(f"type {class_['name']} struct {{\n")
            for field in class_.get('fields', []):
                for field_name, field_info in field.items():
                    field_type = utils.yaml_name_to_lang(field_info['type'], "go")
                    field_size = field_info.get('size', None)
                    if field_size is not None:
                        file.write(f"    {field_name} [{field_size}]{field_type};\n")
                    else:
                        file.write(f"    {field_name} {field_type};\n")

            file.write("}\n\n")

            for function in class_.get('functions', []):
                param_list = []
                for param in function['params']:
                    for param_name, param_info in param.items():
                        param_type = utils.yaml_name_to_lang(param_info['type'], 'go')
                        param_list.append(f"{param_name} {param_type}")
                        return_type = utils.yaml_name_to_lang(function['return_type'], 'go')
                        if return_type is None:
                            return_type = "" 
                file.write(f"func {class_['name']}_{function['name']}(self {class_['name']}, {', '.join(param_list)}) {return_type}{{\n\n}}\n")
            file.write(f"\n\n")

        for function in functions:
            param_list = []
            for param in function['params']:
                for param_name, param_info in param.items():
                    param_type = utils.yaml_name_to_lang(param_info['type'], 'go')
                    param_list.append(f"{param_name} {param_type}")
                    return_type = utils.yaml_name_to_lang(function['return_type'], 'go')
                    if return_type is None:
                        return_type = "" 
            file.write(f"func {function['name']}(self {class_['name']}, {', '.join(param_list)}) {return_type}{{\n\n}}\n")
        file.write(f"\n\n")