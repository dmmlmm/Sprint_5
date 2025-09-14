import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from locators import HomePage

class TestModalWindow:
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        print("Инициализация драйвера...")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        print("Драйвер инициализирован")
    
    def teardown_method(self):
        print("Закрытие драйвера...")
        if self.driver:
            self.driver.quit()
        print("Драйвер закрыт")
    
    def test_modal_window_appears(self):
        print("Запуск теста проверки модального окна")
        
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        print("Сайт открыт")
        
        self._click_element(HomePage.AD_CREATION_BUTTON, "Кнопка 'Разместить объявление'")
        
        self._verify_modal_window_displayed()

    def _verify_modal_window_displayed(self):
        try:
            modal_title = self.wait.until(
                EC.visibility_of_element_located(HomePage.MODAL_TITLE)
            )
            
            assert modal_title.is_displayed(), "Модальное окно не отображается"
            
            print("Модальное окно отображается корректно")
            
        except TimeoutException:
            pytest.fail("Модальное окно не отобразилось")
        except AssertionError as e:
            pytest.fail(f"Ошибка проверки модального окна: {e}")

    def _click_element(self, locator, element_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Успешно нажата {element_name}")
        except TimeoutException:
            pytest.fail(f"Элемент {element_name} не найден или не кликабелен")

if __name__ == "__main__":
    test = TestModalWindow()
    test.setup_method()
    try:
        test.test_modal_window_appears()
        print("Тест выполнен успешно!")
    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")
    finally:
        test.teardown_method()