from playwright.sync_api import Page, expect

def test_scenario_with_analytics_consent(page: Page):
    print("\n--- Test ze zgodą na analitykę ---")
    page.goto("https://www.ing.pl/")

    # Sprawdzenie i próba kliknięcia "Dostosuj" (tylko tutaj if/try)
    page.get_by_text("Request unsuccessful.").content_frame.locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").content_frame.get_by_role("checkbox", name="hCaptcha checkbox with text '").click()

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