import pytest
from playwright.sync_api import Playwright, BrowserContext

# Globalne ustawienia timeoutów
def pytest_configure(config):
    config.option.timeout = 60000  

# Ustawienia dla każdej strony
@pytest.fixture(scope="function")
def page(context: BrowserContext):
    page = context.new_page()
    
    # Zwiększone timeouty
    page.set_default_timeout(30000) 
    page.set_default_navigation_timeout(60000)  # 60s dla nawigacji
    
    # Włącz śledzenie (trace)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield page
    
    # Zapis trace po teście
    context.tracing.stop(path=f"trace-{pytest.browser_name}.zip")
    page.close()

# Fixture dla nazwy przeglądarki
@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser")
