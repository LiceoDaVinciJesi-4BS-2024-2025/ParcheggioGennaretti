from parcheggio import Parcheggio
from parcheggio import postomezzo as PostoMezzo

while True:
    scelta = input("Cosa vuoi fare? 'CreaPark / PrenotaPark / LiberaPark / Visualizza Conteggio / Chiudi / Salva")
    if scelta == "CreaPark": # Crea un posto per un mezzo specifico es. Auto e viene inserito nell'ogetto Parcheggio
        postoMezzo = PostoMezzo(False, targa, tipoMezzo, oreSosta)
        Parcheggio.aggiungiPostoMezzo(postoMezzo)

    elif scelta == "Prenota":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        postoMezzo = PostoMezzo(targa, tipoMezzo, oreSosta)
        posto = Parcheggio.prenota(targa, oreSosta)
        Parcheggio.append(posto)
        contaPosti[tipoMezzo] -= 1
    elif scelta == "Libera":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        posto = PostoMezzo.libera(targa, oreSosta)
        parcheggio.append(posto)
        contaPosti[tipoMezzo] += 1
    elif scelta == "Visualizza Conteggio":
        print(contaPosti)
    elif scelta == "Chiudi":
        break
    else:
        input("Cosa vuoi fare? 'CreaPark / PrenotaPark / LiberaPark / Visualizza Conteggio / Chiudi / Salva")