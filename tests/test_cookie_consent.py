from playwright.sync_api import Page, expect, TimeoutError

def test_scenario_with_analytics_consent(page: Page):
    print("\n--- Test ze zgodą na analitykę ---")

    page.goto("https://www.ing.pl/")

    try:
        expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=1000)
    except TimeoutError:
        try:
            page.frame_locator("iframe[title='Widget containing checkbox for hCaptcha security challenge']") \
                .locator("#anchor").click()
        except:
            pass
        expect(page.get_by_role("button", name="Dostosuj")).to_be_visible(timeout=1000)

    page.get_by_role("button", name="Dostosuj").click()
    page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
    expect(page.get_by_role("button", name="Zaakceptuj zaznaczone")).to_be_hidden()

    cookies = page.context.cookies()
    gdpr = next((c for c in cookies if c['name'] == "cookiePolicyGDPR"), None)

    assert gdpr is not None
    assert gdpr['value'] == "3"

    print(f"Sukces: cookiePolicyGDPR = {gdpr['value']}")