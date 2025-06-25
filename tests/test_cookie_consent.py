from playwright.sync_api import Page, expect, TimeoutError

def test_scenario_with_analytics_consent(page: Page):
    """
    Test weryfikuje, czy po zaznaczeniu cookies analitycznych
    wartość cookiePolicyGDPR wynosi 3.
    """
    print("\n--- Test ze zgodą na analitykę ---")
    
    page.goto("https://www.ing.pl/")
    
    try:
        expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=1000)
    except TimeoutError:
        try:
            # Kliknięcie checkboxa hCaptcha wewnątrz iframe
            hcaptcha_frame = page.frame_locator("iframe[title='Widget containing checkbox for hCaptcha security challenge']")
            hcaptcha_frame.locator("#anchor").click()
    
        except Exception as e:
    
            expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=1000)

    # Kliknięcie w "Dostosuj"
    page.get_by_role("button", name="Dostosuj").click()

    # Zgoda na analityczne cookies
    page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()

    # Weryfikacja UI - baner powinien zniknąć
    expect(page.get_by_role("button", name="Zaakceptuj zaznaczone")).to_be_hidden()

    # Weryfikacja ciasteczek
    cookies = page.context.cookies()
    gdpr_cookie = next((cookie for cookie in cookies if cookie['name'] == "cookiePolicyGDPR"), None)

    assert gdpr_cookie is not None, "Nie znaleziono ciasteczka cookiePolicyGDPR"
    assert gdpr_cookie['value'] == "3", f"Oczekiwano wartości '3', otrzymano '{gdpr_cookie['value']}'"

    print(f"Sukces: cookiePolicyGDPR = {gdpr_cookie['value']} (analityczne zaakceptowane)")
