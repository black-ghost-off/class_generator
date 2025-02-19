import yaml
import sys
import os
import utils
import generators.c
import generators.cpp
import generators.python

def yaml_to_header(yaml_file, header_file, language):
        if language.lower() == "c":
            generators.c.gen(yaml_file, header_file)
        elif language.lower() == "cpp":
            generators.cpp.gen(yaml_file, header_file)
        elif language.lower() == "python":
            generators.python.gen(yaml_file, header_file)

def generate_files(yaml_file):
    base_name = os.path.splitext(yaml_file)[0]
    
    yaml_to_header(yaml_file, f"{sys.argv[2]}", sys.argv[3])
    print(f"Generated {base_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input.yaml h/hpp/py")
    else:
        generate_files(sys.argv[1])
