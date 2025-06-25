## Scenariusz testowy: Akceptacja cookies analitycznych na stronie ING.pl

**Cel:**  
Zweryfikowanie, czy po zaakceptowaniu wyłącznie cookies analitycznych na stronie głównej ING.pl, w przeglądarce zostaje ustawione ciasteczko `cookiePolicyGDPR` o wartości `3`.

**Kroki:**
1. Otwórz stronę https://www.ing.pl/
2. Kliknij przycisk "Dostosuj" na banerze cookies.
3. Włącz przełącznik "Cookies analityczne".
4. Kliknij "Zaakceptuj zaznaczone".
5. Zweryfikuj, że baner zniknął.
6. Sprawdź, czy istnieje ciasteczko `cookiePolicyGDPR` o wartości `3`.
