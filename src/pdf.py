from fpdf import FPDF
from PIL import Image
from src import path_image

def to_pdf(folder, image_with, image_higth, file_name):
    path       = path_image.take_path(folder)
    images     = path_image.take_image(path)
    all_files  = path_image.make_path(path, images)
   
    pdf = FPDF(orientation = 'L', unit = 'mm', format='A4')

    for one_image in all_files:
        pdf.add_page()
        pdf.image(one_image, x = 0, y = 0, w = image_with, h = image_higth)
    pdf.output(file_name) 