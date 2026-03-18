import pytest
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from helpers.urls import BASE_URL, API_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    driver.implicitly_wait(5)
    driver.get(BASE_URL)

    yield driver
    driver.quit()


@pytest.fixture
def authenticated_user(driver):
    email = f"testuser_{random.randint(1000, 9999)}@test.ru"
    password = "password123"

    response = requests.post(
        f"{API_URL}/auth/register",
        json={
            "email": email,
            "password": password,
            "name": "TestUser"
        }
    )

    if response.status_code != 200:
        pytest.fail(f"Failed to create test user: {response.text}")

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(email, password)

    driver.get(BASE_URL)

    return {"email": email, "password": password}