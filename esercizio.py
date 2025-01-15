# Esercizio
# Martino Gennaretti

from liv1 import Auto, Moto, Autobus, Camion
from liv2 import PostoMezzo
import datetime
from veicolo import Veicolo

mezziOK = ("auto", "moto", "camion", "autobus")

    
parcheggio = []
contaPosti = {"auto": 1000, "moto": 200, "camion": 50, "autobus": 200}

# class Parcheggio(PostoMezzo):
#     def __init__(self):
#         super().__init__(tipoMezzo, libero)
#         self.__guadagnoGiornaliero = 0
# 
#     @property
#     def contaPosti(self):
#         return self.__contaPosti
# 
#     @property
#     def guadagnoGiornaliero(self):
#         return self.__guadagnoGiornaliero
# 
#     def __str__(self):
#         a = "Parcheggio: " + str(self.__dict__)
#         return a
#     
#     def postiLiberi(self, tipoMezzo):
#         if str.lower(tipoMezzo) not in mezziOK:
#             raise ValueError("tipoMezzo non accettabile")
#         return self.__contaPosti[tipoMezzo]


mezzo = Auto("AB123CD", 10, 5)

while True:
    scelta = input("Cosa vuoi fare? 'Prenota/Libera/Visualizza Conteggio/Chiudi' ")
    if scelta == "Prenota":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        posto = PostoMezzo.prenota(targa, tipoMezzo)
        parcheggio.append(posto)
        contaPosti[tipoMezzo] -= 1

        



