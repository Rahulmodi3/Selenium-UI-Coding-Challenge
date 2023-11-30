from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_option = webdriver.ChromeOptions()
chrome_option.set_capability("browserName", "chrome")
chrome_option.add_argument('--incognito')
SeleniumManager().driver_location(chrome_option)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://www.t-mobile.com/tablets")


class Selectors:
    CHECKBOX_FILTER = "label[@class='mat-checkbox-layout']"

    @staticmethod
    def get_checkbox(filter_name, checkbox_label_name):
        return (By.XPATH, f"//div[@aria-label='{filter_name}']//span[contains(text(),'{checkbox_label_name}')]//ancestor::{Selectors.CHECKBOX_FILTER}")

    @staticmethod
    def get_filter(filter_name):
        return (By.XPATH, f"//legend[@data-testid='desktop-filter-group-name'][contains(text(),'{filter_name}')]")

    @staticmethod
    def get_filter_checkbox(filter_name: str):
        return (By.XPATH, f"//div[@aria-label='{filter_name}']//{Selectors.CHECKBOX_FILTER}")


def select_filter(filter_name, *filter_checkbox_name):

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Selectors.get_filter(filter_name)))
    driver.find_element(*Selectors.get_filter(filter_name)).click()

    for checkbox in filter_checkbox_name:

        if checkbox == "All":
            selector = Selectors.get_filter_checkbox(filter_name)
            elements = driver.find_elements(*selector)
            for ele in elements:
                ele.click()
        else:
            selector = Selectors.get_checkbox(filter_name, checkbox)
            driver.find_element(*selector).click()


#select_filter("Deals", "New", "Special offer")
select_filter("Brands", "All")