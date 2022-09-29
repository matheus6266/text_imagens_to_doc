import pytesseract as pytesseract
import docx
import os

clear = lambda: os.system("cls")
clear()

# Caminho para o aplicativo do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Tesseract\\tesseract'

dir_name_model = "C:\\TCC_data_science\\projeto_tio_otavio\\"
total_imagens = int(input("Inform the number of images to be read: "))
format_text = '.docx'

while True:
    
	dir_name_images = input("Enter the path of the images directory (exe:'C:\\dir\\images'): ")
	dir_name_docs = input("Enter the path of the docs directory (exe:'C:\\dir\\docs'): ")

	if os.path.isdir(dir_name_images) and os.path.isdir(dir_name_docs):
		print("The paths are valid")
		format_images = input("Enter the image format (exe: .jpeg, .png): ")

		if format_images == ".jpeg" or format_images =='.jpg' or format_images == ".png":
			print("The file formar are valid.")
			print("\n")
			break

		else:
			print("Please, inform the correct file format.")
			continue
	else:
		print("Enter the paths correctly.")	
		continue


for i in range(total_imagens):
	
	base_filename_image = 'imagem_'+str(i + 1)
	base_filename_docs = 'text_'+str(i + 1)
	print("Reading de", i + 1 ,"° image")
	leitura_texto = pytesseract.image_to_string(os.path.join(dir_name_images, base_filename_image + format_images), lang = 'por', config = '--psm 12')
	print("Writting the", i + 1 ,"° image")

	document_model = "MODELO 14X21"

	doc = docx.Document(os.path.join(dir_name_model, document_model + format_text))
	## doc = docx.Document() Creating a new file 
	doc.add_paragraph("%s" % leitura_texto)
	doc.save(os.path.join(dir_name_docs, base_filename_docs + format_text))
	print("\n")
	
print("End of the program.")
print("\n")
