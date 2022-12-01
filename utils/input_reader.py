from collections import defaultdict

def base_type_conversion(value, base_type):
    try:
        return base_type(value)
    except ValueError:
        return value

# ingest and format data as necessary for functions
def ingest(filename, file_format, base_type=str, null_value=int):
    """
    file_format types:
    0: raw
    1: line separated
    2: tuple per line
    3: comma seperated per line


    :param filename:
    :param file_format:
    :return:
    """
    if file_format == "raw":
        data = open(filename).read()
    elif file_format == "line":
        data = [base_type_conversion(line.strip().strip(), base_type) for line in open(filename).readlines()]
    elif file_format == "tuple":
        [tuple([col for col in line.strip().split()]) for line in open(filename).readlines()]
    elif file_format == "list":
        data = [[base_type_conversion(val, base_type) for val in line.strip().split(",")] for line in open(filename).readlines()]
    elif file_format == "grid":
        data = {}
        for j, line in enumerate(open(filename).readlines()):
            for i, value in enumerate(line.strip()):
                data[(i, j)] = base_type_conversion(value, base_type)

    return data
