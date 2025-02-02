from parcheggio import Parcheggio

while True:
    # print("Martino è un tontolone")
    scelta = input("Cosa vuoi fare? 'CreaPark / PrenotaPark / LiberaPark / Visualizza Conteggio / Chiudi / Salva ")
    if scelta == "CreaPark": # Crea un posto per un mezzo specifico es. Auto e viene inserito nell'ogetto Parcheggio
        input("Inserisci il tipoMezzo: ")
        parcheggio = Parcheggio.parcheggia((False, None, tipoMezzo, None))

    elif scelta == "Prenota":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        for postoMezzo["auto"] in parcheggio
        postoMezzo = PostoMezzo(targa, tipoMezzo, oreSosta)
        posto = Parcheggio.prenota(targa, oreSosta)
        Parcheggio.append(posto)
        contaPosti[tipoMezzo] -= 1
    elif scelta == "Libera":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        parcheggio.liberaPark(targa, tipoMezzo)
        contaPosti[tipoMezzo] -= 1
    elif scelta == "Visualizza Conteggio":
        print(contaPosti)
    elif scelta == "Salva":
        break
    else:
        input("Cosa vuoi fare? 'CreaPark / PrenotaPark / LiberaPark / Visualizza Conteggio / Chiudi / Salva ")
