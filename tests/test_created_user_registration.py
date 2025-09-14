import pytest
import random
import time
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from locators import LoginPage, RegistrationPage, HomePage

class TestUserRegistration:
    
    
    def setup_method(self):
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
    
    def test_user_registration_validation(self):
        
        print("Запуск теста валидации полей регистрации")
        print(f"Используемый email: qq123123@qq.com")
        
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        print("Сайт открыт")
        
        self._click_element(LoginPage.LOGIN_BUTTON, "Кнопка 'Вход и регистрация'")
        
        self._click_element(LoginPage.NO_ACCOUNT_BUTTON, "Кнопка 'Нет аккаунта'")
        
        self._fill_registration_form()
        
        self._click_element(RegistrationPage.CREATE_ACCOUNT_BUTTON, "Кнопка 'Создать аккаунт'")

        print("Ожидание 10 секунд для применения стилей...")
        time.sleep(10)
        
        self._verify_all_fields_highlighted_red()
        self._verify_error_message_displayed()

    def _verify_all_fields_highlighted_red(self):
        try:
            border_element = self.wait.until(
                EC.visibility_of_element_located(
                    (RegistrationPage.BORDER_RED)
                )
            )
            
            border = border_element.value_of_css_property("border")
            print(f"CSS border поля: {border}")
            
            expected_border = "0.8px solid rgb(255, 105, 114)"
            
            assert expected_border in border, f"Поле не выделено красным цветом. Ожидалось: {expected_border}, Получено: {border}"
            
            print("✓ Все поля выделены красным цветом (0.8px solid rgb(255, 105, 114))")
            
        except (TimeoutException, AssertionError) as e:
            pytest.fail(f"Ошибка проверки красных границ полей: {e}")

    def _verify_error_message_displayed(self):
        try:
            error_message = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')
                )
            )
            
            assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
            assert "Ошибка" in error_message.text, f"Сообщение не содержит текст 'Ошибка'. Текст: {error_message.text}"
            
            print(f"✓ Отображается сообщение об ошибке: {error_message.text}")
            
        except TimeoutException:
            pytest.fail("Сообщение об ошибке 'Ошибка' не найдено")

    def _click_element(self, locator, element_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Успешно нажата {element_name}")
        except TimeoutException:
            pytest.fail(f"Элемент {element_name} не найден или не кликабелен")

    def _fill_registration_form(self):
        test_data = {
            RegistrationPage.EMAIL_FIELD: "qq123123@qq.com",
            RegistrationPage.PASSWORD_FIELD: "Qwerty123",
            RegistrationPage.CONFIRM_PASSWORD_FIELD: "Qwerty123"
        }
        
        for field_locator, value in test_data.items():
            try:
                field = self.wait.until(EC.visibility_of_element_located(field_locator))
                field.clear()
                field.send_keys(value)
                print(f"Заполнено поле {field_locator[1]} значением: {value}")
            except TimeoutException:
                pytest.fail(f"Поле {field_locator[1]} не найдено")

if __name__ == "__main__":
    test = TestUserRegistration()
    test.setup_method()
    try:
        test.test_user_registration_validation()
        print("Тест выполнен успешно!")
    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")
    finally:
        test.teardown_method()

    def _click_element(self, locator, element_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Успешно нажата {element_name}")
        except TimeoutException:
            pytest.fail(f"Элемент {element_name} не найден или не кликабелен")

    def _fill_registration_form(self):
        test_data = {
            RegistrationPage.EMAIL_FIELD: "qq123123@qq.com",
            RegistrationPage.PASSWORD_FIELD: "Qwerty123",
            RegistrationPage.CONFIRM_PASSWORD_FIELD: "Qwerty123"
        }
        
        for field_locator, value in test_data.items():
            try:
                field = self.wait.until(EC.visibility_of_element_located(field_locator))
                field.clear()
                field.send_keys(value)
                print(f"Заполнено поле {field_locator[1]} значением: {value}")
            except TimeoutException:
                pytest.fail(f"Поле {field_locator[1]} не найдено")

