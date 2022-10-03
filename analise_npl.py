import pytesseract as pytesseract
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

clear = lambda: os.system("cls")
clear()

pytesseract.pytesseract.tesseract_cmd = r'C:\\Tesseract\\tesseract' # Instanciando o alicativo tesseract

dir_name_model = "C:\\TCC_data_science\\projeto_tio_otavio\\"
total_imagens = int(input("Inform the number of images to be read: "))

while True:
    
	dir_name_images = input("Enter the path of the images directory (exe:'C:\\dir\\images'): ") 
	
	if os.path.isdir(dir_name_images): # Validação dos caminhos dos arquivos
		print("The paths are valid")
		format_images = input("Enter the image format (exe: .jpeg, .png): ")

		if format_images == ".jpeg" or format_images =='.jpg' or format_images == ".png": # Validação do formato dos arquivos
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
	#print("Reading de", i + 1 ,"° image")
	leitura_texto = pytesseract.image_to_string(os.path.join(dir_name_images, base_filename_image + format_images), lang = 'por', config = '--psm 12') # Lendo as imagens
	
	sentences = sent_tokenize(leitura_texto) # Separando o texto em senteças
	words = word_tokenize(leitura_texto) # Separando o texto em palavras

	stop_words = set(stopwords.words("portuguese")) # Filtrando as stop words
	filtered_words = [

		word for word in words if word.casefold() not in stop_words
	]

	stemmer = PorterStemmer() # criando uma instânica

	stemmed_words = [stemmer.stem(word) for word in filtered_words]  # reduzindo as palavras para o "root"

	words_tag = nltk.pos_tag(stop_words, lang='eng') # indicar o que é verbo, adjetvio, mas so tem para ingles e russp

	lemmatizer = WordNetLemmatizer()

	lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words] # reduzindo as palavras para o "root"

	frequencia_distribution = FreqDist(filtered_words) # verificando a quantidade de vezes que as palavras aparecem no texto

	#frequencia_distribution.plot(cumulative = True)

	#print(frequencia_distribution.most_common())

	sia = SentimentIntensityAnalyzer()
	teste = [x.encode('utf-8') for x in sentences]

	print(lemmatized_words)

	#print("Writting the", i + 1 ,"° image")
    