from playwright.sync_api import Page, expect, TimeoutError

def test_scenario_with_analytics_consent(page: Page):
    """
    Test weryfikuje, czy po zaznaczeniu cookies analitycznych
    wartość cookiePolicyGDPR wynosi 3.
    """
    print("\n--- Test ze zgodą na analitykę ---")

    page.goto("https://www.ing.pl/")

    def is_dostosuj_visible(timeout_ms=1000) -> bool:
        try:
            expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=timeout_ms)
            return True
        except TimeoutError:
            return False

    # 1. Sprawdź czy "Dostosuj" widoczny
    if not is_dostosuj_visible():
        print("Przycisk 'Dostosuj' nie jest widoczny – próbuję kliknąć w hCaptcha...")

        try:
            # 2. Kliknij hCaptcha
            hcaptcha_frame = page.frame_locator("iframe[title='Widget containing checkbox for hCaptcha security challenge']")
            hcaptcha_frame.locator("#anchor").click()
            print("Kliknięto w hCaptcha.")
        except Exception as e:
            print(f"Błąd podczas klikania w hCaptcha: {e}")

        # 3. Ponownie sprawdź, czy "Dostosuj" się pojawił
        if not is_dostosuj_visible():
            raise AssertionError("Przycisk 'Dostosuj' nadal niewidoczny po próbie kliknięcia w hCaptcha.")

    # Kliknij "Dostosuj"
    page.get_by_role("button", name="Dostosuj").click()

    # Zaznacz analityczne cookies
    page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()

    # Sprawdź, czy baner zniknął
    expect(page.get_by_role("button", name="Zaakceptuj zaznaczone")).to_be_hidden()

    # Weryfikacja ciasteczek
    cookies = page.context.cookies()
    gdpr_cookie = next((cookie for cookie in cookies if cookie['name'] == "cookiePolicyGDPR"), None)

    assert gdpr_cookie is not None, "Nie znaleziono ciasteczka cookiePolicyGDPR"
    assert gdpr_cookie['value'] == "3", f"Oczekiwano wartości '3', otrzymano '{gdpr_cookie['value']}'"

    print(f"Sukces: cookiePolicyGDPR = {gdpr_cookie['value']} (analityczne zaakceptowane)")
