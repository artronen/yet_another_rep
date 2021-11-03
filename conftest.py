import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="choose language for testing site",
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    print(f"\nstart browser on {user_language} language")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
