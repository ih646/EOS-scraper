import mechanize
import random
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import re
import sys
import csv
import requests
import matplotlib.pyplot as plt
import numpy as np

browser = webdriver.Firefox( executable_path='geckodriver.exe')
browser.implicitly_wait(30)

#retreiving the url we want to scrape
browser.get('https://www.worldcoinindex.com/account/login')
time.sleep(5)

Email=browser.find_element_by_name("Email").clear()
Email=browser.find_element_by_name("Email")

password = browser.find_element_by_name('Password').clear()
password = browser.find_element_by_name("Password")

Email.send_keys('bhubon047@gmail.com')
password.send_keys('mvemjsunp123A@'+Keys.RETURN)
time.sleep(3)

browser.get('https://www.worldcoinindex.com/coin/eos')
(browser.page_source).encode('ascii', 'ignore')

dropdown=browser.find_element_by_id('dd')
item=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/nav/div[2]/div[3]/section/div/div/ul/li[2]/a')
ETH=ActionChains(browser).move_to_element(dropdown).click(item)
ETH.perform()

time.sleep(5)

browser2=webdriver.Firefox(executable_path='geckodriver.exe')
browser2.implicitly_wait(30)
browser2.get("https://eosscan.io/")

def ETHprice():
	WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[3]/div[1]/div[1]/table/tbody/tr/td[4]")))
	coin_price=browser.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[1]/table/tbody/tr/td[4]")
	price=coin_price.text.encode('utf-8')
	price=price.replace(price[0:2],"")
	price=float(price)
	return price

def vol():

	WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="market-table"]/tbody/tr/td[8]/a')))
	Vol=browser.find_element_by_xpath('//*[@id="market-table"]/tbody/tr/td[8]/a')
	Vol_ETH=Vol.text.encode('utf-8')
	Vol_ETH=Vol_ETH.replace(Vol_ETH[0:2],'')
	Vol_ETH=Vol_ETH.replace(',','')
	Vol_ETH=float(Vol_ETH)
	return Vol_ETH

fieldnames=['ETHprice', 'Vol(ETH)','marketprice','Time']
				
def marketPrice():
	#checks to see if we have correctly extracted the html
	browser2.refresh()
	time.sleep(3)
	WebDriverWait(browser2,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/section[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/p[3]/strong')))
	marketprice=browser2.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/p[3]/strong')

	try:		
		marketprice=marketprice.text
		
	except Exception:
		print ('Could not extract HTML successfully')		
	
	else:	
		return float(marketprice)
		
starttime=time.time()
print starttime


while time.time()-starttime<120:
	if (os.path.isfile('EOS_realtime.csv')==False):

		print 'hello'
		csv_file=open('EOS_realtime.csv','w+')
		csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames,lineterminator='\n')
		csv_writer.writeheader()
		csv_writer.writerow({			
			'ETHprice':ETHprice(),
			'Vol(ETH)':vol(),
			'marketprice':marketPrice(),
			'Time': time.time()-starttime
			}
		)
		time.sleep(5)

	else:			
		 		
		csv_file=open('EOS_realtime.csv','a')
		csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames,lineterminator='\n')
		csv_writer.writerow({			
			'ETHprice':ETHprice(),
			'Vol(ETH)':vol(),
			'marketprice':marketPrice(),
			'Time': time.time()-starttime	

			}
		)
		time.sleep(5)



csv_file.close()

browser.close()
browser2.close()

