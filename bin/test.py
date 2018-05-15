
from testDirectoryCreation.utils import traverse_data, build_directory_tree
from os.path import exists
from json import load
from sys import argv, stdout

if __name__ == "__main__":
    input_file = argv[1]
    print(input_file)
    if exists(input_file):
        data = load(open(input_file, 'rb'))
        result = traverse_data(data)
        out = build_directory_tree(result)
        stdout.write("{}\n".format(out))