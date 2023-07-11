from pypdf import PdfReader,PdfMerger,PdfWriter
from pathlib import Path
import copy
import pypdfium2 as pdfium
from PIL import Image 

#read file
pdf_reader=PdfReader('sample.pdf')
pdf_write=PdfWriter()
for i in pdf_reader.pages:
    print(i.extract_text())

#merge file
curr_path=Path.cwd()
pdf_merge=PdfMerger()
for i in curr_path.glob("*.pdf"):
    pdf_merge.append(i)
pdf_merge.write('merge.pdf')

#split file
pdf=PdfReader('merge.pdf')
l=len(pdf_reader.pages)
for i in pdf.pages[0:l]:
    print(i.extract_text())

# crop file
first_page=pdf_reader.pages[0]
copy_page=copy.deepcopy(first_page)
copy_page.mediabox.upper_left=[500,0]
copy_page.mediabox.upper_right=[0,800]
pdf_write.add_page(copy_page)
pdf_write.write('crop.pdf')

# rotate file
t=PdfWriter()
for i,page in enumerate(pdf_reader.pages):
    page.rotate(180)
    t.add_page(page)
t.write('rotate.pdf')

# Load a document
pdf = pdfium.PdfDocument("sample.pdf")
for i in range(len(pdf)):
    pil_image = pdf[i].render(scale=4).to_pil()
    pil_image.save(("output{}.jpg").format(i))

#image to pdf
image1=Image.open("output0.jpg")
image1.save("image_to_pdf.pdf")



