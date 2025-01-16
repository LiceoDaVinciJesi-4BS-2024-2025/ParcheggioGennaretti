import datetime
from pathlib import Path
from veicolo import Veicolo
from auto import Auto
from moto import Moto
from autobus import Autobus
from camion import Camion

mezziOK = ("auto", "moto", "camion", "autobus")

class PostoMezzo(Veicolo):
    def __init__(self, targa, tipoMezzo):
        super().__init__(targa)
        self.__libero = False
        if tipoMezzo not in mezziOK:
            self.__tipoMezzo = tipoMezzo
        else:
            raise ValueError("tipoMezzo non valido.")

    def __str__(self):
        if self.libero:
            s = f"Posto {self.__tipoMezzo} libero"
        else:
            s = f"Posto {self.__tipoMezzo} occupato da {self.targa} fino alle {self.oraTermine}"
        return s

        @property
        def tipoMezzo(self):
            return self.__tipoMezzo

        @property
        def libero(self):
            return libero

    def prenota(self, targa, oreSosta):
        if self.libero:
            if self.tipoMezzo in mezziOK:
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
