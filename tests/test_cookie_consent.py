# tests/test_cookie_consent.py
from playwright.sync_api import Page, expect

def test_scenario_with_analytics_consent(page: Page):
    """
    Test weryfikuje, czy po zaznaczeniu cookies analitycznych
    wartość cookiePolicyGDPR wynosi 3.
    """
    print("\n--- Test ze zgodą na analitykę ---")
    
    page.goto("https://www.ing.pl/", timeout=60000)
    page.get_by_role("button", name="Dostosuj").click()
    page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
    
    # Weryfikacja UI - baner powinien zniknąć
    expect(page.get_by_role("button", name="Zaakceptuj zaznaczone")).to_be_hidden()
    
    cookies = page.context.cookies()
    gdpr_cookie = next((cookie for cookie in cookies if cookie['name'] == "cookiePolicyGDPR"), None)
    
    # Asercje wartości cookie
    assert gdpr_cookie is not None, "Nie znaleziono ciasteczka cookiePolicyGDPR"
    assert gdpr_cookie['value'] == "1", f"Oczekiwano wartości '3', otrzymano '{gdpr_cookie['value']}'"
    
    print(f"Sukces: cookiePolicyGDPR = {gdpr_cookie['value']} (analityczne zaakceptowane)")
    


