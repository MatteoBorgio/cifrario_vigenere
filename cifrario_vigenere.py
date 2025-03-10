def genera_tabula_recta() -> list[list[str]]:
    """Genera e restituisce la tabula recta, una matrice 26x26 di alfabeti traslati."""
    matrice = []
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        riga = []
        for j in range(i, 26 + i):
            riga.append(alfabeto[j - 26])
        matrice.append(riga)
    return matrice


def cifra(messaggio: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Cifra un messaggio con il cifrario di Vigenère usando la tabula recta.

    Args:
        messaggio: Il testo da cifrare (solo lettere A-Z, senza spazi o caratteri speciali).
        chiave: La parola chiave usata per la cifratura.
        tabula_recta: La tabula recta pre-generata.

    Returns:
        Il testo cifrato.
    """
    chiave_cifratura = estendi_chiave(chiave, len(messaggio))

    messaggio_cifrato = ""
    for i in range(len(messaggio)):
        indice_messaggio = tabula_recta[0].index(messaggio[i].upper())
        indice_chiave = tabula_recta[0].index(chiave_cifratura[i].upper())
        messaggio_cifrato += tabula_recta[indice_chiave][indice_messaggio]

    return messaggio_cifrato.upper()


def decifra(messaggio_cifrato: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Decifra un messaggio cifrato con il cifrario di Vigenère usando la tabula recta.

    Args:
        messaggio_cifrato: Il testo cifrato.
        chiave: La parola chiave usata per la cifratura.
        tabula_recta: La tabula recta pre-generata.

    Returns:
        Il testo decifrato.
    """
    chiave_cifratura = estendi_chiave(chiave, len(messaggio_cifrato))

    messaggio_decifrato = ""
    for i in range(len(messaggio_cifrato)):
        indice_chiave = tabula_recta[0].index(chiave_cifratura[i].upper())
        indice_messaggio_cifrato = tabula_recta[indice_chiave].index(messaggio_cifrato[i])
        messaggio_decifrato += tabula_recta[0][indice_messaggio_cifrato]

    return messaggio_decifrato


def normalizza_testo(testo: str) -> str:
    """Rimuove caratteri non alfabetici e converte tutto in maiuscolo per garantire compatibilità con la cifratura.

    Args:
        testo: Il testo di input.

    Returns:
        Il testo pulito e in maiuscolo.
    """
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    testo_normalizzato = ""
    for carattere in testo.upper():
        if carattere in alfabeto:
            testo_normalizzato += carattere

    return testo_normalizzato


def estendi_chiave(chiave: str, lunghezza: int) -> str:
    """Espande la chiave fino alla lunghezza richiesta ripetendola ciclicamente.

    Args:
        chiave: La parola chiave originale.
        lunghezza: La lunghezza del testo da cifrare/decifrare.

    Returns:
        La chiave estesa.
    """
    i = 0
    chiave_cifratura = ""
    while len(chiave_cifratura) != lunghezza:
        if i >= len(chiave):
            i = 0
        chiave_cifratura += chiave[i]
        i += 1

    return chiave_cifratura


def main():
    """Funzione principale che gestisce l'interazione con l'utente."""
    print("Cifrario di Vigenère")

    tabula_recta = genera_tabula_recta()

    scelta = input("Vuoi cifrare (C) o decifrare (D)? ").strip().upper()

    if scelta == "C":
        messaggio = input("Inserisci il messaggio da cifrare: ")
        chiave = input("Inserisci la chiave: ")
        messaggio = normalizza_testo(messaggio)
        chiave = normalizza_testo(chiave)
        chiave_estesa = estendi_chiave(chiave, len(messaggio))
        testo_cifrato = cifra(messaggio, chiave_estesa, tabula_recta)
        print(f"Testo cifrato: {testo_cifrato}")

    elif scelta == "D":
        messaggio_cifrato = input("Inserisci il messaggio cifrato: ")
        chiave = input("Inserisci la chiave: ")
        messaggio_cifrato = normalizza_testo(messaggio_cifrato)
        chiave = normalizza_testo(chiave)
        chiave_estesa = estendi_chiave(chiave, len(messaggio_cifrato))
        testo_decifrato = decifra(messaggio_cifrato, chiave_estesa, tabula_recta)
        print(f"Testo decifrato: {testo_decifrato}")

    else:
        print("Scelta non valida.")


if __name__ == "__main__":
    main()
