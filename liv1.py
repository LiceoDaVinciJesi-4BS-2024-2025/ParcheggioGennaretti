# Livello 1
# Martino Gennaretti

from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, targa, maxPers, traspPers, marca = "", modello = ""):
        super().__init__(targa, marca, modello)
        self.__maxPers = maxPers
        if traspPers > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = traspPers

    def __str__(self):
        return "Auto:" + str(self.__dict__)
    
    @property
    def maxPers(self):
        return self.__maxPers

    @property
    def traspPers(self):
        return self.__traspPers

    @traspPers.setter
    def traspPers(self, value):
        if value > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = value
        return


class Moto(Veicolo):
    def __init__(self, targa, maxPers, traspPers, marca = "", modello = ""):
        super().__init__(targa, marca, modello)
        self.__maxPers = maxPers
        if traspPers > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = traspPers
    
    def __str__(self):
        return "Moto:" + str(self.__dict__)
    
    @property
    def maxPers(self):
        return self.__maxPers

    @property
    def traspPers(self):
        return self.__traspPers
        
    @traspPers.setter
    def traspPers(self, value):
        if value > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = value
        return


class Autobus(Veicolo):
    def __init__(self, targa, maxPers, traspPers, marca = "", modello = ""):
        super().__init__(targa, marca, modello)
        self.__maxPers = maxPers
        if traspPers > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = traspPers
    
    def __str__(self):
        return "Autobus:" + str(self.__dict__)
    
    @property
    def maxPers(self):
        return self.__maxPers

    @property
    def traspPers(self):
        return self.__traspPers
        
    @traspPers.setter
    def traspPers(self, value):
        if value > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = value
        return


class Camion(Veicolo):
    def __init__(self, targa, maxKg, traspKg, marca = "", modello = ""):
        super().__init__(targa, marca, modello)
        self.__maxKg = maxKg
        if traspKg > self.__maxKg:
            raise ValueError("Il peso della merce supera quello trasportabile")
        self.__traspKg = traspKg
        
    def __str__(self):
        return "Camion:" + str(self.__dict__)
    
    @property
    def maxKg(self):
        return self.__maxKg

    @property
    def traspKg(self):
        return self.__traspKg
        
    @traspKg.setter
    def traspKg(self, value):
        if value > self.__maxKg:
            raise ValueError("Il peso della merce supera quello trasportabile")
        self.__traspKg = value
        return
