import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests


def send_telegram_message(message, chat_id):
    f = open('./bot_token.txt', 'r')
    token = f.read()
    f.close()
    
    get_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'

    result = requests.get(get_url)
    return result


def check_price(driver, url, price_span_xpath, normal_price):
    driver.get(url)
    time.sleep(2)

    cookie_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    cookie_button.click()

    time.sleep(1)

    span_price = driver.find_element(By.XPATH, price_span_xpath)
    price = span_price.text

    if price != normal_price:
        send_telegram_message(f'ÜRÜNÜN FİYATI DEĞİŞTİ: {price}: {url}', '-904442434')
    # else:
    #     send_telegram_message(f'ÜRÜNÜN FİYATI AYNI: {price}: {url}', '-904442434')

    return send_telegram_message


options = Options()
options.add_argument("--window-size=1920,1080")
# options.add_argument('--headless=new')
options.add_argument('--incognito')
options.add_argument('--disable-gpu')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome('chromedriver.exe', options=options)

url = "https://www.massimodutti.com/tr/kapusonlu-uzun-parka-l06727620?colorId=526"
price_span_xpath = "/html/body/app-root/layout-default/div[2]/product-layout/product-page-layout/div/div/div[2]/product-page-product-details/div/div[1]/div[2]/product-prices/div/formatted-price/div/div/span"
normal_price = "3.499,00 TL"

check_price(driver, url, price_span_xpath, normal_price)

####################################################################################

driver.quit()
