
from testDirectoryCreation.utils import traverse_data, make_named_directory, make_a_tiff, make_a_jpeg,\
    make_a_text_document, make_an_xml_document, make_a_simple_pdf
from testDirectoryCreation.pdf_making import generate_a_pdf
from os.path import exists
from json import load
from sys import argv, stdout

def build_directory_tree(data):
    """convenience function to create a basic LIMB style mvol directory

    taken from https://stackoverflow.com/questions/2925484/place-image-over-pdf
    """
    data = traverse_data(data)
    starter_directory = make_named_directory('root')
    dir_path = starter_directory
    for path, mimetype in data:
        if not mimetype:
            make_named_directory(path, dir=dir_path)
        if mimetype == 'image/tiff':
            # make tiff image
            make_a_tiff(path, 'blue', dir=dir_path)
        elif mimetype == 'image/jpeg':
            # make a jpeg image
            make_a_jpeg(path, 'blue', dir=dir_path)
        elif mimetype == 'text/plain':
            # make a text file
            make_a_text_document(path, dir=dir_path)
        elif mimetype == 'application/xml':
            # make an xml file
            make_an_xml_document(path, dir=dir_path)
        elif mimetype == 'application/pdf':
            # make a pdf file
            generate_a_pdf(path, 3, dir=dir_path)
    return dir_path    

if __name__ == "__main__":
    input_file = argv[1]
    print(input_file)
    if exists(input_file):
        data = load(open(input_file, 'rb'))
        build_directory_tree(data)
