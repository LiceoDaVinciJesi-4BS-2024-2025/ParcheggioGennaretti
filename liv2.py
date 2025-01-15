# Livello 2
# Martino Gennaretti

mezziOK = ("auto", "moto", "camion", "autobus")

import datetime
from veicolo import Veicolo

class PostoMezzo(Veicolo):
    def __init__(self, tipoMezzo):
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        self.__tipoMezzo = tipoMezzo
        self.libero = True
        self.oraTermine = ""
    
    def __str__(self):
        if self.libero:
            s = f"Posto {self.__tipoMezzo} libero"
        else:
            s = f"Posto {self.__tipoMezzo} occupato da {self.targa} fino alle {self.oraTermine}"
        return s
    
    @property
    def tipoMezzo(self):
        return self.__tipoMezzo

    def prenota(self, targa, oreSosta):
        if self.libero:
            self.libero = False
            ora = datetime.datetime.now()
            self.oraTermine = ora + datetime.timedelta(hours=oreSosta)
            return True
        else:
            return False

    def libera(self, targa):
        self.libero = True
        self.targa = ""
        self.oraTermine = None
        return
