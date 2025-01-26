import random
import time
from email import message
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


def check_availability_of_cloth_size(driver, url, indexes, message):
    """
    :param indexes: En küçük beden 0 olacak şekilde, 1'er artışlarla bakılacak bedenlerin indexleri.
    """
    driver.get(url)
    ul_elements = driver.find_element(By.CLASS_NAME, "size-selector-sizes--grid-gap")
    li_elements = ul_elements.find_elements(By.TAG_NAME, "li")

    for index in indexes:
        if index < len(li_elements):
            li_element = li_elements[index]
            class_attribute = li_element.get_attribute("class")

            if "size-selector-sizes-size--unavailable" not in class_attribute:
                send_telegram_message(f'{message}: {url}', '-596278799')
            else:
                # send_telegram_message('deneme', '-596278799')
                print(message, 'için beden yok')


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=options)
# driver.save_screenshot('ss.png')

while True:
    url = "https://www.zara.com/tr/tr/soluk-efektli-ve-kapusonlu-sweatshirt-p08417454.html?v1=412379690"
    check_availability_of_cloth_size(driver, url, [2, 3], 'BABAANNE KREM SWEAT')


    url = "https://www.zara.com/tr/tr/soluk-efektli-ve-kapusonlu-sweatshirt-p08417454.html?v1=412379689"
    check_availability_of_cloth_size(driver, url, [2, 3], "BABAANNE KAHVE SWEAT")

    random_time = random.randint(50, 70)
    print(random_time, 'saniye sonra tekrar denenecek')
    time.sleep(random_time)


# send_telegram_message(f'calisiyor', '-770148157')


# # PREMIUM SLIM FIT JEAN SIYAH
# url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=177662108"
# button_id = "product-size-selector-177662108-item-3"
# message = 'SIYAH KOT GELDI US34 BEDEN'
# check_availability_of_cloth_size(driver, url, button_id, message)
#
# # PREMIUM SLIM FIT JEAN KOT MAVISI
# url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=177662111"
# button_id = "product-size-selector-177662111-item-3"
# message = 'KOT MAVISI GELDİ US34 BEDEN'
# check_availability_of_cloth_size(driver, url, button_id, message)
#
# # PREMIUM SLIM FIT JEAN KOT MAVISI 2
# url = "https://www.zara.com/tr/tr/premium-slim-fit-jean-p05072300.html?v1=1776621123"
# button_id = "product-size-selector-223692184-item-3"
# message = 'KOT MAVISI 2 GELDİ US34 BEDEN'
# check_availability_of_cloth_size(driver, url, button_id, message)
#
# # BABAANNE SISME MONT
# url = "https://www.zara.com/tr/tr/kapusonlu-sisme-mont-p00518240.html?v1=177653360"
# button_id = "product-size-selector-177653360-item-3"
# message = 'BABAANNE MONT GELDI'
# check_availability_of_cloth_size(driver, url, button_id, message)

####################################################################################
driver.quit()

