from email import message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests


def send_telegram_message(message, chat_id):
    f = open('../bot_token.txt', 'r')
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
        send_telegram_message(f'{message}: {url}', '-596278799')
    return send_telegram_message


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome('../chromedriver.exe', options=options)
# driver.save_screenshot('./babaanne_tshirt.png')

# PREMIUM SLIM FIT JEAN DONUK MAVI
url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=177662109"
button_id = "product-size-selector-177662109-item-3"
message = 'DONUK MAVI KOT GELDI US34 BEDEN'
check_availability_of_cloth_size(driver, url, button_id, message)

# PREMIUM SLIM FIT JEAN SIYAH
url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=177662108"
button_id = "product-size-selector-177662108-item-3"
message = 'SIYAH KOT GELDI US34 BEDEN'
check_availability_of_cloth_size(driver, url, button_id, message)

# PREMIUM SLIM FIT JEAN KOT MAVISI
url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=177662111"
button_id = "product-size-selector-177662111-item-3"
message = 'KOT MAVISI GELDİ US34 BEDEN'
check_availability_of_cloth_size(driver, url, button_id, message)

# PREMIUM SLIM FIT JEAN KOT MAVISI 2
url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=1776621123"
button_id = "product-size-selector-223692184-item-3"
message = 'KOT MAVISI 2 GELDİ US34 BEDEN'
check_availability_of_cloth_size(driver, url, button_id, message)

# BABAANNE SISME MONT
url = "https://www.zara.com/tr/tr/kapusonlu-sisme-mont-p00518240.html?v1=177653360"
button_id = "product-size-selector-177653360-item-3"
message = 'BABAANNE MONT GELDI'
check_availability_of_cloth_size(driver, url, button_id, message)

####################################################################################
driver.quit()

send_telegram_message(f'calisiyor', '-770148157')
