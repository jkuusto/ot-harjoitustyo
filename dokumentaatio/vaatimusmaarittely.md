# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat hakea itse tallentamiaan suosituksia hahmon valintatilanteeseen MOBA-typpisissä, asymmetrisissä kilpailullisissa verkkopeleissä, joissa on usein toistasataa pelattavaa hahmoa.

Sovelluksesta on apua ensisijaisesti silloin, kun vastustaja on valinnut hahmonsa pelissä ensin: Käyttäjä syöttää vastustajan valitseman hahmon sovellukseen ja saa vastauksena listan hahmosuosituksia pelattavaksi.

Toinen käyttötapa on syöttää hahmo, jota käyttäjä on itse aikeissa pelata. Tästä on hyötyä peleissä, joissa on ns. "bannausvaihe" ennen hahmovalintavaihetta, ja käyttäjä saa sovelluksen avulla suosituksia hahmosta, joka kannattaisi sulkea pois vastustajan valikoimasta.

## Käyttäjät

Sovellus ei hyödynnä käyttäjäkirjautumista eikä -tilejä. Oletus on, että jokainen sovelluksen asennus on tarkoitettu käyttäjän henkilökohtaiseen käyttöön.

## Käyttöliittymä

Tekstikäyttöliittymä sopii hyvin sovelluksen tarkoitukseen perusversiossa.

## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi lisätä hahmon (**tehty**)
- Käyttäjä voi nähdä listan kaikista lisätyistä hahmoista (**tehty**)
- Käyttäjä voi poistaa hahmon (**tehty**)
- Käyttäjä voi lisätä hahmolle vastavalinnan, eli hahmon, jota vastaan muokattava hahmo on heikko (**tehty**)
- Käyttäjä voi poistaa vastavalinnan hahmolta
- Käyttäjä voi hakea tietyn hahmon ja saada näkyviin listan hahmoista, joita vastaan valittu hahmo on heikko (**tehty**)

## Jatkokehitysideoita

Sovellusta voi täydentää seuraavilla toiminallisuuksilla:

- Käyttäjä voi muokata hahmon nimeä
  - Hyödyllinen ominaisuus kirjoitusvirheiden varalle
- Käyttäjä näkee hakutuloksissa myös käänteishakuna tehdyn listan hahmoista, joita vastaan valittu hahmo on vahva
  - Tämä tieto auttaa käyttäjää muodostamaan ajan mittaan paremman kokonaiskuvan hahmojen välisistä voimasuhteista
- Käyttäjä voi lisätä kommentteja hahmojen vastavalintatietoihin, kuten suositeltavia taktiikoita tai esine-/loitsuvalintoja
  - Kommentit ovat vastavalintakohtaisia
  - Käyttäjä voi myös muokata kommentteja
- Käyttäjän ei tarvitse lisätä hahmoa ennen vastavalinnan lisäämistä
  - Automaattinen hahmon luonti vastavalinnan luonnin yhteydessä
- Käyttäjä voi tallentaa useiden eri pelien tietoja
- Käyttäjä voi määrittää vastavalinnan vahvuusasteen asteikolla 1-3
  - Tätä tietoa voisi hyödyntää esim. hakutulosten järjestämiseen vahvuusasteen mukaan
  - Vaatii enemmän tietoa ja arviointia käyttäjältä mutta saattaisi olla hyödyllinen työkalu edistyneemmille käyttäjille
- Graafinen käyttöliittymä
- Käyttäjä voi tuoda hahmoja tiedostosta, esim. CSV tai JSON
- Käyttäjä voi tuoda vastavalintadataa tiedostosta
- Käyttäjä voi viedä hakutuloksia tiedostoon
- Käyttäjä voi hakea vastavalintasuosituksia usealle vihollisjoukkueen valitsemalle hahmolle samanaikaisesti
  - Tämä auttaa käyttäjää valitsemaan optimaalisen hahmon vihollisjoukkueen tekemien kaikkien hahmovalintojen perusteella kokonaisuutena
  - Ollakseen hyödyllinen vaatii, että käyttäjä on syöttänyt paljon dataa sovellukseen
- Käyttäjä voi lisätä hahmoille ominaisuuksia
  - Esim. hyökkäyksen ulottuvuutta tai muita ominaisuuksia vertailemalla voisi tehdä tarkempia ja myöhemmin jopa automatisoituja määrityksiä hahmojen välisistä voimasuhteista
  - Vaatii käyttäjältä merkittävää tiedonhakutyötä hahmojen ominaisuuksista
  - Saattaa rajata pois joitakin pelityyppejä
