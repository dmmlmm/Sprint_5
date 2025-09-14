import pytest
import pdb
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from locators import LoginPage, HomePage, MakeNewAd, SearchForAd


class TestCreateAdvertisement:
    
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
    
    def test_create_advertisement(self):
        """Тест создания объявления"""
        
        print("Запуск теста создания объявления")
        
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        print("Сайт открыт")
        
        self._login()
        
        self._create_new_advertisement()
        
        self._search_and_verify_advertisement()

    def _login(self):

        self._click_element(LoginPage.LOGIN_BUTTON, "Кнопка 'Вход и регистрация'")
        
        self._fill_login_form()
        
        self._click_element(LoginPage.SUBMIT_LOGIN_BUTTON, "Кнопка 'Войти'")
        
        self.wait.until(EC.visibility_of_element_located(HomePage.HOME_PAGE_INDICATOR))

    def _create_new_advertisement(self):

        self._click_element(HomePage.AD_CREATION_BUTTON, "Кнопка создания объявления")
        
        self._fill_advertisement_form()
        
        self._click_element(MakeNewAd.PUBLICATE_BUTTON, "Кнопка публикации")

    def _fill_advertisement_form(self):

        self._fill_field(MakeNewAd.NAME_FIELD, "Тестовое название")
        print("Заполнено название объявления")
        
        self._fill_field(MakeNewAd.DESCRIPTION, "Тестовое описание")
        print("Заполнено описание объявления")
        
        self._fill_field(MakeNewAd.PRICE, "744")
        print("Заполнена цена")
        
        self._click_element(MakeNewAd.OPEN_TYPE_LIST, "Открытие списка категорий")
        self._click_element(MakeNewAd.TECHNOLOGY_TYPE, "Выбор категории 'Технологии'")
        print("Выбрана категория")

        city_list = self.driver.find_element(By.XPATH, "//input[contains(@name,'city')]/../button",)
        city_list.click()



        self._click_element(MakeNewAd.EKATERINBURG_CITY, "Выбор города 'Екатеринбург'")

        radio_button = self.driver.find_element(By.XPATH, "//input[@name='condition' and @value='Б/У']/../div[@class='radioUnput_inputRegular__FbVbr']",)
        radio_button.click()

        print("Выбрано состояние товара")


    def _search_and_verify_advertisement(self):

        try:
            self._fill_field(SearchForAd.NAME_SEARCH_FIELD, "Тестовое название")
            print("Введено название для поиска")
            
            category_search_list = self.driver.find_element(By.XPATH, "//input[contains(@name,'category')]/../button")
            category_search_list.click()
            
            self._click_element(SearchForAd.SEARCH_TECHNOLOGY_TYPE, "Выбор категории 'Технологии' в поиске")
            print("Выбрана категория для поиска")
            
            self._click_element(SearchForAd.SEARCH_BUTTON, "Кнопка поиска")
            print("Выполнен поиск объявления")

            time.sleep(3)
            
            title_element = self.wait.until(
                EC.presence_of_element_located(SearchForAd.AD_NAME)
            )
            assert title_element.text == "Тестовое название", f"Неверное название объявления: {title_element.text}"
            print("Название объявления корректно")
            
            city_element = self.wait.until(
                EC.presence_of_element_located(SearchForAd.AD_CITY)
            )
            assert city_element.text == "Москва", f"Неверный город: {city_element.text}"
            print("Город объявления корректен")
            
            price_element = self.wait.until(
                EC.presence_of_element_located(SearchForAd.AD_PRICE)
            )
            assert price_element.text == "744 ₽", f"Неверная цена: {price_element.text}"
            print("Цена объявления корректна")
            
            print("Проверка объявления успешно завершена")
            
        except TimeoutException:
            pytest.fail("Не удалось найти элементы объявления")
        except AssertionError as e:
            pytest.fail(f"Ошибка при проверке объявления: {str(e)}")

    def _fill_login_form(self):

        test_data = {
            LoginPage.EMAIL_FIELD: self.email,
            LoginPage.PASSWORD_FIELD: self.password
        }
        
        for field_locator, value in test_data.items():
            self._fill_field(field_locator, value)

    def _fill_field(self, locator, value):

        try:
            field = self.wait.until(EC.visibility_of_element_located(locator))
            field.clear()
            field.send_keys(value)
            print(f"Заполнено поле {locator[1]} значением: {value}")
        except TimeoutException:
            pytest.fail(f"Поле {locator[1]} не найдено")

    def _click_element(self, locator, element_name):
        
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Успешно нажата {element_name}")
        except TimeoutException:
            pytest.fail(f"Элемент {element_name} не найден или не кликабелен")

if __name__ == "__main__":
    test = TestCreateAdvertisement()
    test.setup_method()
    try:
        test.test_create_advertisement()
        print("Тест выполнен успешно!")
    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")
    finally:
        test.teardown_method()