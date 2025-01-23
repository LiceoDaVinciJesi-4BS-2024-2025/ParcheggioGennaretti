from postomezzo import PostoMezzo
import datetime
import csv

mezziOK = ("auto", "moto", "camion", "autobus")
class Parcheggio:
    def __init__(self):
        self.__parcheggio = {"auto": "", "moto": "", "camion": "", "autobus": ""}
        self.__contaPosti = {"auto": 1000, "moto": 200, "camion": 50, "autobus": 200}
        self.__guadagnoGG = {"auto": 1.5, "moto": 1.2, "camion": 1.8, "autobus": 2.4}

    def __str__(self):
        a = "Parcheggio: " + str(self.__dict__)
        return a

    @property
    def parcheggio(self):
        """Restituisce il parcheggio"""
        return self.__parcheggio

    @property
    def contaPosti(self):
        """Restituisce il numero di posti per tipo di veicolo"""
        return self.__contaPosti

    @property
    def guadagnoGG(self):
        """Restituisce il guadagno giornaliero per tipo di veicolo"""
        return self.__guadagnoGG

    def guadagnoGiornaliero(self):
        """Restituisce il guadagno giornaliero totale del parcheggio"""
        for tipoMezzo in self.__parcheggio:
            self.__guadagnoGiornaliero[tipoMezzo] = self.__guadagnoGG[tipoMezzo] * self.__parcheggio[tipoMezzo]
        return self.__guadagnoGiornaliero

    def postiLiberi(self, tipoMezzo):
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        return self.__contaPosti[tipoMezzo]
    
    def prenota(self, targa, tipoMezzo, oreSosta):
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

    def modificaFile(self, azione, postoMezzo):
        f = open("park.data", "w")
        if azione == "Prenota":
            scrittore = csv.DictWriter(file, campi)
            else:
                f.write(postoMezzo.mezzo.targa + " " + datetime.datetime.now())
        