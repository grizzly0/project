from selenium.common import NoSuchElementException
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TenzorSearchlocators:
    LOCATOR_Tenzor_SEARCH_BLOCK = (By.XPATH, "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and text()='Сила в людях']")
    LOCATOR_Tenzor_SEARCH_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a")
    LOCATOR_Tenzor_SEARCH_IMAGES = (By.CSS_SELECTOR, "div.tensor_ru-About__block3-image-wrapper > img")

class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.url = "https://tensor.ru/"

    def check_block(self):
        try:
            element = self.find_element(TenzorSearchlocators.LOCATOR_Tenzor_SEARCH_BLOCK)
            print(f"  Текст: {element.text}")
        except NoSuchElementException:
            print("not found")
            print(f" Текст не совпадает.  получено:")

    def click_on_the_search_buton(self):
        return self.find_element(TenzorSearchlocators.LOCATOR_Tenzor_SEARCH_BUTTON).click()


    def check_images(self):
        images = self.find_elements(TenzorSearchlocators.LOCATOR_Tenzor_SEARCH_IMAGES)

        if len(images) == 0:
            print("[ERROR] Изображения не найдены")
            return False

        print(f"Найдено изображений: {len(images)}")

        # Пробуем несколько способов получить размеры
        first_img = images[0]

        # Способ 1: Через HTML-атрибуты (ваш текущий метод)
        ref_width_html = first_img.get_attribute("width")
        ref_height_html = first_img.get_attribute("height")

        # Способ 2: Через .size (отображаемые размеры)
        ref_size_display = first_img.size  # {'width': 270, 'height': 192}

        # Выбираем метод проверки
        if ref_width_html and ref_height_html:
            # Используем HTML-атрибуты, если они есть
            try:
                ref_width = int(ref_width_html)
                ref_height = int(ref_height_html)
                print(f"Эталон (HTML-атрибуты): {ref_width} x {ref_height} px")
                check_method = "html"
            except (TypeError, ValueError):
                print("[WARNING] HTML-атрибуты некорректны, использую отображаемые размеры")
                ref_width = ref_size_display['width']
                ref_height = ref_size_display['height']
                check_method = "display"
        else:
            # Используем отображаемые размеры
            ref_width = ref_size_display['width']
            ref_height = ref_size_display['height']
            print(f"Эталон (отображаемый размер): {ref_width} x {ref_height} px")
            check_method = "display"

        # Проверяем все изображения
        all_match = True
        for i, img in enumerate(images[1:], start=2):
            try:
                if check_method == "html":
                    # Через HTML-атрибуты
                    current_width = int(img.get_attribute("width"))
                    current_height = int(img.get_attribute("height"))
                else:
                    # Через отображаемые размеры
                    current_size = img.size
                    current_width = current_size['width']
                    current_height = current_size['height']

                if current_width == ref_width and current_height == ref_height:
                    print(f"[OK] Изображение {i}: {current_width} x {current_height} px")
                else:
                    print(f"[ERROR] Изображение {i}: {current_width} x {current_height} px "
                          f"(ожидалось {ref_width} x {ref_height})")
                    all_match = False

            except (TypeError, ValueError, AttributeError) as e:
                print(f"[ERROR] Изображение {i}: не удалось получить размеры ({e})")
                all_match = False

        # Итог
        print("=" * 40)
        if all_match:
            print(f"[SUCCESS] Все {len(images)} изображений имеют одинаковый размер.")
            return True
        else:
            print("[FAIL] Найдены изображения с разными размерами.")
            return False
