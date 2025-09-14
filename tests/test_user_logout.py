import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from locators import LoginPage, HomePage, RegistrationPage

class TestUserLogin:
    
    def setup_method(self):
        print("Инициализация драйвера...")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        self.email = "qq123123@qq.com"
        self.password = "Qwerty123"
        
        print("Драйвер инициализирован")
    
    def teardown_method(self):
        print("Закрытие драйвера...")
        if self.driver:
            self.driver.quit()
        print("Драйвер закрыт")
    
    def test_user_login(self):
        
        print("Запуск теста авторизации пользователя")
        print(f"Используемый email: {self.email}")
        
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        print("Сайт открыт")
        
        self._click_element(LoginPage.LOGIN_BUTTON, "Кнопка 'Вход и регистрация'")
        
        self._fill_login_form()

        self._click_element(LoginPage.SUBMIT_LOGIN_BUTTON, "Кнопка 'Войти'")
        
        self._verify_redirect_to_home_page()
        self._verify_user_avatar_displayed()
        self._verify_user_name_displayed()

        self._click_element(HomePage.LOGOUT_BUTTON, "Кнопка 'Выйти'")
        
        self._verify_user_avatar_not_displayed()
        self._verify_user_name_not_displayed()
        self._verify_login_button_displayed()

    def _fill_login_form(self):
        test_data = {
            LoginPage.EMAIL_FIELD: self.email,
            LoginPage.PASSWORD_FIELD: self.password
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

    def _verify_user_avatar_not_displayed(self):
        try:
            time.sleep(2)
            avatars = self.driver.find_elements(*HomePage.USER_AVATAR)
            if avatars:
                assert not avatars[0].is_displayed(), "Аватар пользователя все еще отображается"
            print("Аватар пользователя успешно скрыт")
        except Exception as e:
            print(f"Ошибка при проверке скрытия аватара: {e}")
            pytest.fail("Аватар пользователя не был скрыт после выхода")

    def _verify_user_name_not_displayed(self):
        try:
            user_names = self.driver.find_elements(*HomePage.USER_NAME)
            if user_names:
                assert not user_names[0].is_displayed(), "Имя пользователя все еще отображается"
            print("Имя пользователя успешно скрыто")
        except Exception as e:
            print(f"Ошибка при проверке скрытия имени: {e}")
            pytest.fail("Имя пользователя не было скрыто после выхода")

    def _verify_login_button_displayed(self):
        try:
            login_button = self.wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON))
            assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается"
            print("Кнопка 'Вход и регистрация' отображается корректно")
        except (TimeoutException, AssertionError):
            pytest.fail("Кнопка 'Вход и регистрация' не отображается после выхода")

    def _click_element(self, locator, element_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Успешно нажата {element_name}")
        except TimeoutException:
            pytest.fail(f"Элемент {element_name} не найден или не кликабелен")

if __name__ == "__main__":
    test = TestUserLogin()
    test.setup_method()
    try:
        test.test_user_login()
        print("Тест выполнен успешно!")
    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")
    finally:
        test.teardown_method()