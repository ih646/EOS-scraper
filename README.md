# Description

This is a EOS web scraper that I made using python to gather data on the crypto currency EOS. It includes two scrapers- one static and one realtime. The realtime scraper uses Selenium webdriver to gather information from the website *worldcoinindex* and the static scraper uses beautifulsoup to gather data from *coinmarketcap*.

#Instuctions

Once you've cloned the repository into your local machine you will need to install geckodriver.exe, beautifulsoup and selenium to make the code run.This can be done easily by using the command line to go to the directory where the files are located and typing.

`pip install -U selenium`

and then

`pip install beautifulsoup4`

geckodriver can de downloaded from the internet and installed inside the folder with the relevant files. The code can then be run from the command line as usual.

Note - The static scraper was just an experiment for me to learn beautifulsoup and was not meant to be used for any practical data collection; it only works if it is run for a very long time. This why the EOSplot.py only plots the data from the realtime scraper. The CSV files I've included in my repo is just an example of what the format of the CSV looks like. Therefore, the already existant CSV files should be deleted before running the program for fresh data collection.
