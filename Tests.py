from SabyPage import SearchHelper
from TenzorPage import TensorPage
import time

def test_Saby_Tenzor_search(driver):
    main_page = SearchHelper(driver)
    main_page.go_to_site()
    main_page.mouse_hover()
    time.sleep(3)
    main_page.click_on_the_search_button()
    main_page.go_to_tenzor()
    main_page = TensorPage(driver)
    main_page.go_to_site()
    main_page.check_block()
    main_page.click_on_the_search_buton()
    main_page.check_images()
    time.sleep(10)

def test_region(driver):
    main_page = SearchHelper(driver)
    main_page.go_to_site()
    main_page.go_to_site()
    main_page.mouse_hover()
    time.sleep(3)
    main_page.click_on_the_search_button()
    #свой регион вставить ниже
    main_page.check_region()
    main_page.check_partners_list()
    main_page.change_region()
    time.sleep(3)
    main_page.check_kamchatka()
    time.sleep(10)