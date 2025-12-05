# Kielimallien käyttö projektissa

Projektin koodikannassa on osittain kielimallin avulla generoitua koodia seuraavissa osissa:

- counter_repository.py
  - create()
  - find_counters_for()
  - delete()
- ui.py
  - \_add_counter() ja siihen liittyvät apufunktiot
  - \_search_counters() ja siihen liittyvät apufunktiot
  - kuinka \_handle_menu_choice() kutsutaan
  - \_delete_counter()
- counterpicker_service.py
  - kaikki metodit paitsi delete_counter_relationship()

Projektin docstringit ovat alunperin kielimallin kirjoittamia, ja muokattu tarvittaessa.
