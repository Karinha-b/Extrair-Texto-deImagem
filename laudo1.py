#Bibliotecas
import pytesseract
import cv2

#ler essa imagem
imagem =cv2.imread("laudo1_pg1.jpg")
#local da biblioteca
caminho=r"C:\Program Files\Tesseract-OCR"
#extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)
#Chamar a imagem
#print(texto)
#criar arquivo txt
with open("Laudo_1.txt","w") as arq1:
    #passar texto escaneado para txt
    arq1.write(texto)
