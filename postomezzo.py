import datetime
from pathlib import Path
from auto import Auto
from moto import Moto
from autobus import Autobus
from camion import Camion

mezziOK = ("auto", "moto", "camion", "autobus")

class PostoMezzo(Veicolo):
    def __init__(self, targa, marca = "", modello = "", colore = "", cilindrata = 0, alimentazione = "benzina"):
        super().__init__(targa, marca, modello, colore, cilindrata, alimentazione)
         self.__libero = False

    def __str__(self):
        if self.libero:
            s = f"Posto {self.__tipoMezzo} libero"
        else:
            s = f"Posto {self.__tipoMezzo} occupato da {self.targa} fino alle {self.oraTermine}"
        return s
    
    derf

class PostoMezzo(Auto):
    
    
    @property
    def tipoMezzo(self):
        return self.__tipoMezzo

    def prenota(self, targa, oreSosta):
        if self.libero:
            if self.tipoMezzo == mezziOK[0]:
                self.libero = False
                self.targa = targa
                ora = datetime.datetime.now()
                self.oraTermine = ora + datetime.timedelta(hours=oreSosta)
                return True
        else:
            return False

    def libera(self, targa):
        self.targa = ""
        self.libero = True
        self.oraTermine = None
        return
