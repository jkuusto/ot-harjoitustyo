# Käyttöohje

Voit ladata projektin viimeisimmän [releasen](https://github.com/jkuusto/ot-harjoitustyo/releases) lähdekoodin valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Tietokannan tiedostonimen voi halutessaan konfiguroida mieleisekseen. Luo oma _.env_-tiedosto seuraavalla komennolla:

```bash
cp .env.example .env
```

Muuta näin luodussa _.env_-tiedostossa oleva tietokannan nimi haluamaksesi. Tiedosto ja sen tarvitsema _data_-hakemisto luodaan automaattisesti, jos niitä ei vielä ole olemassa.

## Sovelluksen käynnistäminen

Ennen ensimmäistä käynnistämistä asenna riippuvuudet komennolla:

```bash
poetry install
```

Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Ohjelman pystyy jatkossa käynnistämään komennolla:

```bash
poetry run invoke start
```

## Sovelluksen käyttö

1. Ennen countereiden (vastavalintasuhteiden) lisäämistä tulee sovellukseen lisätä hahmoja.
   - Lisää hahmoja valitsemalla `Add character` ja syöttämällä hahmon nimi.
2. Ennen countereiden hakua tulee sovellukseen lisätä vähintään yksi hahmojen välinen counter-suhde.
   - Lisää counter valitsemalla `Add counter` ja syöttämällä ensin hahmon nimi, jolle counter lisätään; syötä sen jälkeen hahmon nimi, joka toimii counterina em. hahmolle.
3. Nyt voit hakea countereita valitsemalla `Search counters` ja syöttämällä sen hahmon nimen, jonka counterit haluat nähdä.

Countereita ja hahmoja voi poistaa valinnoilla `Delete counter` ja `Delete character`.

Sovellus suljetaan valitsemalla `Exit`.
