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


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
options.add_argument('--disable-gpu')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome('./chromedriver.exe', options=options)
url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072402.html?v1=153423933"
driver.get(url)

driver.save_screenshot('./ozi_pantolon.png')

us30_beden = driver.find_element(By.ID, 'product-detail-size-selector-product-detail-product-size-selector-153423933-item-0')
is_available = False if 'size-out-of-stock' == us30_beden.get_attribute('data-qa-action') else True

print(is_available)

babaanne_url = "https://www.zara.com/tr/tr/pamuklu-premium-t-shirt-p04174015.html?v1=172577525&v2=2137904"
driver.get(babaanne_url)

babaanne_L = driver.find_element(By.ID, 'product-detail-size-selector-product-detail-product-size-selector-172577525-item-3')
is_babaanne_available = False if 'size-out-of-stock' == babaanne_L.get_attribute('data-qa-action') else True
print(is_babaanne_available)
driver.save_screenshot('./babaanne_tshirt.png')
driver.quit()
send_telegram_message(f'calisiyor', '-770148157')

if is_available:
    send_telegram_message(f'Pantolon Geldi HEM DE 30 BEDEN ALO: {url}', '-596278799')

if is_babaanne_available:
    send_telegram_message(f'BABAANNE T-SHIRT GELDİ: {babaanne_url}', '-596278799')
