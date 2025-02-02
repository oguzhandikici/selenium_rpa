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


def check_availability_of_cloth_size(driver: webdriver.Chrome, url: str, size_indexes: set, message: str, done_indexes: set):
    """
    :param url: Kıyafet URL'i.
    :param size_indexes: En küçük beden 0 olacak şekilde, 1'er artışlarla bakılacak bedenlerin indexleri.
    :param message: Kıyafetin bulunması durumunda telegram'dan gönderilecek mesaj.
    :param done_indexes: Başlangıçta boş bir set() verilir. Bu fonksiyonun return değeri ile bulunan bedenler ile içi doldurularak tekrar aynı bedene bakılmaz.
    """
    driver.get(url)
    ul_elements = driver.find_element(By.CLASS_NAME, "size-selector-sizes--grid-gap")
    li_elements = ul_elements.find_elements(By.TAG_NAME, "li")

    for index in size_indexes:
        time.sleep(0.5)

        if index not in done_indexes:
            li_element = li_elements[index]
            class_attribute = li_element.get_attribute("class")

            if "size-selector-sizes-size--unavailable" not in class_attribute:
                send_telegram_message(f'{message}: {url}', '-596278799')
                done_indexes.add(index)
            else:
                # send_telegram_message('deneme', '-596278799')
                print(message, index, 'için beden yok')
    return done_indexes


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=options)
# driver.save_screenshot('ss.png')


clothes = [
    {'url': 'https://www.zara.com/tr/tr/soluk-efektli-ve-kapusonlu-sweatshirt-p08417454.html?v1=412379690', 'message': 'BABAANNE KREM SWEAT', 'indexes': {3}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/soluk-efektli-ve-kapusonlu-sweatshirt-p08417454.html?v1=412379689', 'message': 'BABAANNE KAHVE SWEAT', 'indexes': {3}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/duz-penye-pantolon-p03199634.html?v1=387282868&v2=2141374', 'message': 'BABAANNE KREM EŞOFMAN ALT', 'indexes': {4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/cep-detayli-kapusonlu-sweatshirt-p03199633.html?v1=387282869', 'message': 'BABAANNE KREM EŞOFMAN ÜST', 'indexes': {4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/straight-fit-jean-p03991317.html?v1=391334067', 'message': 'GRI STRAIGHT FIT JEAN', 'indexes': {1, 4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/straight-fit-jean-p08062400.html?v1=364092436', 'message': 'AÇIK MAVI STRAIGHT FIT JEAN', 'indexes': {0, 1, 4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/duz-renk-regular-fit-jean-p03991350.html?v1=395959533', 'message': 'DÜZ RENK REGULAR FIT JEAN', 'indexes': {1, 4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/slim-fit-jean-p00621303.html?v1=393041905', 'message': 'ORIGINS SLIM FIT JEAN SIYAH', 'indexes': {0}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/relaxed-straight-fit-jean-p03991380.html', 'message': 'MAVI RELAXED STRAIGHT FIT JEAN', 'indexes': {0, 4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/relaxed-straight-fit-jean-p03991380.html?v1=387299545', 'message': 'KÖMÜR RELAXED STRAIGHT FIT JEAN', 'indexes': {1, 4}, 'done_indexes': set()},
    {'url': 'https://www.zara.com/tr/tr/dokumlu-regular-fit-gomlek-p07545316.html?v1=388518009', 'message': 'MODAL GÖMLEK SİYAH', 'indexes': {0}, 'done_indexes': set()},
]

done_count = 0
while done_count < len(clothes):
    for i, cloth in enumerate(clothes):
        if cloth['done_indexes'] != cloth['indexes']:
            done_indexes = check_availability_of_cloth_size(driver, **cloth)
            if done_indexes != cloth['done_indexes']:
                clothes[i]['done_indexes'] = done_indexes

            if clothes[i]['done_indexes'] == clothes[i]['indexes']:
                done_count += 1

    random_time = random.randint(50, 70)
    print(random_time, 'saniye sonra tekrar denenecek')
    time.sleep(random_time)


# send_telegram_message(f'calisiyor', '-770148157')

####################################################################################
driver.quit()

