from postomezzo import PostoMezzo

parcheggio = {"auto": "", "moto": "", "camion": "", "autobus": ""}
contaPosti = {"auto": 1000, "moto": 200, "camion": 50, "autobus": 200}
guadagnoGG = {"auto": 1.5, "moto": 1.2, "camion": 1.8, "autobus": 2.4}

class Parcheggio(PostoMezzo):
    def __init__(self):
        super().__init__(targa, libero)
        self.__guadagnoGiornaliero
    @property
    def contaPosti(self):
        return self.__contaPosti

    @property
    def guadagnoGiornaliero(self):
        return self.__guadagnoGiornaliero

    def __str__(self):
        a = "Parcheggio: " + str(self.__dict__)
        return a

    def postiLiberi(self, tipoMezzo):
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        return self.__contaPosti[tipoMezzo]

    def aggiornaFile(self, azione, postoMezzo):
        f = open("park.data", "w")
        if azione == "Prenota":
            f.write(postoMezzo)
        else:
            f.write(targa + " " + datetime.datetime.now())
