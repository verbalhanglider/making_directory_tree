from os import getcwd
from os.path import join
from io import BytesIO
from PyPDF2.pdf import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from .utils import make_a_jpeg

def pick_a_color(num):
    """function to randomly select a color to make the image on a given pdf page

    Args:
        num (int): the current page number being created

    Returns:
        str. one of three words: red, blue or green
    """
    color_choices = ['red', 'blue', 'green']
    if num <= len(color_choices) - 1:
        pos = num
    else:
        pos = 0
    return color_choices[pos]

def generate_a_pdf(filename, num_pages, dir=None):
    """function to generate a random PDF file of N pages with single image per page

    taken from https://stackoverflow.com/questions/2925484/place-image-over-pdf

    Args:
        filename (str): path to save the pdf file
        num_pages (int): number of pages to make the pdf file

    KWArgs:
        dir (str): the path to the directory to save the pdf file

    Returns:
        str. path to the new pdf file
    """
    pdf = PdfFileWriter()
    for num in range(1, num_pages+1):
        imgTemp = BytesIO()
        jpeg_path = make_a_jpeg('{}.jpeg'.format(str(num)), pick_a_color(num)) 
        imgDoc = canvas.Canvas(imgTemp, pagesize=A4)
        imgDoc.drawImage(jpeg_path, 25, 45)
        imgDoc.save()
        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
    if dir:
        path = join(dir, filename)
    else:
        path = join(getcwd(), filename)
    pdf.write(open(path, 'wb'))
    return path
