
from base64 import b64encode
from io import BytesIO
from os import getcwd, mkdir
from os.path import abspath, basename, dirname, exists, join, normpath

from shutil import copyfileobj
from uuid import uuid4
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

from .utils import make_a_path

class NewDirectory:
    def __init__(self, payload):
        if payload.get("root_dir"):
            self.root = normpath(payload["root_dir"] )
        else:
            self.root = getcwd()
        if payload.get("dirname"):
            self.name = normpath(payload["dirname"])
        else:
            self.name = uuid4().hex

    def get_string(self):
        return join(self.root, self.name)

    def write(self):
        new_path = join(self.root, self.name)
        if not exists(new_path):
            mkdir(new_path)
        else:
            msg = "there is already a directory {}".format(new_path)
            raise IOError(msg)

class NewTiff:
    def __init__(self, payload):
        if payload.get("compression"):
            self.compression = payload["compression"]
        if payload.get("numpages"):
            self.pages = payload["pages"]
        if payload.get("height"):
            self.height = payload["height"]
        if payload.get("width"):
            self.width = payload["width"]
        self.image = Image.new(mode=RGB)
    def build(self):
        pass

class NewJPEG:
    def __init__(self, payload):
        self.payload = payload

    def build(self):
        pass

    def write(self):
       pass

    #new_image = make_a_solid_color_image(color)
    #new_image.save(path, 'JPEG', resolution=100.0)
    #return path

class NewPDF:
    def __init__(self, payload):
        self.payload = payload

    def build(self):
        pass

class NewText:
    def __init__(self, payload):
        if payload.get("data"):
           self.text_body = payload["data"] 
        else:
            self.text_body = "this is a generic string: replace me with something interesting\nor at least informative"

    def get_string(self):
        return self.text_body.encode("utf-8")

    def write(self, path_to_write):
        bytes_obj = BytesIO(self.text_body.encode("utf-8"))
        bytes_obj.seek(0)
        with open(path_to_write, 'wb+', encoding="utf-8") as write_file:
            copyfileobj(bytes_obj, write_file, length=131072)

class NewXML:
    def __init__(self, payload):
        if payload.get("data"):
            self.xml_body = self._wrap_body_in_envlope(
                self._convert_payload_to_xml(payload["data"]))
        else:
            self.xml_body = self._convert_payload_to_xml(
                self._generic_xml_body())

    def _wrap_body_in_envlope(self, some_xml):
        root_element = Element("root")
        SubElement(root_element, some_xml)
        return root_element

    def _generic_xml_body(self):
        an_xml_element = Element("body")
        title_el = SubElement(an_xml_element, 'title')
        title_el.text = "Generic title"
        author_el = SubElement(an_xml_element, 'author')
        author_el.text = "Doe, Jane"
        return an_xml_element

    def _convert_payload_to_xml(self, json_blob):
        an_xml_element = Element("body")
        for key, value in json_blob.items():
            new_sub_element = SubElement(an_xml_element, key)
            new_sub_element.text = value
        return an_xml_element

    def get_string(self):
        return tostring(self.xml_body, encoding="utf-8", method="xml")

    def write(self, path_to_write):
        tree = ElementTree(self.xml_body)
        tree.write(path_to_write, xml_declaration=True, encoding="UTF-8")
