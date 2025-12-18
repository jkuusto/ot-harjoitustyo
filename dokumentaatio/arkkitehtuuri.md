# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmitasoista kerrosarkkitehtuuria koodin pakkausrakenteen ollessa seuraavanlainen:

```mermaid
  graph TD
      UI
      Services
      Repositories
      Entities

      UI --> Services
      Services --> Repositories
      Services --> Entities
      Repositories --> Entities
```

Pakkaus ui vastaa käyttöliittymästä, services sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta. Pakkauksen entities luokat kuvastavat sovelluksen käyttämiä tietokohteita.

## Sovelluslogiikka

Sovelluksen logiikasta vastaavat luokat Character ja Counter.

```mermaid
 classDiagram
    Character "1" <-- "*" Counter : character_id
    Character "1" <-- "*" Counter : counter_character_id
    class Character{
        id
        name
    }
    class Counter{
        id
        character_id
        counter_character_id
    }
```

Toiminnallisista kokonaisuuksista vastaa [CounterPickerService](src/services/counterpicker_service.py). Luokka tarjoaa metodeja käyttöliittymälle kuten:

- `create_character(name)`
- `get_all_characters()`
- `create_counter_relationship(character_id, counter_character_id)`
- `get_counter_details(character_id)`

_CounterPickerServicellä_ on pääsy hahmoihin ja vastavalintasuhteisiin luokkien [CharacterRepository](src/repositories/character_repository.py) ja [CounterRepository](src/repositories/counter_repository.py) kautta. Toteutukset injektoidaan sovelluslogiikalle luokan konstruktorikutsussa.

## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokat `CharacterRepository` ja `CounterRepository` ovat vastuussa tietojen tallentamisesta SQLite-tietokantaan.

Luokat noudattavat repository-suunnittelumallia, jolloin ne ovat mahdollista korvata uusilla toteutuksilla, jos datan tallennustapaa halutaan vaihtaa.

## Päätoiminnallisuudet

Tässä kuvataan sovelluksen päätoiminnallisuuksien toimintalogiikkaa sekvenssikaavioina.

### Vastavalintasuhteen luominen

Ennen vastavalintasuhteen luomista, tulee luoda siihen lisättävät hahmot. Kaaviossa oletetaan, että käyttäjä on jo lisännyt sovellukseen hahmot Alice ja Bob.

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CounterPickerService
  participant CharacterRepository
  participant CounterRepository

  User->>UI: select "Add counter"
  UI->>UI: _add_counter()
  UI->>User: ask "Character name:"
  User->>UI: enter "Bob"
  UI->>CounterPickerService: find_character_by_name("Bob")
  CounterPickerService->>CharacterRepository: find_all()
  CharacterRepository-->>CounterPickerService: [characters]
  CounterPickerService-->>UI: character1

  UI->>User: ask "Counter character name:"
  User->>UI: enter "Alice"
  UI->>CounterPickerService: find_character_by_name("Alice")
  CounterPickerService->>CharacterRepository: find_all()
  CharacterRepository-->>CounterPickerService: [characters]
  CounterPickerService-->>UI: character2

  UI->>CounterPickerService: create_counter_relationship(character1.id, character2.id)
  CounterPickerService->>CounterRepository: create(character1.id, character2.id)
  CounterRepository-->>CounterPickerService: counter
  CounterPickerService-->>UI:
  UI->>User: display "Counter added: Alice counters Bob."
```

UI hakee käyttäjän syöttämiä nimiä vastaavat hahmot CounterPickerRepositoryn kautta CharacterRepositorysta, annetaan hahmojen ID:t argumentteina CounterRepositoryn create-metodille, joka palauttaa counter-olion.

### Vastavalintojen hakeminen hahmolle

Kun hahmolle on lisätty vastavalintoja, niitä voidaan hakea:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CounterPickerService
  participant CharacterRepository
  participant CounterRepository

  User->>UI: select "Search counters"
  UI->>UI: _search_counters()
  UI->>User: ask "Character name:"
  User->>UI: enter "Bob"
  UI->>CounterPickerService: find_character_by_name("Bob")
  CounterPickerService->>CharacterRepository: find_all()
  CharacterRepository-->>CounterPickerService: [characters]
  CounterPickerService-->>UI: character

  UI->>CounterPickerService: get_counter_details(character.id)
  CounterPickerService->>CounterRepository: find_counters_for(character.id)
  CounterRepository-->>CounterPickerService: [counters]

  loop for each counter
    CounterPickerService->>CharacterRepository: find_by_id(counter.counter_character_id)
    CharacterRepository-->>CounterPickerService: counter_character
  end

  CounterPickerService-->>UI: [counter_details]

  UI->>User: display counter list in table format
```

UI hakee käyttäjän syöttämää nimeä vastaavan hahmon CounterPickerServicen kautta CharacterRepositorysta, noudetaan vastavalintahahmojen id:t listana CounterRepositorysta, CounterPickerService hakee id:eitten avulla hahmojen tiedot listana ja UI esittää ne visuaalisesti taulukoituna käyttäjälle.
