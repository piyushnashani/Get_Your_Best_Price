import string

from selenium import webdriver

Name_of_Product = ""
Currency = 'Rupees'
min_price = ''
max_price = ''
filters = {
    'min': min_price, 'max': max_price
}
headers = {'User-Agent': '' }
Base_URL = "https://www.amazon.in/"


def get_chrome_webdriver(options):
    return webdriver.Chrome('./chromedriver', chrome_options=options)


def get_webdriver_options():
    return webdriver.ChromeOptions()


def ignore_certificate_errors(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_icognito(options):
    options.add_argument('--icognito')


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", [ "enable-automation" ])
options.add_experimental_option('useAutomationExtension', False)
