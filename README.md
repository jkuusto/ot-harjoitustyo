# Ohjelmistotekniikka harjoitustyö

**Hahmovalinnan avustaja** perustuen vastustajan hahmovalintaan asymmetrisissä kilpailullisissa verkkopeleissä (_esim. MOBA-pelit_).

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/jkuusto/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/jkuusto/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](https://github.com/jkuusto/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/jkuusto/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Kielimalliseloste](https://github.com/jkuusto/ot-harjoitustyo/blob/main/dokumentaatio/kielimallit.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```
poetry install
```

2. Valinnainen vaihe: Luo oma .env-tiedosto:

```
cp .env.example .env
```

3. Suorita vaadittavat alustustoimenpiteet komennolla:

```
poetry run invoke build
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon ja avataan esim. Chromella komennolla `google-chrome htmlcov/index.html`.
