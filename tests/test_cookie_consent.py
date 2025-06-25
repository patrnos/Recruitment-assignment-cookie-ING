from playwright.sync_api import Page, expect

def test_scenario_with_analytics_consent(page: Page):
    print("\n--- Test ze zgodą na analitykę ---")
    page.goto("https://www.ing.pl/")

    # Sprawdzenie i próba kliknięcia "Dostosuj" (tylko tutaj if/try)
    hcaptcha_iframe = page.get_by_role("checkbox", name="hCaptcha checkbox with text '")
    if hcaptcha_iframe.is_visible(timeout=500):
        print("Wykryto hCaptcha – próbuję kliknąć 'I am human'...")
        try:
            page.page.get_by_role("checkbox", name="hCaptcha checkbox with text '").click()
        except Exception as e:
            print(f"Nie udało się kliknąć hCaptcha: {e}")

        try:
            expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=500)
            print("Przycisk 'Dostosuj' po hCaptcha jest widoczny.")
        except Exception:
            print("Nie znaleziono przycisku 'Dostosuj' po hCaptcha.")
    else:
        try:
            expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=500)
            print("Przycisk 'Dostosuj' jest widoczny.")
        except Exception:
            print("Nie znaleziono przycisku 'Dostosuj'.")

    # Dalsza część testu – bez żadnych if/try/except
    page.get_by_role("button", name="Dostosuj").click()
    page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
    expect(page.get_by_role("button", name="Zaakceptuj zaznaczone")).to_be_hidden(timeout=2000)

    cookies = page.context.cookies()
    gdpr = next((c for c in cookies if c['name'] == "cookiePolicyGDPR"), None)

    assert gdpr is not None
    assert gdpr['value'] == "3"

    print(f"Sukces: cookiePolicyGDPR = {gdpr['value']}")