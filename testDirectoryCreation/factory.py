
from .builders import NewDirectory, NewTiff, NewJPEG, NewPDF, NewXML

class NewThingFactory:
    def __init__(self, mimetype, payload):
        self.payload = payload
        self.flag = mimetype

    def request(self):
        flag = self.flag
        if flag == 'None':
            NewDirectory(self.payload)
        elif flag == 'image/tiff':
            NewTiff(self.payload)
        elif flag == 'image/jpeg':
            NewJPEG(self.payload)
        elif flag == 'application/xml':
            NewXML(self.payload)
        elif flag == 'application/pdf':
            NewPDF(self.payload)
        else:
            msg = "cannot create directory item of type {}".format(flag)
            raise TypeError(msg)
