from email import message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests


def send_telegram_message(message, chat_id):
    f = open('./bot_token.txt','r')
    token = f.read()
    f.close()
    
    get_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'

    result = requests.get(get_url)
    return result


def check_availability_of_cloth_size(driver, url, button_id, message):
    driver.get(url)
    size_button = driver.find_element(By.ID, button_id)
    print(size_button)
    is_size_available = False if 'size-out-of-stock' == size_button.get_attribute('data-qa-action') else True

    if is_size_available:
        send_telegram_message(f'{message}: {babaanne_url}', '-596278799')
    return send_telegram_message


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
options.add_argument('--disable-gpu')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome('./chromedriver.exe', options=options)

# TAKIM BLAZER
url = "https://www.zara.com/tr/tr/pamuklu-keten-blazer-takim-p05631150.html?v1=200488403&v2=2111004"
button_id = "product-detail-size-selector-product-detail-product-size-selector-200488403-item-0"
message = 'Blazer geldi'
check_availability_of_cloth_size(driver, url, button_id, message)

# TAKIM PANTOLON
url = "https://www.zara.com/tr/tr/pamuklu-keten-takim-pantolonu-p05638150.html?v1=200488404&v2=2111004"
button_id = "product-detail-size-selector-product-detail-product-size-selector-200488404-item-0"
message = 'Takım pantolon geldi'
check_availability_of_cloth_size(driver, url, button_id, message)

# BABAANNE TSHIRT
url = "https://www.zara.com/tr/tr/pamuklu-premium-t-shirt-p04174015.html?v1=172577525&v2=2137904"
button_id = 'product-detail-size-selector-product-detail-product-size-selector-172577525-item-3'
message = 'Babaanne tişört geldi'
check_availability_of_cloth_size(driver, url, button_id, message)

driver.quit()

send_telegram_message(f'calisiyor', '-770148157')
