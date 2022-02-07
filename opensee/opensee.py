from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import logging
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
driver.get("https://opensea.io")
print(driver.title)
