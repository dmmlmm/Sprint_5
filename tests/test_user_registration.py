import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from locators import LoginPage, RegistrationPage, HomePage

class TestUserRegistration:
    
    def _generate_unique_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"testuser{random_string}@example.com"
    
    def setup_method(self):
        print("Инициализация драйвера...")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        self.test_email = self._generate_unique_email()
        print(f"Сгенерирован email: {self.test_email}")
        
        print("Драйвер инициализирован")
    
    def teardown_method(self):
        print("Закрытие драйвера...")
        if self.driver:
            self.driver.quit()
        print("Драйвер закрыт")
    
    def test_user_registration(self):
        
        print("Запуск теста регистрации пользователя")
        print(f"Используемый email: {self.test_email}")
        
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        print("Сайт открыт")
        
        self._click_element(LoginPage.LOGIN_BUTTON, "Кнопка 'Вход и регистрация'")
        
        self._click_element(LoginPage.NO_ACCOUNT_BUTTON, "Кнопка 'Нет аккаунта'")
        
        self._fill_registration_form()
        
        self._click_element(RegistrationPage.CREATE_ACCOUNT_BUTTON, "Кнопка 'Создать аккаунт'")
        
        self._verify_redirect_to_home_page()
        self._verify_user_avatar_displayed()
        self._verify_user_name_displayed()

    def _click_element(self, locator, element_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Успешно нажата {element_name}")
        except TimeoutException:
            pytest.fail(f"Элемент {element_name} не найден или не кликабелен")

    def _fill_registration_form(self):
        test_data = {
            RegistrationPage.EMAIL_FIELD: self.test_email,
            RegistrationPage.PASSWORD_FIELD: "Password123!",
            RegistrationPage.CONFIRM_PASSWORD_FIELD: "Password123!"
        }
        
        for field_locator, value in test_data.items():
            try:
                field = self.wait.until(EC.visibility_of_element_located(field_locator))
                field.clear()
                field.send_keys(value)
                print(f"Заполнено поле {field_locator[1]} значением: {value}")
            except TimeoutException:
                pytest.fail(f"Поле {field_locator[1]} не найдено")

    def _verify_redirect_to_home_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(HomePage.HOME_PAGE_INDICATOR))
            print("Успешный переход на главную страницу")
        except TimeoutException:
            pytest.fail("Не произошел переход на главную страницу")

    def _verify_user_avatar_displayed(self):
        try:
            avatar = self.wait.until(EC.visibility_of_element_located(HomePage.USER_AVATAR))
            assert avatar.is_displayed(), "Аватар пользователя не отображается"
            print("Аватар пользователя отображается корректно")
        except (TimeoutException, AssertionError):
            pytest.fail("Аватар пользователя не отображается")

    def _verify_user_name_displayed(self):
        try:
            user_name = self.wait.until(EC.visibility_of_element_located(HomePage.USER_NAME))
            assert user_name.is_displayed(), "Имя пользователя не отображается"
            assert "User" in user_name.text, "Имя пользователя не содержит 'User'"
            print("Имя пользователя отображается корректно")
        except (TimeoutException, AssertionError):
            pytest.fail("Имя пользователя не отображается корректно")

if __name__ == "__main__":
    test = TestUserRegistration()
    test.setup_method()
    try:
        test.test_user_registration()
        print("Тест выполнен успешно!")
    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")
    finally:
        test.teardown_method()