"""a set of functions for creating files and directories on-disk
"""

__version__ = '1.0.0'

from os import getcwd, mkdir
from os.path import join, exists
from io import BytesIO
from PIL import Image
from tempfile import TemporaryDirectory
from xml.etree import ElementTree

def make_a_solid_color_image(color):
    """function to make a 128x128 pixel image that is a single color

    Args:
        color (str): the RGB value as string to determine what color the image should be. 
                     Example: blue, green, yellow, red
    
    Returns:
        PIL.Image.Image. the Image object that you want to create
    """
    return Image.new(mode='RGB', size=(128,128), color=color)

def make_a_path(filename, dir=None):
    """function to make a path on disk

    Without the keyword arg dir will base the new path on your current working directory.

    Args:
        filename (str): the path to create

    KWargs:
        dir (str): the directory to put the new path into

    Returns:
        str. the path that you want to create
    """
    if dir:
        return join(dir, filename)
    else:
        return join(getcwd(), filename)    

def make_a_simple_pdf(filename, color, dir=None):
    """function to make a pdf file with a single image

    Args:
        filename (str): the full path to write the jpeg image to
        color (str): the RGB value as string to determine what color the image should be. 
                     Example: blue, green, yellow, red
    
    KWargs:
        dir (str): the directory location to put the new text document into

    Return:
        str. the path to the new pdf document
    """

    path = make_a_path(filename, dir=dir)
    new_image = make_a_solid_color_image(color)
    new_image.save(path, 'PDF', resolution=100.0)
    return path

def make_a_jpeg(filename, color, dir=None):
    """function to make a pdf file with a single image

    Args:
        filename (str): the full path to write the jpeg image to
        color (str): the RGB value as string to determine what color the image should be. 
                     Example: blue, green, yellow, red
    
    KWargs:
        dir (str): the directory location to put the new text document into

    Return:
        str. the path to the new pdf document
    """

    path = make_a_path(filename, dir=dir)
    new_image = make_a_solid_color_image(color)
    new_image.save(path, 'JPEG', resolution=100.0)
    return path

def make_a_tiff(filename, color, dir=None):
    """function to make a tiff image

    Args:
        filename (str): the full path to write the tiff image to
        color (str): the RGB value as string to determine what color the image should be. 
                     Example: blue, green, yellow, red
   
    KWargs:
        dir (str): the directory location to put the new text document into

    Return:
        str. the path to the new xml document
    """

    path = make_a_path(filename, dir=dir)
    new_image = make_a_solid_color_image(color)
    new_image.save(path)
    return path

def make_anonymous_directory(dir=None):
    """a function to create an anonymous directory
    
    KWargs:
        dir (str): the path to put the new directory into

    Returns
        str. the path to the new anonymous directory
    """
    if dir:
        return TemporaryDirectory(dir=dir).name
    else:
        return TemporaryDirectory().name

def make_named_directory(dirname, dir=None):
    """function to make an xml document

    Args:
        dirname (str): the full path of the new directory
    
    KWargs:
        dir (str): the directory location to put the new directory inside of

    Return:
        str. the path to the new directory
    """

    path = make_a_path(dirname, dir=dir)
    if exists(path):
        pass
    else:
        mkdir(path)
    return path

def encode_text(a_string):
    """function to encode a string passed as ascii to utf-8

    Args:
        a_string (str): some ascii string that needs to be converted to bytes

    Returns:
        bytes. a new binary string
    """
    if isinstance(a_string, str):
        return a_string.encode("utf-8")
    elif isinstance(a_string, bytes):
        return a_string

def make_an_xml_document(filename, dir=None, xml_doc=None):
    """function to make an xml document

    Args:
        filename (str): the full path to write the text document to
    
    KWargs:
        dir (str): the directory location to put the new text document into
        xml_doc (xml.etree.ElementTree.Element): some xml element to add to the newly created xml document

    Return:
        str. the path to the new xml document
    """
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
    """function to make a text document

    Args:
        filename (str): the full path to write the text document to
    
    KWargs:
        dir (str): the directory location to put the new text document into
        text_data (bytes): some bytestring to write to the text document being created

    Return:
        str. the path to the new text document
    """
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
    """naive implementation of reading the contract JSON for instructions of what to write

    Example of contract to create a directory:

    [{
        "type": "directory",
        "name": "test",
        "contents": [
            {
                "type": "file",
                "name": "test.jpeg",
                "mimetype": "image/jpeg"
            }
        ]
    }]

    Example of contract to create a file:

    [{
        "type": "file",
        "name": "test.xml",
        "mimetype": "application/xml"
    }]
    """
    for i in a_dict:
        if i['type'] == 'directory':
            yield (i["name"], None)
            for j in traverse_data(i['contents']):
                yield j
        elif i['type'] == 'file':
            yield (i["name"], i["mimetype"])
