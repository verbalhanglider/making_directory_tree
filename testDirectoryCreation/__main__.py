
from argparse import ArgumentParser
from json import load
from sys import stdout

from .utils import make_named_directory, make_a_tiff, make_a_jpeg,\
    make_a_text_document, make_an_xml_document, make_a_simple_pdf, traverse_data

def main():
    arguments = ArgumentParser(description="A simple CLI tool to generate a directory tree from a blob of JSON. " +\
                                           "Intended to make it easy to generate test directories for sysadmin applications.")
    arguments.add_argument("contract", action='store', type=str, help="The JSON contract for the directory tree to create")
    arguments.add_argument("color", type=str, action='store', help="Enter the color that you want images to include.")
    parsed_args = arguments.parse_args()
    try:
        stdout.write("starting to create new directory tree\n")
        data = load(open(parsed_args.contract, 'rb'))
        data = traverse_data(data)
        starter_directory = make_named_directory('root')
        dir_path = starter_directory
        for path, mimetype, payload in data:
            print(path)
            mime2filecreation.get(mimetype)(path, dir=dir_path, payload=payload)
        stdout.write("finished creating new directory tree at 'root'\n")
        return 0
    except KeyboardInterrupt:
        return 131

# mimetype -> file creation function lookup
mime2filecreation = {
    "image/tiff": make_a_tiff,
    "image/jpeg": make_a_jpeg,
    "text/plain": make_a_text_document,
    "application/xml": make_an_xml_document,
    "application/pdf": make_a_simple_pdf,
    None: make_named_directory
}