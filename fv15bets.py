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
import time as pythontime
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
danskespilLLR=(517,289,555,302)
danskespilHTS=(799,289,841,302)
danskespilzoom=1
danskespilscroll="window.scrollTo(0.0*document.body.scrollWidth, 0.05*document.body.scrollHeight);"
#nordicbet
nordicbetlink="https://www.nordicbet.dk/sports#m=951&bgi=1"
nordicbetLLR=(933,212,994,233)
nordicbetHTS=(933,253,994,268)
nordicbetzoom=5
nordicbetscroll="window.scrollTo(0.175*document.body.scrollWidth, 0.075*document.body.scrollHeight);"
#betsafe
betsafelink="https://www.betsafe.dk/odds/#/#m%3D951%26bgi%3D1"
betsafeLLR=(860,287,951,326)
betsafeHTS=(860,366,951,408)
betsafezoom=8
betsafescroll="window.scrollTo(0.4*document.body.scrollWidth, 0.1*document.body.scrollHeight);"
#Unibet
unibetlink="https://www.unibet.dk/betting#/group/2000061905/category/3998"
unibetLLR=(753,226,798,240)
unibetHTS=(753,254,798,263)
unibetzoom=11
unibetscroll="window.scrollTo(0.45*document.body.scrollWidth, 0.05*document.body.scrollHeight);"


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
def makefig(name,col1,col2):
	csv_f = csv.reader(open("data.csv"), delimiter=str(u';'))
	hts=[];
	llr=[];
	rownumber=1;
	laghts=0;
	lagllr=0;
	time=[];
	probllr=[];
	probhts=[];
	for row in csv_f:
	  if row != []: 
	  	if rownumber>1:
	  		# save date
	  		try:
		  		if int(row[0])<600:
		  			d=531-int(row[0])+18
			  	if int(row[0])>600:
			  		d=618-int(row[0])
			  	# save time
			  	b=row[1]
		  		h=d+(float((24-float(b[:2]))*60+60-float(b[2:4])))/1440
		  		time.append(h)
		  	except ValueError:
		  		continue
		  	# save hts
		  	if len(row[col1])>0 :
	  			try:
	  					laghts=float(row[col1])
		  				hts.append(float(row[col1]))
		  				htsa=float(row[col1])
		  		except ValueError:
		  			hts.append(laghts)
		  			htsa=laghts
		  	if len(row[col1])<1:
		  		hts.append(laghts)
		  		htsa=laghts
		  	# save llr 
		  	if len(row[col2])>0 :
	  			try:
	  					lagllr=float(row[col2])
		  				llr.append(float(row[col2]))
		  				llra=float(row[col2])
		  		except ValueError:
		  			llr.append(lagllr)
		  			llra=float(lagllr)
		  	if len(row[col2])<1:
		  		llr.append(lagllr)
		  		llra=float(lagllr)
			try:
				probllr.append(100*htsa/(llra+htsa))
				probhts.append(100*llra/(llra+htsa))
			except ValueError:
				continue	
	  	rownumber=rownumber+1
	matplotlib.rcParams.update({'font.size':22})
	fig=plt.figure(figsize=(20,9))
	ax=fig.add_axes([0,0,1,1])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	xlim(20,0)
	ylim(0,4)
	plt.plot(time,llr,'b-', linewidth=4.0,label="Lars Løkke Rasmussen")
	plt.plot(time,hts,'r-', linewidth=4.0,label="Helle Thorning-Schmidt")
	plt.legend(frameon=False)
	plt.ylabel('Odds')
	plt.xlabel('Dage til valg')
	tid= pythontime.strftime("%Y%m%d-%H%M")
	text(10.1,-.5,'Af @njharbo og @hhsievertsen. Senest opdateret:'+tid)
	savefig(name+'.png', bbox_inches='tight')
	plt.close()
	plt.clf()
	fig=plt.figure(figsize=(20,9))
	ax=fig.add_axes([0,0,1,1])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	xlim(20,0)
	ylim(0,100)
	axhline(y=50,xmin=0,xmax=20,color='0.75')
	plt.plot(time,probllr,'b-', linewidth=4.0,label="Lars Løkke Rasmussen")
	plt.plot(time,probhts,'r-', linewidth=4.0,label="Helle Thorning-Schmidt")
	plt.legend(frameon=False)
	plt.ylabel('Implicit sandsynlighed')
	plt.xlabel('Dage til valg')
	tid= pythontime.strftime("%Y%m%d-%H%M")
	text(10.1,-15,'Af @njharbo og @hhsievertsen. Senest opdateret:'+tid)
	savefig(name+'_sandsynlighed.png', bbox_inches='tight')
	plt.close()
	plt.clf()


def spangraph(name):
	llr_ssh_max=[]
	llr_ssh_mean=[]
	llr_ssh_min=[]
	hts_ssh_max=[]
	hts_ssh_mean=[]
	hts_ssh_min=[]
	time=[]
	csv_f = csv.reader(open("data.csv"), delimiter=str(u';'))
	for row in csv_f:
		# save date
		try:
			if float(row[0])<600:
				d=531-float(row[0])+18
	  		if float(row[0])>600:
	  			d=618-float(row[0])
	  	# save time
	  		b=row[1]
			h=d+(float((24-float(b[:2]))*60+60-float(b[2:4])))/1440
			time.append(h)
		except:
			continue
		try:
			llr_ssh_1=1/float(row[4])/(1/float(row[3])+1/float(row[4]))
		except:
			llr_ssh_1=np.nan
		try:
			llr_ssh_2=1/float(row[6])/(1/float(row[5])+1/float(row[6]))
		except:
			llr_ssh_2=np.nan
		try:
			llr_ssh_3=1/float(row[8])/(1/float(row[7])+1/float(row[8]))
		except:
			llr_ssh_3=np.nan
		try:
			llr_ssh_4=1/float(row[10])/(1/float(row[9])+1/float(row[10]))
		except:
			llr_ssh_4=np.nan
		try:
			hts_ssh_1=1/float(row[3])/(1/float(row[3])+1/float(row[4]))
		except:
			hts_ssh_1=np.nan
		try:
			hts_ssh_2=1/float(row[5])/(1/float(row[5])+1/float(row[6]))
		except:
			hts_ssh_2=np.nan
		try:
			hts_ssh_3=1/float(row[7])/(1/float(row[7])+1/float(row[8]))
		except:
			hts_ssh_3=np.nan
		try:
			hts_ssh_4=1/float(row[9])/(1/float(row[9])+1/float(row[10]))
		except:
			hts_ssh_4=np.nan
		# #mean, min and max for hts
		array_ssh_hts=(hts_ssh_1,hts_ssh_2,hts_ssh_3,hts_ssh_4)
		array_ssh_llr=(llr_ssh_1,llr_ssh_2,llr_ssh_3,llr_ssh_4)
		hts_ssh_mean.append(100*np.nanmean(array_ssh_hts,0))
		hts_ssh_min.append(100*np.nanmin(array_ssh_hts,0))
		hts_ssh_max.append(100*np.nanmax(array_ssh_hts,0))
		llr_ssh_mean.append(100*np.nanmean(array_ssh_llr,0))
		llr_ssh_min.append(100*np.nanmin(array_ssh_llr,0))
		llr_ssh_max.append(100*np.nanmax(array_ssh_llr,0))

	#Fan chart, probs
	matplotlib.rcParams.update({'font.size':22})
	fig=plt.figure(figsize=(20,9))
	ax=fig.add_axes([0,0,1,1])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	xlim(20,0)
	ylim(0,100)
	axhline(y=50,xmin=0,xmax=20,color='0.75')
	plt.fill_between(time, hts_ssh_max, hts_ssh_min,color=(0.99, 0.33, 0.33), alpha=1)
	plt.plot(time, hts_ssh_mean, color=(0.99, 0., 0.),label="Helle Thorning-Schmidt",linewidth=4.0,) # Plot the original signal
	plt.fill_between(time, llr_ssh_max, llr_ssh_min,color=(0.4, 0.4, 0.99), alpha=1,)
	plt.plot(time, llr_ssh_mean, color=(0.0, 0., 0.99),label="Lars Løkke Rasmussen",linewidth=4.0,) # Plot the original signal
	plt.legend(frameon=False)
	plt.ylabel('Implicit sandsynlighed')
	plt.xlabel('Dage til valg')
	tid= pythontime.strftime("%Y%m%d-%H%M")
	text(10.1,-15,'Af @njharbo og @hhsievertsen. Senest opdateret:'+tid)
	savefig(name+'.png', bbox_inches='tight')
	plt.close()
	plt.clf()

def sshot(name,link,HTS,LLR,scroll,zooms):
	driver = webdriver.Firefox()
	#OPEN WINDOW
	driver.get(link)
	pythontime.sleep(10)
	driver.set_window_size(1024, 768)
	pythontime.sleep(2)
	zoom(driver,zooms)
	# #TAKE SCREENSHOT
	pythontime.sleep(5)
	driver.execute_script(scroll)
	pythontime.sleep(5)
	im = ImageGrab.grab()
	timestr = pythontime.strftime("%Y%m%d-%H%M%S")
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
	LLR=LLR.replace(",", ".")
	LLR=LLR.replace(" ", "")
	HTS=HTS.replace(",", ".")
	HTS=HTS.replace(" ", "")
	return(LLR,HTS)
	
#Loop
def myloop():
 	#try:
		global count
		bf=sshot("betfair",betfairlink,befairHTS,befairLLR,betfairscroll,betfairzoom)
		ds=sshot("danskespil",danskespillink,danskespilHTS,danskespilLLR,danskespilscroll,danskespilzoom)
		ub=sshot("unibet",unibetlink,unibetHTS,unibetLLR,unibetscroll,unibetzoom)
		nb=sshot("nordicbet",nordicbetlink,nordicbetHTS,nordicbetLLR,nordicbetscroll,nordicbetzoom)

		# Save data
		times = pythontime.strftime("%H%M")
		dates = pythontime.strftime("%m%d")
		with open('data.csv','a') as f:
	                                 fileWriter = csv.writer(f , delimiter=str(u';'))
	                                 fileWriter.writerows([[dates,times, bf[0],bf[1],ds[0],ds[1],ub[0],ub[1],nb[0],nb[1]]]) 

		# produce graphs
		makefig("betfair",3,2)
		makefig("danskespil",5,4)
		makefig("unibet",7,6)
		makefig("nordicbet",9,8)
		spangraph("spangraph")
		# Nextiteration
		count=count+1
		print("Iteration: "+str(count))
		pythontime.sleep(1800)
	 	myloop()



	#except:
	 	print("Iteration: "+str(count)+" failed. ")
	 	count=count+1
	  	pythontime.sleep(1800)
	 	myloop()

myloop()


