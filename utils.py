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