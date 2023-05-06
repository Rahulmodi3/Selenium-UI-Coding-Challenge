import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.common.action_chains import ActionChains

SeleniumManager.driver_location('chrome')
driver = webdriver.Chrome()


class Selectors:
    dragable_box = "//div[@id='countries']//div[@class='dragableBoxRight']//div[@class='dragableBox']"
    capital_drag_box = "//div[@id='capitals']//div[@id='dropContent']"

    @staticmethod
    def get_capital_box(capital: str) -> str:
        return f"//div[@id='capitals']//div[@class='dragableBox'][contains(@id,'box')][contains(text(),'{capital}')]"

    @staticmethod
    def get_country_box(country: str) -> str:
        return f"//div[@id='countries']//div[@class='dragableBoxRight'][contains(text(),'{country}')]"

    @staticmethod
    def get_country_dragable_box(country: str) -> str:
        return Selectors.get_country_box(country) + "//div[@class='dragableBox']"


def drag_capitals(capital: str, country: str):
    action = ActionChains(driver)
    capital_box_element = driver.find_element(By.XPATH, Selectors.get_capital_box(capital))
    country_box_element = driver.find_element(By.XPATH, Selectors.get_country_box(country))
    # Drag and Drop capital to country
    action.drag_and_drop(capital_box_element, country_box_element).perform()
    # print color after drag
    colour = get_color_country_box(country)
    print(f"Equivalent color string:  {colour}")

    if colour == '#00FF00':
        print(f"Correct drag-drop Done: {capital}:{country}")
    else:
        print(f"In-Correct drag-drop Done: {capital}:{country}")


def move_capitals_back():
    print("it's time to move back all the capitals")
    action = ActionChains(driver)

    capital_box_element = driver.find_element(By.XPATH, Selectors.capital_drag_box)
    drag_boxs_elements = driver.find_elements(By.XPATH, Selectors.dragable_box)

    # Drag and Drop capital to country
    for box_element in drag_boxs_elements:
        action.drag_and_drop(box_element, capital_box_element).perform()


def get_color_country_box(country: str) -> str:
    country_box_element = driver.find_element(By.XPATH, Selectors.get_country_dragable_box(country))
    box_background_color = country_box_element.value_of_css_property('background-color')
    print(box_background_color)
    r, g, b = get_rgb_value(box_background_color)
    colour = rgb_to_hex(r, g, b)
    return colour


def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


def get_rgb_value(rgba: str):
    text_color_split = rgba.split(',')
    btn_colour_split_1st = text_color_split[0]
    r = btn_colour_split_1st.split('(')[1]
    g = text_color_split[1].strip()
    b = text_color_split[2].strip()

    return int(r), int(g), int(b)


if __name__ == '__main__':
    base_url = 'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
    driver.get(base_url)
    drag_capitals('Oslo', 'Norway')
    drag_capitals('Stockholm', 'Sweden')
    drag_capitals('Washington', 'United States')
    drag_capitals('Seoul', 'South Korea')
    drag_capitals('Rome', 'Italy')
    drag_capitals('Madrid', 'Spain')
    drag_capitals('Copenhagen', 'Denmark')

    time.sleep(3)
    move_capitals_back()
    time.sleep(3)

    # -ve use cases
    drag_capitals('Oslo', 'Sweden')
    drag_capitals('Stockholm', 'United States')
    drag_capitals('Washington', 'South Korea')
    drag_capitals('Seoul', 'Italy')
    drag_capitals('Rome', 'Spain')
    drag_capitals('Madrid', 'Denmark')
    drag_capitals('Copenhagen', 'Norway')

    time.sleep(3)
    move_capitals_back()
    time.sleep(3)

    # combination of +ve use case nad -ve uses cases
    drag_capitals('Oslo', 'Norway')
    drag_capitals('Stockholm', 'Sweden')
    drag_capitals('Washington', 'United States')
    drag_capitals('Seoul', 'Spain')
    drag_capitals('Rome', 'Italy')
    drag_capitals('Madrid', 'South Korea')
    drag_capitals('Copenhagen', 'Denmark')

    time.sleep(3)
    move_capitals_back()
    time.sleep(3)
