import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SeleniumManager.driver_location(browser='chrome')

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_option)


class Selector:
    get_currentWorldPopulation = '//span[@rel="current_population"]'
    get_birthsToday = '//span[@rel="births_today"]'
    get_deathsToday = '//span[@rel="dth1s_today"]'
    get_populationGrowthToday = '//span[@rel="absolute_growth"]'
    get_birthsYear = '//span[@rel="births_this_year"]'
    get_deathsYear = '//span[@rel="dth1s_this_year"]'
    get_populationGrowthYear = '//span[@rel="absolute_growth_year"]'

driver.get('https://www.worldometers.info/world-population/')

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Selector.get_currentWorldPopulation)))

start_time = time.time()

while True:

    Current_World_Population = driver.find_element(By.XPATH, Selector.get_currentWorldPopulation).text
    print('Current World Population : ', Current_World_Population)

    Births_today = driver.find_element(By.XPATH, Selector.get_birthsToday).text
    print('Births today : ', Births_today)

    Deaths_today = driver.find_element(By.XPATH, Selector.get_deathsToday).text
    print('Deaths today : ', Deaths_today)

    Population_Growth_today = driver.find_element(By.XPATH, Selector.get_populationGrowthToday).text
    print('Population Growth today : ', Population_Growth_today)

    Births_this_year = driver.find_element(By.XPATH, Selector.get_birthsYear).text
    print('Births this year : ', Births_this_year)

    Deaths_this_year = driver.find_element(By.XPATH, Selector.get_deathsYear).text
    print('Deaths this year : ', Deaths_this_year)

    Population_Growth_this_year = driver.find_element(By.XPATH, Selector.get_populationGrowthYear).text
    print('Population Growth this year : ', Population_Growth_this_year)

    end_time = time.time()
    run_time = (round(end_time - start_time))

    if run_time >= 20:
        print('before break', run_time)
        break
