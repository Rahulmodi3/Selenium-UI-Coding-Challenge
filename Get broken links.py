import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
import requests
import multiprocessing as mp


def check_broken_links(link_url):
    try:
        url_status_code = requests.head(link_url).status_code
        if url_status_code >= 400:
            print(f"{link_url} : is status code is {url_status_code}")
    except requests.exceptions.MissingSchema:
        print(f"Encountered MissingSchema Exception in url : {link_url}")
    except requests.exceptions.InvalidSchema:  # mail or phone in link it will skip
        print(f"Encountered InvalidSchema Exception in url : {link_url}")
    except:
        print(f"Encountered Some other execution{link_url}")


if __name__ == '__main__':
    SeleniumManager.driver_location(browser='chrome')
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--incognito')
    chrome_option.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_option)

    driver.get('https://www.amazon.in/')
    get_all_links = driver.find_elements(By.TAG_NAME, 'a')
    print('Total Links : ', len(get_all_links))
    # get the start time
    st = time.time()
    # get active link from the all links
    active_links = [link.get_attribute('href') for link in get_all_links
                    if link.get_attribute('href') != None]

    print('Active links list : ', active_links)

    ''' ------------------  Run parallel using multiprocessing ------------------ '''
    pool = mp.Pool()
    result_objects = pool.map(check_broken_links, active_links)
    # get the end time
    et = time.time()
    # get the execution time
    elapsed_time = et - st
    print('Execution time:', round(elapsed_time, 3), 'seconds')

    driver.close()
