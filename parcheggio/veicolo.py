# Veicolo

alimOk = ("", "benzina", "diesel", "elettrico", "metano", "GPL")
marchiOk = ("", "fiat", "toyota", "audi", "bmw", "mercedes", "subaru")
modelliOk = ("", "panda", "yaris", "a3", "serie3", "classeA", "impreza")
coloriOk = ("", "rosso", "grigio", "nero", "bianco", "blu")
alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"

def targaValida(targa) -> bool:
    """controlla se la targa è in un formato valido (del tipo AB123CD)"""
    if len(targa) != 7: # Controllo lunghezza
        return False
    
    for pos in (0,1,5,6): # Controllo lettere ABCD
        lettera = str.upper(targa[pos])
        if lettera not in alfabeto:
            return False
        
    for pos in (2,3,4): # Controllo numeri 123
        numero = targa[pos]
        if numero not in numeri:
            return False
    return True

class Veicolo:
    def __init__(self, targa, marca = "", modello = "", colore = "", cilindrata = 0, alimentazione = "benzina"):
        if not targaValida(targa):
            raise ValueError("targa non accettabile")
        self.__targa = targa
        
        if marca not in marchiOk:
            raise ValueError("marca non accettabile")
        self.__marca = marca
        
        if modello not in modelliOk:
            raise ValueError("modello non accettabile")        
        self.__modello = modello

        if colore not in coloriOk:
            raise ValueError("colore non accettabile")
        self.__colore = colore
        
        if cilindrata < 0 or cilindrata % 100 != 0: # Multiplo di 100, cilindrata positiva
            raise ValueError("cilindrata non accettabile")
        self.__cilindrata = cilindrata
        
        if alimentazione not in alimOk:
            raise ValueError("alimentazione non accettabile")
        self.__alimentazione = alimentazione
        return

    def __str__(self):
        return "Veicolo:" + str(self.__dict__)
    
    def __repr__(self):
        return self.__str__()

    @property
    def targa(self):
        """ proprietà sola lettura: la targa NON deve essere modificabile """
        return self.__targa
    
    @property
    def marca(self):
        """Marca del veicolo"""
        return self.__marca
        
    @marca.setter
    def marca(self, value):
        if value not in marchiOk:
            raise ValueError("marca non accettabile")
        self.__marca = value
        return
    
    @property
    def colore(self):
        """Colore del veicolo"""
        return self.__colore
    
    @colore.setter
    def colore(self, value):
        if value not in coloriOk:
            raise ValueError("colore non accettabile")
        self.__colore = value
        return

    @property
    def cilindrata(self):
        """Cilindrata del veicolo"""
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self,value):
        if value > 0 and value % 100 == 0:
            self.__cilindrata = value
            return
        raise ValueError("Cilindrata non accettabile")
    
    @property
    def alimentazione(self):
        """Alimentazione del veicolo"""
        return self.__alimentazione
        
    @alimentazione.setter
    def alimentazione(self, value):
        if value not in alimOk:
            raise ValueError("alimentazione non valida")
        self.__alimentazione = value
        return

    def __lt__(self, other) -> bool:
        if self.marca < other.marca:
            return True
        
        if self.marca == other.marca and self.modello < other.modello:
            return True
        
        if self.marca == other.marca and self.modello == other.modello and self.cilindrata < other.cilindrata: 
            return True
        return False
