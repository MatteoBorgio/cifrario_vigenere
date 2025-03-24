# Il Cifrario di Vigenère

Il **cifrario di Vigenère** è un algoritmo crittografico basato su una variante del cifrario di Cesare. A differenza di quest’ultimo, che utilizza una sola chiave per effettuare una sostituzione su tutto il testo, il cifrario di Vigenère impiega una **parola chiave** per determinare più spostamenti differenti nel testo cifrato.

Questo lo rende più sicuro rispetto a un cifrario a sostituzione monoalfabetica, poiché l’uso di una chiave variabile distribuisce le sostituzioni su più alfabeti, impedendo che ogni lettera del testo in chiaro corrisponda sempre alla stessa lettera cifrata. In questo modo si riducono le regolarità statistiche tipiche delle lingue naturali, come la maggiore frequenza di alcune lettere (ad esempio, le vocali), la ripetizione di combinazioni comuni e la prevedibilità delle doppie, rendendo più difficile la crittoanalisi basata sulla distribuzione delle lettere.

## Il cifrario di Vigenère attraverso i secoli

Il cifrario di Vigenère prende il nome dal **diplomatico francese Blaise de Vigenère**, che lo descrisse nel suo trattato *Traité des chiffres* nel 1586. Tuttavia, il metodo era stato concepito già un secolo prima dall’italiano **Leon Battista Alberti** (1466) e poi perfezionato in seguito da **Giovanni Battista Bellaso**, che nel 1553 descrisse un sistema simile basato su una parola chiave segreta.

Nonostante ciò, il cifrario venne erroneamente attribuito a Vigenère, il cui nome rimase associato alla versione polialfabetica descritta nel suo trattato.

Questo sistema crittografico venne considerato **indecifrabile per quasi tre secoli**, guadagnandosi il soprannome di “*le chiffre indéchiffrable*” in Francia. Il cifrario rimase uno degli strumenti crittografici più affidabili fino a metà dell’Ottocento, quando venne definitivamente violato. Il primo a scoprire una tecnica per decifrarlo sistematicamente fu **Charles Babbage**, matematico e inventore britannico, durante la **Guerra di Crimea** (1853-1856). Il suo lavoro non venne però pubblicato ufficialmente, in quanto coperto da segreto militare, e rimase sconosciuto per anni. In modo indipendente, nel 1863, il crittografo prussiano **Friedrich Kasiski** sviluppò lo stesso metodo di Babbage, che consisteva nel determinare la lunghezza della chiave analizzando la ripetizione di sequenze di lettere nel testo cifrato. Il metodo di Kasiski permetteva di ricostruire la chiave e, di conseguenza, decifrare il messaggio, segnando la fine dell’era del cifrario di Vigenère come sistema crittografico sicuro.

## Funzionamento del Cifrario

Il cifrario di Vigenère utilizza una **tabella di sostituzione**, chiamata ***tabula recta***, che contiene 26 righe, ognuna delle quali è una versione traslata dell’alfabeto:

# Il Cifrario di Vigenère

Il **cifrario di Vigenère** è un algoritmo crittografico basato su una variante del cifrario di Cesare. A differenza di quest’ultimo, che utilizza una sola chiave per effettuare una sostituzione su tutto il testo, il cifrario di Vigenère impiega una **parola chiave** per determinare più spostamenti differenti nel testo cifrato.

Questo lo rende più sicuro rispetto a un cifrario a sostituzione monoalfabetica, poiché l’uso di una chiave variabile distribuisce le sostituzioni su più alfabeti, impedendo che ogni lettera del testo in chiaro corrisponda sempre alla stessa lettera cifrata. In questo modo si riducono le regolarità statistiche tipiche delle lingue naturali, come la maggiore frequenza di alcune lettere (ad esempio, le vocali), la ripetizione di combinazioni comuni e la prevedibilità delle doppie, rendendo più difficile la crittoanalisi basata sulla distribuzione delle lettere.

## Il cifrario di Vigenère attraverso i secoli

Il cifrario di Vigenère prende il nome dal **diplomatico francese Blaise de Vigenère**, che lo descrisse nel suo trattato *Traité des chiffres* nel 1586. Tuttavia, il metodo era stato concepito già un secolo prima dall’italiano **Leon Battista Alberti** (1466) e poi perfezionato in seguito da **Giovanni Battista Bellaso**, che nel 1553 descrisse un sistema simile basato su una parola chiave segreta.

Nonostante ciò, il cifrario venne erroneamente attribuito a Vigenère, il cui nome rimase associato alla versione polialfabetica descritta nel suo trattato.

Questo sistema crittografico venne considerato **indecifrabile per quasi tre secoli**, guadagnandosi il soprannome di “*le chiffre indéchiffrable*” in Francia. Il cifrario rimase uno degli strumenti crittografici più affidabili fino a metà dell’Ottocento, quando venne definitivamente violato. Il primo a scoprire una tecnica per decifrarlo sistematicamente fu **Charles Babbage**, matematico e inventore britannico, durante la **Guerra di Crimea** (1853-1856). Il suo lavoro non venne però pubblicato ufficialmente, in quanto coperto da segreto militare, e rimase sconosciuto per anni. In modo indipendente, nel 1863, il crittografo prussiano **Friedrich Kasiski** sviluppò lo stesso metodo di Babbage, che consisteva nel determinare la lunghezza della chiave analizzando la ripetizione di sequenze di lettere nel testo cifrato. Il metodo di Kasiski permetteva di ricostruire la chiave e, di conseguenza, decifrare il messaggio, segnando la fine dell’era del cifrario di Vigenère come sistema crittografico sicuro.

## Funzionamento del Cifrario

Il cifrario di Vigenère utilizza una **tabella di sostituzione**, chiamata ***tabula recta***, che contiene 26 righe, ognuna delle quali è una versione traslata dell’alfabeto:

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y


### Cifratura

1. Si sceglie una **parola chiave** (ad esempio, “LEMON”).
2. Si ripete la parola chiave fino a raggiungere la lunghezza del testo in chiaro.  
   - **Testo in chiaro**: `ATTACKATDAWN`  
   - **Chiave ripetuta**: `LEMONLEMONLE`
3. Ogni lettera del testo viene cifrata utilizzando la tabula recta:  
   - `A` con chiave `L` → `L`
   - `T` con chiave `E` → `X`
   - `T` con chiave `M` → `F`
   - Risultato: **`LXFOPVEFRNHR`**

---

## Implementazione del cifrario di Vigenère

Per implementare il cifrario, possiamo seguire questa struttura in Python:

```python
def genera_tabula_recta() -> list[list[str]]:
    """Genera e restituisce la tabula recta, una matrice 26x26 di alfabeti traslati."""
    pass

def cifra(messaggio: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Cifra un messaggio con il cifrario di Vigenère usando la tabula recta."""
    pass

def decifra(messaggio_cifrato: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Decifra un messaggio cifrato con il cifrario di Vigenère."""
    pass

def normalizza_testo(testo: str) -> str:
    """Rimuove caratteri non alfabetici e converte tutto in maiuscolo."""
    pass

def estendi_chiave(chiave: str, lunghezza: int) -> str:
    """Espande la chiave fino alla lunghezza richiesta ripetendola ciclicamente."""
    pass

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
def genera_tabula_recta():
    matrice = []
    for i in range(26):
        riga = [(chr(((j % 26) + 65))) for j in range(i, i + 26)]
        matrice.append(riga)
    return matrice
