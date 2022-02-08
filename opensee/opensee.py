from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
import logging
from time import sleep


def get_total_items(driver, url):
    driver.get(url)
    try:
        totalforitem = driver.find_elements(By.CLASS_NAME, "CollectionStatsBar--info")[0].get_attribute("innerText").split("items")[0].strip()
    except:
        return url, "0"
    return url, totalforitem


def main():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--user-data-dir=/Applications/Google Chrome.app/User Data")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')
    # options.binary_location = "/Applications/Google Chrome Canary.app"
    chromedriver = ChromeDriverManager(chrome_type=ChromeType.GOOGLE, log_level=logging.INFO, print_first_line=False).install()
    s = Service('/Users/jc/chromedriverreal')
    driver = webdriver.Chrome(chromedriver, options=options, service=s, service_log_path=None)
    # driver = webdriver.Chrome('/Users/jc/chromedriver')
    driver.get("https://opensea.io/rankings")
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # height = driver.execute_script("return document.body.scrollHeight")
    # j = 0
    # for i in range(height):
    #     driver.execute_script('window.scrollBy(0,10)')  # scroll by 20 on each iteration
    #     height = height + 10
    #     # sleep(0.1)
    #     j = j + 1
    #     if j == 600:
    #         break
    height = driver.execute_script("return document.body.scrollHeight")
    action = webdriver.ActionChains(driver)
    action.move_by_offset(10, 20)
    figuredit = set()
    for scrol in range(200, height, 200):
        # try:
        driver.execute_script(f"window.scrollTo(0,{scrol})")
        # except:
        #    continue
        sleep(0.01)
        stuff = driver.find_elements(By.XPATH, "//a[@href]")
        for item in stuff:
            # if item.starts_with("")
            # if "collection" in item.get_attribute('href'):
            print(item.get_attribute('href'))
            figuredit.add(item.get_attribute('href'))
        # action.move_by_offset(10, 20)
    action.move_by_offset(10, 20)
    # sleep(10)
    stuff = []
    action.move_to_element(driver.find_element(By.CLASS_NAME, "fTomoL"))
    # stuff = driver.find_elements(By.XPATH, "//a[@href]")
    # stuff = driver.find_elements(By.CLASS_NAME, "Overflowreact__OverflowContainer-sc-7qr9y8-0")
    # stuff = driver.find_elements(By.CLASS_NAME, "Overflowreact__OverflowContainer-sc-7qr9y8-0")
    # Textreact__Text-sc-1w94ul3-0
    # stuff = driver.find_elements(By.CLASS_NAME, "Blockreact__Block-sc-1xf18x6-0")
    print(f"total found this page: {len(figuredit)}")
    # for item in stuff:
    #    print(item.get_attribute("innerText"))
    # driver.find_element(By.CLASS_NAME, "fTomoL").click()
    totalitems = dict()
    for link in figuredit:
        if "collection" in link:
            url, totalitem = get_total_items(driver, link)
            totalitems[url] = totalitem
        else:
            continue
    for k, v in totalitems.items():
        print(f"{k}:{v}")
    print(driver.title)


if __name__ == "__main__":
    main()