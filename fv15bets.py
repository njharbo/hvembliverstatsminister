# -*- coding: utf-8 -*- 
# Load libs.
from __future__ import unicode_literals
from __future__ import division
# Load tools for image processing
from PIL import Image
import pyscreenshot as ImageGrab
# Load tools for OCR functionality
import pytesseract
# Load tools for WebDriver functionality
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#Load tool for timing
import time 
#Load tool for saving to CSV
import csv
#Numpy 
import numpy as np

#plotting
import matplotlib.pyplot as plt
from pylab import *

#Define variables
count=1
#betfair
betfairlink="https://www.betfair.com/exchange/plus/#/politics/market/1.117367358"
befairLLR=(828,576,926,621)
befairHTS=(828,672,926,717)
betfairzoom=9
betfairscroll="window.scrollTo(0.25*document.body.scrollWidth, 0.2*document.body.scrollHeight);"
#danskespil
danskespillink="https://danskespil.dk/oddset/politik/danmark/folketingsvalg-2015"
danskespilLLR=(520,491,563,509)
danskespilHTS=(804,491,845,509)
danskespilzoom=1
danskespilscroll="window.scrollTo(0.0*document.body.scrollWidth, 0.05*document.body.scrollHeight);"
#nordicbet
nordicbetlink="https://www.nordicbet.dk/sports#m=951&bgi=1"
nordicbetHTS=(934,160,987,179)
nordicbetLLR=(934,204,987,221)
nordicbetzoom=5
nordicbetscroll="window.scrollTo(0.175*document.body.scrollWidth, 0.08*document.body.scrollHeight);"
#betsafe
betsafelink="https://www.betsafe.dk/odds/#/#m%3D951%26bgi%3D1"
betsafeLLR=(860,287,951,326)
betsafeHTS=(860,366,951,408)
betsafezoom=8
betsafescroll="window.scrollTo(0.4*document.body.scrollWidth, 0.1*document.body.scrollHeight);"
#Unibet
unibetlink="https://www.unibet.dk/betting#/group/2000061905/category/3998"
unibetHTS=(941,311,1003,329)
unibetLLR=(941,289,1003,304)
unibetzoom=5
unibetscroll="window.scrollTo(0.15*document.body.scrollWidth, 0.05*document.body.scrollHeight);"


# Define functions
def zoom(name,num):
	counts=0
	while counts<num:
		name.find_element_by_tag_name("body").send_keys(Keys.CONTROL,Keys.ADD)
		counts=counts+1

# Save data
# with open('data.csv','wb') as f:
#                                       fileWriter = csv.writer(f , delimiter=';')
#                                    # Screenshot

def sshot(name,link,HTS,LLR,scroll,zooms):
	driver = webdriver.Firefox()
	#OPEN WINDOW
	driver.get(link)
	time.sleep(10)
	driver.set_window_size(1024, 768)
	time.sleep(2)
	zoom(driver,zooms)
	# #TAKE SCREENSHOT
	time.sleep(5)
	driver.execute_script(scroll)
	time.sleep(5)
	im = ImageGrab.grab()
	timestr = time.strftime("%Y%m%d-%H%M%S")
	#SAVE SCREENSHOT
	im.save(name+'/'+timestr+'.tiff')
	driver.close()
	#CROP IMAGE
	im=Image.open(name+'/'+timestr+'.tiff')
	imfile=im.crop(HTS)
	basewidth = 300
	wpercent = (basewidth/float(imfile.size[0]))
	hsize = int((float(imfile.size[1])*float(wpercent)))
	imfile = imfile.resize((basewidth,hsize), Image.ANTIALIAS)
	imfile.save(name+'/cropped'+timestr+'HTS.tiff')	
	#LLR
	imfile=im.crop(LLR)
	#Resize
	basewidth = 300
	wpercent = (basewidth/float(imfile.size[0]))
	hsize = int((float(imfile.size[1])*float(wpercent)))
	imfile = imfile.resize((basewidth,hsize), Image.ANTIALIAS)
	imfile.save(name+'/cropped'+timestr+'LLR.tiff')
	# Encode
	LLR=str((pytesseract.image_to_string(Image.open(name+'/cropped'+timestr+'LLR.tiff'))))
	HTS=str((pytesseract.image_to_string(Image.open(name+'/cropped'+timestr+'HTS.tiff'))))
	try:
		LLR=LLR.replace(",", ".")
		LLR=LLR.replace(" ", "")
		HTS=HTS.replace(",", ".")
		HTS=HTS.replace(" ", "")
		HTS=HTS.replace("l", "1")
		LLR=LLR.replace("l", "1")
	except:
		print("decoding failed")
	return(LLR,HTS)
	
#Loop
def myloop():
 	#try:
 	time.sleep(9000)
 	try:
 		time.sleep(900)
 		print("Starting: "+str(countme)+'started at'+time.strftime("%H%M"))
		global count
		bf=sshot("betfair",betfairlink,befairHTS,befairLLR,betfairscroll,betfairzoom)
		ds=sshot("danskespil",danskespillink,danskespilHTS,danskespilLLR,danskespilscroll,danskespilzoom)
		ub=sshot("unibet",unibetlink,unibetHTS,unibetLLR,unibetscroll,unibetzoom)
		nb=sshot("nordicbet",nordicbetlink,nordicbetHTS,nordicbetLLR,nordicbetscroll,nordicbetzoom)

		# Save data
		times = time.strftime("%H%M")
		dates = time.strftime("%m%d")
		with open('data.csv','a') as f:
	                                 fileWriter = csv.writer(f , delimiter=str(u';'))
	                                 fileWriter.writerows([[dates,times, bf[0],bf[1],ds[0],ds[1],ub[0],ub[1],nb[0],nb[1]]]) 
	except:
		time.sleep(1800)
	 	print("failed")  



		



countme=0
while countme<1000:
		print("Iteration: "+str(countme)+'started at'+time.strftime("%H%M"))
		myloop()
		countme=countme+1

	

