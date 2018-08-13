# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome('C://chromedriver', chrome_options=options)


def get_video_post_details(video_post):
	driver.get(video_post)
	# views = driver.find_element_by_xpath('//span[@class="fcg"]').text.split()[0].replace('K', '000')
	# likes = driver.find_element_by_xpath('//span[contains(text(),"Likes")]').text.split()[0]
	# comments = driver.find_element_by_xpath('//span[contains(text(),"Comments")]').text.split()[0]
	views = driver.find_element_by_xpath('//span[@class="fcg"]').text.split(':')[-1].replace(' тыс.', '000').replace(' mil', '000').replace('K', '000').replace(' B', '000').strip()
	likes = driver.find_elements_by_xpath('//span[@class="_2u_j"]')[0].text.split(':')[-1].split()[0]
	comments = driver.find_elements_by_xpath('//span[@class="_2u_j"]')[1].text.split(':')[-1].split()[0]
	return [views, likes, comments]


details = get_video_post_details('https://www.facebook.com/JungleVT/videos/1720510198003354/')
print(details)
driver.close()