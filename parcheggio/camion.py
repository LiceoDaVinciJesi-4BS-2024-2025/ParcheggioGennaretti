from veicolo import Veicolo

class Camion(Veicolo):
    def __init__(self, targa: str, maxKg: float, traspKg: float, marca: str = "", modello: str = ""):
        super().__init__(targa, marca, modello)
        self.__maxKg = maxKg
        if traspKg > self.__maxKg:
            raise ValueError("Il peso della merce supera quello trasportabile")
        self.__traspKg = traspKg
        
    def __str__(self):
        return "Camion:" + str(self.__dict__)
    
    @property
    def maxKg(self):
        """Peso massimo trasportabile"""
        return self.__maxKg

    @property
    def traspKg(self):
        """Peso trasportato"""
        return self.__traspKg
        
    @traspKg.setter
    def traspKg(self, value):
        if value > self.__maxKg:
            raise ValueError("Il peso della merce supera quello trasportabile")
        self.__traspKg = value
        return
