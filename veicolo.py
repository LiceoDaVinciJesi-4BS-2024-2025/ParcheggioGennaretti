# Veicolo

listaAlim = ("benzina", "diesel", "elettrico", "metano")
listaMarche = ("fiat", "toyota", "audi", "piaggio")
listaColori = ("rosso", "grigio", "nero", "bianco", "blu")
alfabeto = "qwertyuiopasdfghjklzxcvbnm"
numeri = "12334567890"

def controlloTarga(targa):
    if len(targa) != 6:
        return False
    
    for car in targa:
        if car in alfabeto and conta < 3 and conta > 4:
            valido = True
        elif car in numeri and conta > 1 and conta < 5:
            controllo = True
            else:
                controllo = False
    return controllo

class Veicolo:
    def __init__(marca = "", modello = "", colore = "", cilindrata = 0, alimentazione = "benzina", targa): 
        if marca in listaMarche:
            self.__marca = marca
            else:
                raise ValueError("Marca veicolo non valida")

        if modello in listaModello:
            self.__modello = modello
            else:
                raise ValueError("Modello veicolo non valida")

        if colore in listaColori:
            self.__colore = colore
            else:
                raise ValueError("Colore veicolo non valida")

        if cilindrata % 100 and cilindrata >= 100:
            self.__cilindrata = cilindrata
            else:
                raise ValueError("Cilindrata veicolo non valida")  
    
        if alimentazione in listaAlim:
            self.__alimentazione = alimentazione
            else:
                raise ValueError("Alimentazione non valida")

        if  controlloTarga(targa) == True:
            self.__targa = targa 
            else:
                raise ValueError("Targa non valida")
    
    def __str__(self):
        return __class__.__name__(self.__dict__)

        