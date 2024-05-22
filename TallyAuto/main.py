# code 1
import pytesseract
from PIL import Image

# load the image
img = Image.open("path/to/image.png")

# perform OCR using pytesseract
text = pytesseract.image_to_string(img)

# print the extracted text
print(text)

#  code 2
import pytesseract
from PIL import Image
import openpyxl

# open the image file
image = Image.open('image.jpg')

# extract text from the image
text = pytesseract.image_to_string(image)

# create a new Excel workbook
workbook = openpyxl.Workbook()

# select the active worksheet
worksheet = workbook.active

# split the text into lines
lines = text.split('\n')

# write each line to a row in the worksheet
for i, line in enumerate(lines):
    worksheet.cell(row=i+1, column=1, value=line)

# save the workbook to a file
workbook.save('output.xlsx')
