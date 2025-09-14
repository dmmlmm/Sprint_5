from selenium.webdriver.common.by import By

class LoginPage:
    """Локаторы для страницы логина и регистрации"""
    LOGIN_BUTTON = (By.XPATH, "//button[@type='button'][text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button'][text()='Нет аккаунта']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[@type='submit'][text()='Войти']")
    LOGIN_FORM = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")


class RegistrationPage:
    """Локаторы для формы регистрации"""
    REGISTRATION_FORM = (By.CLASS_NAME, "popUp_shell__LuyqR")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_TEXT = (By.XPATH, "//*[contains(text(),'Ошибка')]")
    BORDER_RED = (By.CSS_SELECTOR, ".input_inputError__fLUP9")

class HomePage:
    """Локаторы для главной страницы"""
    HOME_PAGE_INDICATOR = (By.CSS_SELECTOR, "h3.profileText.name")
    USER_AVATAR = (By.CLASS_NAME, 'svgSmall')
    USER_NAME = (By.XPATH, "//h3[contains(@class, 'profileText')][text()='User.']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.spanGlobal.btnSmall")
    AD_CREATION_BUTTON = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText")
    MODAL_TITLE = (By.XPATH, "//form[@class='popUp_shell__LuyqR']//h1[@class='h1']")

class MakeNewAd:

    NAME_FIELD = (By.XPATH, "//input[@placeholder='Название' and @name='name']")
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PRICE = (By.XPATH, "//input[@placeholder='Стоимость' and @name='price']")
    OPEN_TYPE_LIST = (By.CSS_SELECTOR, ".dropDownMenu_arrowUp__I25Xq.dropDownMenu_noDefault__wSKsP")
    TECHNOLOGY_TYPE = (By.CSS_SELECTOR, ".dropDownMenu_btn__o8ARs.dropDownMenu_noDefault__wSKsP")
    PUBLICATE_BUTTON = (By.XPATH, "//button[@type='submit'][text()='Опубликовать']")
    CHOOSE_CITY = (By.XPATH, "//input[contains(@name,'city')]/../button",)
    EKATERINBURG_CITY = (By.CSS_SELECTOR, ".dropDownMenu_btn__o8ARs.dropDownMenu_noDefault__wSKsP")

class SearchForAd:

    NAME_SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='text'][placeholder='Я хочу купить...']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit'][text()='Применить']")
    SEARCH_TECHNOLOGY_TYPE = (By.CSS_SELECTOR, ".dropDownMenu_btn__o8ARs.dropDownMenu_noDefault__wSKsP")
    AD_NAME = (By.XPATH, "//h2[@class='h2'][contains(text(), 'Тестовое название')]")
    AD_PRICE = (By.XPATH, "//h2[@class='h2'][contains(text(), '₽')]")
    AD_CITY = (By.XPATH, "//h3[@class='h3'][contains(text(), 'Москва')]")
    
