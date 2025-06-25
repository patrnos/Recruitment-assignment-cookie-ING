# ING Cookie Consent Automation Test

Automatyczny test sprawdzający obsługę zgody na cookie analityczne na stronie ING.pl, napisany w Pythonie z użyciem Playwright.

## Wymagania

- Python 3.8+
- [Playwright for Python](https://playwright.dev/python/)
- pytest, pytest-playwright

## Instalacja

1. Utwórz i aktywuj wirtualne środowisko:
python -m venv venv

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate



2. Zainstaluj zależności:
pip install -r requirements.txt
playwright install



## Uruchamianie testów lokalnie

- Domyślnie (chromium):
pytest


- Konkretna przeglądarka:
  
pytest --browser chromium

pytest --browser firefox

pytest --browser webkit


- Wszystkie przeglądarki równocześnie:
pytest --browser chromium --browser firefox --browser webkit



## Struktura projektu

- `tests/` – pliki z testami
- `requirements.txt` – zależności
- `.github/workflows/` – pipeline CI/CD

## Automatyzacja (CI/CD)

Testy są automatycznie uruchamiane w GitHub Actions na każdą zmianę w repozytorium. Pipeline wykonuje testy we wszystkich wspieranych przeglądarkach (Chromium, Firefox, WebKit) równolegle.

## Wyniki

- Po przejściu testów otrzymasz komunikat o sukcesie.
- W przypadku błędów, trace z testów zostanie zapisany jako artefakt do pobrania.

## Uwaga dotycząca CAPTCHA

Automatyczne testy mogą być blokowane przez mechanizmy CAPTCHA obecne na stronie produkcyjnej ING. W szczególności podczas uruchamiania testów w środowisku CI/CD (np. GitHub Actions) pojawia się CAPTCHA, która uniemożliwia pełne przejście testu bez interakcji użytkownika.

**Rekomendacje:**
- Zaleca się uruchamianie testów automatycznych na środowisku testowym, gdzie CAPTCHA jest wyłączona lub skonfigurowana w trybie testowym.

- W środowiskach produkcyjnych, gdzie nie można wyłączyć CAPTCHA, pełna automatyzacja testów nie jest możliwa.
