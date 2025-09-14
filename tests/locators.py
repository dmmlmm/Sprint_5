from selenium.webdriver.common.by import By

class LoginPage:
    """Локаторы для страницы логина и регистрации"""
    LOGIN_BUTTON = (By.XPATH, "//button[@type='button'][text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button'][text()='Нет аккаунта']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[@type='submit'][text()='Войти']")
    LOGIN_FORM = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]')


class RegistrationPage:
    """Локаторы для формы регистрации"""
    REGISTRATION_FORM = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button[2]')
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_TEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')
    BORDER_RED = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div')

class HomePage:
    """Локаторы для главной страницы"""
    HOME_PAGE_INDICATOR = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/h3')
    POST_AD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button[2]')
    USER_AVATAR = (By.CLASS_NAME, 'svgSmall')
    USER_NAME = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/h3')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/button')
    AD_CREATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button')
    MODAL_TITLE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form')

class MakeNewAd:

    NAME_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[1]/div/div/input')
    DESCRIPTION = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[4]/div/textarea')
    PRICE = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[5]/div/div/input')
    OPEN_TYPE_LIST = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[1]/button')
    TECHNOLOGY_TYPE = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[2]/button[5]/span')
    INACTIVE_RADIO_BUTTON = (By.XPATH, "//input[@name='condition' and @value='Б/У']/../div[@class='radioUnput_inputRegular__FbVbr']")
    PUBLICATE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/button')
    OPEN_CITY_LIST = (By.XPATH, "//input[contains(@name,'city')]/../button")
    EKATERINBURG_CITY = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[2]/button[4]/span')

class SearchForAd:

    NAME_SEARCH_FIELD = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div[1]/div/div/input')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div[2]/button')
    SEARCH_TYPE_LIST = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div[2]/div[1]/div[1]/input')
    SEARCH_TECHNOLOGY_TYPE = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div[2]/div[1]/div[2]/button[5]')
    AD_NAME = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/h2')
    AD_CITY = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/h3')
    AD_PRICE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/h2')
