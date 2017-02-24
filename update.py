import os
import json
import requests
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from wand.image import Image


books = []  

s_dir = 'assets/books/'
s_cover_dir = 'assets/covers/'
s_img_ext = '.gif'

def convert_image(pdf_file, image_name):
	"""
	"""
   	with Image(filename=pdf_file+"[0]") as img:
		img.save(filename=image_name)


for f in os.listdir(s_dir):
	if f.endswith('.pdf'):
		pdf_file = s_dir + f
		parser = PDFParser(open(pdf_file,  'rb'))
		doc_info = PDFDocument(parser).info[0]
		# create cover
		title = doc_info.get('Title', f).replace(' ', '_')
		cover = s_cover_dir + title + s_img_ext
		author = doc_info.get('Author', 'NA')

		convert_image(pdf_file, cover)
		print(pdf_file)
		#print("https://www.google.co.in/search?q={} by {}".format(title,author))
		books.append({
			'author': author,
			'title': title,
			'level': 'Intermediate',
			'cover': cover,
			'authorUrl': "https://www.google.co.in/search?q="+author ,
			'info': 'NA',
			'url': pdf_file,

		})

with open('issues.json', 'w') as outfile:
    json.dump({'books':books}, outfile)
