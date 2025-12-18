# Changelog

## Viikko 3

- Käyttäjä voi lisätä hahmon
- Käyttäjä näkee listan kaikista listäyistä hahmoista
- Lisätty Character entity-luokka, joka edustaa yksittäisiä hahmoja
- Lisätty CharacterRepository-luokka, joka vastaa hahmojen lisäämisestä, hausta ja poistosta tietokannasta
- Lisätty UI-luokka, joka vastaa käyttöliittymälogiikasta
- Lisätty ConsoleIO-luokka, joka vastaa käyttäjäsyötteestä ja terminaaliin tulostuksesta
- Lisätty TestCharacter-luokka, joka vastaa hahmoihin liittyvistä testeistä
- Testattu, että hahmo voidaan luoda Character-luokkaa käyttäen
- Lisätty mahdollisuus luoda coverage-testikattavuusraportti
- Lisätty invoke-taskit sovelluksen käynnistämiselle, testaukselle ja testikattavuusraportille

## Viikko 4

- Lisätty Pylint ja Autopep8 koodikannan siistimiseksi
- Käyttäjä voi poistaa hahmon
- Käyttäjän kirjoittama hahmo tunnistetaan kirjainkoosta riippumatta
- Testattu, että hahmon str ja repr tulostuvat oikein
- Lisätty testitietokantakonfiguraatio
- Testattu hahmorepositorion metodien toimivuus
- Selkeytetty käyttäjäviestejä
- Lisätty luokkakaavio havainnollistamaan sovelluksen rakennetta

## Viikko 5

- Käyttäjä voi lisätä vastavalinnan
- Käyttäjä voi hakea lisättyjä vastavalintoja hahmolle
- Testattu, että vastavalinta voidaan lisätä
- Testattu, että vastavalinnan haku hakee oikeat hahmot
- Korjattu SQL on delete cascade -bugi
- Lisätty sekvenssikaavioita havainnollistamaan sovelluksen toimintalogiikkaa

## Viikko 6

- Käyttäjä voi poistaa vastavalintasuhteen
- Lisätty docstringejä koodikannan luettavuuden parantamiseksi
- Koodikanta refaktoroitu käyttämään service layeria
- Arkkitehtuuridokumentointiin lisätty rakennekuvaus
- Arkkitehtuuridokumentoinnin sovelluslogiikkaosiota laajennettu
- Arkkitehtuuridokumentoinnin sekvenssidiagrammit päivitetty vastaamaan refaktoroitua koodikantaa
- Lisätty käyttöohje

## Viikko 7

- Testattu, että hahmon lisäys toimii servicellä
- Lisätty testausraportti
- Dokumentointia päivitetty
