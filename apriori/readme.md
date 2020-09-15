# Assotsiatsioonireeglid

## A osa

Tekkisid järgmised klastrid: `apriori.exe -tm input.txt output.txt` (Address{n})
- 8 11 3 (11.1111)
- 13 9 6 5 1 16 10 14 2 (22.2222)
- 15 12 7 4 3 2 (33.3333)

Sama tulemuse sai ka veergude ja ridade ümber paigutamisel

Vaatab, mida transponeerimine annab: (Transaction{n})
- 1 3 8 (12.5)
- 7 6 4 (12.5)
- 2 5 9 (37.5)

Endiselt 3 klastrit

Ent klastrid polnud perfektsed: `apriori.exe -tc input.txt output.txt` (Address{n})
- 8 11 (33.3333)
- 8 11 3 (11.1111)
- 13 9 6 5 1 16 10 14 2 (22.2222)
- 15 12 7 4 3 2 (33.3333)
- 10 14 (33.3333)
- 3 (44.4444)
- 2 (55.5556)

Nagu näha, siis oli kummalisi kombinisatsioone. (Address{n})
- 8 11 (33.3333)
- 8 11 3 (11.1111)

Kus 3 ei suutnud ära otsustada, et kumba klastrisse ta kuuluda sooviks

Sama ka veergudega: (Transaction{n})
- 2 5 9 (37.5)
- 2 5 9 6 4 (6.25)
- 7 6 4 (12.5)
- 6 4 (56.25)

Siin 6 ja 4 kombinisatsioon ei suutnud ära otsustada, et kuhu ta kuuluda tahab.

Päris elus polegi klastrid perfektsed ning see vist peakski olema hetke väljund, et sellest aru saaks

## B osa

Tekkisid järgmised klastrid: `apriori.exe -tm input.txt output.txt` (Header #{n})
- 3 4 8 9 (7.14286)
- 3 6 9 (7.14286)
- 3 5 8 (7.14286)
- 3 5 9 (7.14286)
- 1 4 7 9 (7.14286)
- 1 6 8 7 (7.14286)
- 4 2 8 7 9 (7.14286)
- 6 2 8 9 (7.14286)
- 6 2 7 (7.14286)
- 5 2 8 7 (7.14286)
- 5 2 7 9 (7.14286)

Siin pole otseselt esilekerkivaid klastreid vaid andmed on ühtlaselt jaotunud

Proovib transponeerides: (Transaction{n})
- 6 5 9 7 (11.1111)
- 6 5 10 14 4 (11.1111)
- 6 2 7 14 11 12 (11.1111)
- 1 13 2 3 (11.1111)
- 1 8 9 2 11 (11.1111)
- 1 8 2 3 14 4 12 (11.1111)
- 13 5 9 10 7 3 11 4 12 (11.1111)
- 8 10 14 11 4 12 (11.1111)

Sama lugu.

Märkimisväärselt ühtlasi on jaotunud see. Tundub, et isegi tehislikult hästi. Pole kõrvalekallet ega midagi.

`apriori.exe -tc input.txt output.txt` nii tulpade kuid ka veergudega annavad ühtlaselt jaotunud seaduspära kuid mõned kombinisatsioonid on veidi sagedasemad

Assotsiatsioonireeglitest märkimisväärne on see, et value `> 10` -> `suspicious transaction` 100% ajast

Muud assotsiatsioonireeglid olid väikeste tõenäosustega arvestades ridade arvu

Ridade ja veergude ära vahetamine annab, assotsiatsiooni reegli põhjal, et esimesed 2 rida on sarnased.