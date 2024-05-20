from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=["chrome", "mozillafirefox"], scope="class")
def invoke_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "mozillafirefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    web_driver.maximize_window()
    web_driver.get("https://qase.io/")
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()