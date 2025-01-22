import datetime
from auto import Auto
from moto import Moto
from autobus import Autobus
from camion import Camion

mezziOK = ("auto", "moto", "camion", "autobus")

class PostoMezzo():
    def __init__(self, tipoMezzo):
        self.__libero = True
        self.__mezzo = ""
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
    def mezzo(self):
        return self.__mezzo

    @property
    def libero(self):
        return self.__libero

    def prenota(self, targa, oreSosta):
        if self.libero:
            if self.__tipoMezzo in mezziOK:
                if self.__tipoMezzo == "auto":
                    self.__mezzo = Auto(targa)
                elif self.__tipoMezzo == "moto":
                    self.__mezzo = Moto(targa)
                elif self.__tipoMezzo == "camion":
                    self.__mezzo = Camion(targa)
                elif self.__tipoMezzo == "autobus":
                    self.__mezzo = Autobus(targa)

                self.libero = False
                ora = datetime.datetime.now()
                self.oraTermine = ora + datetime.timedelta(hours=oreSosta)
                return True
        else:
            return False
