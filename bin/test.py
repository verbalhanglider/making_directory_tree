
from testDirectoryCreation.utils import traverse_data, make_named_directory, make_a_tiff, make_a_jpeg,\
    make_a_text_document, make_an_xml_document
from os.path import exists
from json import load
from sys import argv, stdout

def build_directory_tree(data):
    """convenience funciton to create a basic LIMB style mvol directory
    """
    data = traverse_data(data)
    starter_directory = make_named_directory('root')
    dir_path = starter_directory
    for path, mimetype in data:
        if not mimetype:
            print(make_named_directory(path, dir=dir_path))
        if mimetype == 'image/tiff':
            # make tiff image
            print(make_a_tiff(path, 'blue', dir=dir_path))
        elif mimetype == 'image/jpeg':
            # make a jpeg image
            print(make_a_jpeg(path, 'blue', dir=dir_path))
        elif mimetype == 'text/plain':
            # make a text file
            print(make_a_text_document(path, dir=dir_path))
        elif mimetype == 'application/xml':
            # make an xml file
            print(make_an_xml_document(path, dir=dir_path))
    return dir_path    

if __name__ == "__main__":
    input_file = argv[1]
    print(input_file)
    if exists(input_file):
        data = load(open(input_file, 'rb'))
        build_directory_tree(data)
