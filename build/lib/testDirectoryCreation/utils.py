
from os import getcwd, mkdir
from os.path import join, exists
from io import BytesIO
from PIL import Image
from tempfile import TemporaryDirectory
from xml.etree import ElementTree

def make_a_solid_color_image(color):
  return Image.new(mode='RGB', size=(128,128), color=color)

def make_a_path(filename, dir=None):
    if dir:
        return join(dir, filename)
    else:
        return join(getcwd(), filename)    

def make_a_jpeg(filename, color, dir=None):
    path = make_a_path(filename, dir=dir)
    new_image = make_a_solid_color_image(color)
    new_image.save(path, tiffInfo=0)
    return path

def make_a_tiff(filename, color, dir=None):
    path = make_a_path(filename, dir=dir)
    new_image = make_a_solid_color_image(color)
    new_image.save(path)
    return path

def make_anonymous_directory(dir=None):
    if dir:
        return TemporaryDirectory(dir=dir)
    else:
        return TemporaryDirectory()

def make_named_directory(dirname, dir=None):
    path = make_a_path(dirname, dir=dir)
    if exists(path):
        pass
    else:
        mkdir(path)
    return path

def encode_text(a_string):
    if isinstance(a_string, str):
        return a_string.encode("utf-8")
    elif isinstance(a_string, bytes):
        return a_string

def make_an_xml_document(filename, dir=None, xml_doc=None):
    path = make_a_path(filename, dir=dir)
    if xml_doc:
        root = ElementTree.Element("root")
        ElementTree.SubElement(root, xml_doc)
        tree = ElementTree.ElementTree(root)
    else:
        root = ElementTree.Element("root")
        title = ElementTree.SubElement(root, "title")
        title.text = "This is a title"
        author = ElementTree.SubElement(root, "author")
        author.text = "Doe, Jane"
        tree = ElementTree.ElementTree(root)
    tree.write(path, xml_declaration=True, encoding="UTF-8")
    return path

def make_a_text_document(filename, dir=None, text_data=None):
    path = make_a_path(filename, dir=dir)
    if text_data:
        text_data = encode_text(text_data)
        with open(path, 'wb') as write_file:
            write_file.write(text_data)
            write_file.seek(0)
    else:
        with open(path, 'wb') as write_file:
            write_file.write(b"this is a simple text file")
            write_file.seek(0)
    return path

def traverse_data(a_dict):
    for i in a_dict:
        if i['type'] == 'directory':
            yield (i["name"], None)
            for j in traverse_data(i['contents']):
                yield j
        elif i['type'] == 'file':
            yield (i["name"], i["mimetype"])

def build_directory_tree(data):
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