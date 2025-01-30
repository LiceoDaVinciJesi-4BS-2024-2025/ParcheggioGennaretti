from parcheggio import Parcheggio

while True:
    scelta = input("Cosa vuoi fare? 'CreaPark / PrenotaPark / LiberaPark / Visualizza Conteggio / Chiudi / Salva ")
    if scelta == "CreaPark": # Crea un posto per un mezzo specifico es. Auto e viene inserito nell'ogetto Parcheggio
        input("Inserisci il tipoMezzo: ")
        Parcheggio.aggiungiPostoMezzo((False, None, tipoMezzo, None))

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
        posto = PostoMezzo.libera(targa, oreSosta)
        parcheggio.append(posto)
        contaPosti[tipoMezzo] += 1
    elif scelta == "Visualizza Conteggio":
        print(contaPosti)
    elif scelta == "Salva":
        break
    else:
        input("Cosa vuoi fare? 'CreaPark / PrenotaPark / LiberaPark / Visualizza Conteggio / Chiudi / Salva ")