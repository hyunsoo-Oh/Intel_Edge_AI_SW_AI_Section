from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from setuptools.package_index import user_agent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchDriverException
import pandas as pd
import re
import time
import datetime

def scroll_page(scroll_target=None, wait_time=2):
    if scroll_target:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_target)
    else:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(wait_time)


def scroll_to_bottom(scroll_target_xpath=None, times=0, wait_time=2):
    if scroll_target_xpath:
        try:
            scroll_target = driver.find_element(By.XPATH, scroll_target_xpath)
        except NoSuchElementException as e:
            print(f"Could not find scroll : {e}")
            return
    else:
        scroll_target = None  # document.body 대상

    if times == 0:
        command = "return arguments[0].scrollHeight" if scroll_target else "return document.body.scrollHeight"
        last_height = driver.execute_script(command, scroll_target)
        while True:
            scroll_page(scroll_target, wait_time=wait_time)
            new_height = driver.execute_script(command, scroll_target)
            if new_height == last_height:
                break
            last_height = new_height
    else:
        for i in range(times):
            scroll_page(wait_time)

options = ChromeOptions()
user_agent = ''
options.add_argument(f'user-agent={user_agent}')
options.add_argument('lang=ko_KR')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

button_movie_xpath = '//*[@id="contents"]/section/div[3]/div/section/div/div/div[2]/button'
button_drama_xpath = '//*[@id="contents"]/section/div[3]/div/section/div/div/div[3]/button'
button_anime_xpath = '//*[@id="contents"]/section/div[3]/div/section/div/div/div[4]/button'

check_xpath = f'//*[@id="contents"]/section/div[4]/div/div[2]/div/div[{4}]/button'

start_url = 'https://m.kinolights.com/discover/explore'
driver.get(start_url)
time.sleep(0.5)

button_movie = driver.find_element(By.XPATH, button_movie_xpath)
driver.execute_script("arguments[0].click();", button_movie)
time.sleep(0.5)

check_comedy = driver.find_element(By.XPATH, check_xpath)
driver.execute_script("arguments[0].click();", check_comedy)
time.sleep(0.5)

# for i in range(50):
#     driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
#     time.sleep(0.2)
scroll_to_bottom(times=10)

a_tag_xpath = '/html/body/div/div/div/main/div/div[2]/a[1]'
title_xpath = '/html/body/div/div/div/main/div/div[2]/a[1]/div/div[2]/span'

hrefs = []
titles = []

for i in range(1, 5):
    href = driver.find_element(By.XPATH,
            f'/html/body/div/div/div/main/div/div[2]/a[{i}]').get_attribute('href')
    hrefs.append(href)
    title = driver.find_element(By.XPATH,
            f'/html/body/div/div/div/main/div/div[2]/a[{i}]/div/div[2]/span').text
    titles.append(title)

print(hrefs)
print(titles)

reviews = []

for idx, url in enumerate(hrefs):
    driver.get(url + '?tab=review')
    time.sleep(0.5)
    review = ''

    scroll_to_bottom(scroll_target_xpath='//*[@id="content__body"]', times=5)
    # for _ in range(50):
    #     scroll_target_xpath = '//*[@id="content__body"]'
    #     scroll_target = driver.find_element(By.XPATH, scroll_target_xpath)
    #     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_target)
    #     height = driver.execute_script("return arguments[0].scrollHeight", scroll_target)
    #     time.sleep(0.2)

    for i in range(1, 10):
        try:
            review_xpath = f'//*[@id="contents"]/div[4]/section[2]/div/article[{i}]/div[3]/a[1]'
            review_button = driver.find_element(By.XPATH, review_xpath)
            driver.execute_script('arguments[0].click();', review_button)
            time.sleep(0.5)
            try:
                review = review + driver.find_element(By.XPATH,
                        '//*[@id="contents"]/div[2]/div[1]/div/section[2]/div/div/div/p').text
            except:
                review = review + driver.find_element(By.XPATH,
                        '//*[@id="contents"]/div[2]/div[1]/div/section[2]/div/div/h3').text
            driver.back()
            print(i, 'try')
            time.sleep(0.5)

        except:
            try:
                review = review + driver.find_element(By.XPATH,
                        f'//*[@id="contents"]/div[4]/section[2]/div/article[{i}]/div[3]/a/h5').text
            except:
                review = review
            print(i, 'except')
    reviews.append(review)

print(reviews)

pf = pd.DataFrame({'titles':titles, 'review':reviews})

pf.to_csv('./data/movie_JKY.csv', index=False)