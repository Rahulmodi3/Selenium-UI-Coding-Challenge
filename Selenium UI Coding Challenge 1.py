import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selector:

    states = "//*[name()='svg']//*[local-name()='g']//*[local-name()='path']"
    frame = ".//*[contains(@id,'map-instance')]"
    inside_state = "//*[name()='svg']//*[local-name()='g']//*[local-name()='path' and @class='child flash']"
    header_state_name = "//ul[@class='breadcrumb']//span"


SeleniumManager.driver_location(browser='chrome')

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_option)

base_url = 'https://petdiseasealerts.org/forecast-map'

driver.get(base_url)
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,Selector.frame))  # switch to frame
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.XPATH, Selector.states)))

all_states = driver.find_elements(By.XPATH, Selector.states)
print(f"Total States {len(all_states)}")


def click_state(state):
    for i in all_states:
        state_name = i.get_attribute('name')
        print(state_name)
        if state_name == state:
            action = ActionChains(driver)
            wait.until(EC.element_to_be_clickable(i))
            action.move_to_element(i).perform()
            i.click()
            """verify state name"""
            verify_state(state)
            break


def verify_state(state_name):
    wait.until(EC.visibility_of_element_located((By.XPATH, Selector.inside_state)))
    get_state_name = driver.find_element(By.XPATH, Selector.header_state_name).text
    assert get_state_name == state_name.upper(), f"actual state :{get_state_name} and expected is :{state_name}"


click_state('California')

# California
# Florida
# New York
# Maryland




