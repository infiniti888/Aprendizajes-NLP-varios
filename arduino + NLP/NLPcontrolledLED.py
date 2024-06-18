#Referencias
#https://pythonforthelab.com/blog/how-control-arduino-computer-using-python/
#https://www.luisllamas.es/controlar-arduino-con-python-y-la-libreria-pyserial/
#https://spacy.io/universe/project/eng_spacysentiment

#En función de si le escribes una frase positiva o negativa se encenderá o apagará el LED de un Arduino. 
#Se necesita el programa en Arduino sketch_pyserial ejecutandose.
import serial
import time
import eng_spacysentiment
dev = serial.Serial("COM4", baudrate=19200)
nlp = eng_spacysentiment.load()

#Bucle infinito para que funcione al mismo tiempo que el Arduino
while True:
    text=input("Write a sentence in English, if it is happy the LED will light up. Example: This is a cheerful sentence that tells you that I am happy and I feel satisfied\n")
    print(text)
    #Aplicamos el modelo NLP cargado (Spacy sentiment analysis)
    doc = nlp(text)
    #si el sentimiento es positivo manda 1 al Arduino, sino 0
    if doc.cats.get("positive") > 0.5:
        dev.write(b'1')
    else:
        dev.write(b'0')


#Para parar la conexión Serial
#dev.close()