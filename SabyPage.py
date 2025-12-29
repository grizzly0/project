from selenium.common import NoSuchElementException
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from TenzorPage import TensorPage



class SabySearchlocators:
    LOCATOR_SABY_SEARCH_BUTTON1 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]/span")
    LOCATOR_SABY_SEARCH_BUTTON2 = (By.CSS_SELECTOR, "a.sbisru-link.sbis_ru-link")
    LOCATOR_SABY_SEARCH_BUTTON3 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a")
    #свой регион вставить ниже. пример text() = "Республика Башкортостан"
    LOCATOR_SABY_SEARCH_MYREGION = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link' and text()='Нижегородская обл.']")
    LOCATOR_SABY_SEARCH_PARTNERS = (By.XPATH,  "//div[@class='controls-ListView__itemV-relative controls-ListView__itemV controls-ListView__item_default controls-ListView__item_contentWrapper js-controls-ListView__editingTarget  controls-ListView__itemV_cursor-pointer  controls-ListView__item_showActions js-controls-ListView__measurableContainer controls-ListView__item__unmarked_default controls-ListView__item_highlightOnHover controls-hover-background-default controls-Tree__item']")
    LOCATOR_SABY_SEARCH_REGION = (By.XPATH,"//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']")
    LOCATOR_SABY_SEARCH_CHANGEREGION = (By.CSS_SELECTOR, "div.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l > div > ul > li:nth-child(43)")
    LOCATOR_TITLE_KAMCHATKA = (By.XPATH, "//title[contains(text(), 'Камчатский край')]")
    LOCATOR_SABY_SEARCH_KAMCHATKA = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link' and text()='Камчатский край']")
    LOCATOR_SABY_KAMCHATKA_PARTNER = (By.XPATH, "//div[@title='Saby - Камчатка' and contains(@class, 'sbisru-Contacts-List__name')]")

class SearchHelper(BasePage):
    def mouse_hover(self):
        tutorial = self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_BUTTON1)
        return self.move_element(tutorial)

    def click_on_the_search_button(self):
        return self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_BUTTON2).click()

    def go_to_tenzor(self):
        link = self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_BUTTON3)
        self.browser.execute_script("arguments[0].removeAttribute('target')", link)
        link.click()
        return TensorPage(self.browser)

    def check_region(self):
        try:
            element = self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_MYREGION)
            print(f"  Текст: {element.text}")
        except NoSuchElementException:
            print("not found")
            print(f" Текст не совпадает.  получено:")

    def check_partners_list(self):
        try:
            return self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_PARTNERS)
        except NoSuchElementException:
            print("not found")

    def change_region(self):
        self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_REGION).click()
        self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_CHANGEREGION).click()
    def check_kamchatka(self):
        try:
            self.find_element(SabySearchlocators.LOCATOR_SABY_SEARCH_KAMCHATKA)
            self.find_element(SabySearchlocators.LOCATOR_SABY_KAMCHATKA_PARTNER)
            self.find_element(SabySearchlocators.LOCATOR_TITLE_KAMCHATKA)

            """Проверка URL Камчатского края"""

            current_url = self.browser.current_url
            print(f"Текущий URL: {current_url}")

            # Ожидаемый URL (может быть несколько вариантов)
            expected_patterns = [
                "https://saby.ru/contacts/41-kamchatskij-kraj",
                "https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients",
                "https://saby.ru/contacts/41-kamchatskij-kraj?",
                "kamchatskij-kraj",  # Часть URL
                "/41-kamchatskij-kraj"  # Путь
            ]

            # Проверяем все варианты
            url_matches = []
            for pattern in expected_patterns:
                if pattern in current_url:
                    url_matches.append(pattern)
                    break

            if url_matches:
                print(f"✓ URL содержит Камчатский край: {url_matches[0]}")
                return True
            else:
                print(f"✗ URL НЕ содержит Камчатский край")
                print(f"  Ожидалось что-то из: {expected_patterns[:3]}")
                print(f"  Получено: {current_url}")
                return False


        except NoSuchElementException:
            print("not found")
