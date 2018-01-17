from bs4 import BeautifulSoup
import random
import requests
import csv
import os
import time

#keeps track of how long the script runs
starttime=time.time()

#the datacollection is set for two minutes i.e 120 seconds, but can easily be modified by changing the time of the while loop
while time.time()-starttime<=500:

	#list of user agents as a precaution to avaoid getting banned for scraping
	userAgents = [
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13',
	'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
	];		
	
	#picks a random user agent every time we start this script		
	headers={		
	'User-Agent' : random.choice(userAgents)		
	}		
	
	#the site that we are scraping		
	url="https://coinmarketcap.com/currencies/eos/#markets/"		
	
	#checks to see if we have correctly extracted the html
	try:		
	#sending an http request to site to obtain its HTML

		r=requests.get(url, headers=headers,timeout=5)

	#throws an exception if status code error e.g 404 error
		r.raise_for_status()		
	except requests.exceptions.HTTPError as e:
		print e
		exit(1)		
	except Exception:
		print ('Could not extract HTML successfully')		
	
	else:		
		
	    #extracts page HTML		
		soup=BeautifulSoup(r.content,'html.parser',from_encoding="UTF-8")
		#contains the HTML that contains all the price information
	    
		price_info_container=soup.find("div",{'class':"col-xs-6 col-sm-8 col-md-4 text-left"})
	    #contains HTML that cotains the Volume(24h) info		
		volume_container=soup.findAll("div", {'class':'coin-summary-item-detail details-text-medium'})
		#trade volume of EOS in USD		
		volUSD=float(volume_container[1].span['data-usd'])

	    #price of EOS in USD		
		USD=float(price_info_container.find('span',{'class':'text-large2'}).text)
		#function that finds the price in ETH and converts it to float
		def ETHprice():
			crypto_prices=soup.findAll("span",{'class':"text-gray details-text-medium"})
			for price in crypto_prices:
				if ('ETH' in price.text):
					ETHprice=price.text.replace(" ETH",'')
					return float(ETHprice)
			return 'no price in ETH'

	    #function that finds Etherum vol and converts it to a float				
		def ETHvol():
			cryptoVol=volume_container[1].findAll('span',{'class':'text-gray'})
			ETHvol=cryptoVol[1].text.replace(" ETH",'')
			ETHvol=ETHvol.replace(',','')
			return float(ETHvol)		

	 	#the datafields for our CSV   
	 	fieldnames=['USD','Vol(USD)','ETH','Vol(ETH)','Time']

	 	#if file is not already created, script will create a new csv and will write the datafields on the top row
	 	if (os.path.isfile('EOS.csv')==False):

	 		csv_file=open('EOS.csv','w+')
	 		csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames,lineterminator='\n')
	 		csv_writer.writeheader()
	 		csv_writer.writerow({			
	 			'USD':USD,
	 			'Vol(USD)': volUSD,
	 			'ETH':ETHprice(),
	 			'Vol(ETH)':ETHvol(),
	 			'Time': time.time()-starttime		
	 			}
	 		)


	 	else:			
	 		
	 		csv_file=open('EOS.csv','a')
	 		csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames,lineterminator='\n')
	 		csv_writer.writerow({			
	 			'USD':USD,
	 			'Vol(USD)': volUSD,
	 			'ETH':ETHprice(),
	 			'Vol(ETH)':ETHvol(),
	 			'Time': time.time()-starttime

	 			}
	 		)



	 	csv_file.close()


