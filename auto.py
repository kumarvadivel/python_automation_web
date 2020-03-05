#automate ksrct digipro
#localhost pages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d= webdriver.Chrome()
d.get('http://10.1.5.12/')
d.find_element_by_xpath('//*[@id="lid"]').send_keys('1721175')
d.find_element_by_xpath('//*[@id="lpass"]').send_keys('1721177')
d.find_element_by_xpath('//*[@id="bsubmit"]').click()


