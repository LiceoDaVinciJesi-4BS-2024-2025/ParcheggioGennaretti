from postomezzo import PostoMezzo

mezziOK = ("auto", "moto", "camion", "autobus")
class Parcheggio:
    def __init__(self):
        self.__parcheggio = {"auto": [], "moto": [], "camion": [], "autobus": []}
        self.__guadagnoGG = {"auto": 1.5, "moto": 1.2, "camion": 1.8, "autobus": 2.4}

    def __str__(self):
        a = "Parcheggio: " + str(self.__dict__)
        return a

    @property
    def parcheggio(self):
        """Restituisce il parcheggio"""
        return self.__parcheggio

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
        return len(self.__parcheggio[tipoMezzo])
    
    def aggiungiPostoMezzo(self, postoMezzo):
        if not isinstance(postoMezzo, PostoMezzo):
            raise ValueError("postoMezzo non accettabile")
        self.__parcheggio[postoMezzo.tipoMezzo] = postoMezzo
        return
