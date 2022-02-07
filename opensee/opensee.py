from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
import logging
from time import sleep
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
driver.get("https://opensea.io/rankings?sortBy=total_volume")
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
for scrol in range(10, height, 10):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    # sleep(0.001)
    action.move_by_offset(10, 20)
action.move_by_offset(10, 20)
# sleep(10)
stuff = []
action.move_to_element(driver.find_element(By.CLASS_NAME, "fTomoL"))
stuff = driver.find_elements(By.XPATH, "//a[@href]")
print(len(stuff))
for item in stuff:
    print(item.get_attribute("href"))
driver.find_element(By.CLASS_NAME, "fTomoL").click()
print(driver.title)
