# -*- coding: utf-8 -*- 
# Load libs.
from __future__ import unicode_literals
from __future__ import division
# Load tools for image processing
from PIL import Image

#Load tool for timing
import time as pythontime
#Load tool for saving to CSV
import csv
#Numpy 
import numpy as np

#plotting
import matplotlib.pyplot as plt
from pylab import *

lasttime=0
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
	plt.xticks(np.arange(0, 20, 1))
	ylim(0,4)
	plt.yticks(np.arange(0, 4, 0.5))
	plt.plot(time,llr,'b-', linewidth=4.0,label="Lars Løkke Rasmussen")
	plt.plot(time,hts,'r-', linewidth=4.0,label="Helle Thorning-Schmidt")
	plt.legend(frameon=False)
	plt.ylabel('Odds')
	plt.xlabel('Dage til valg')
	tid= pythontime.strftime("%Y%m%d-%H%M")
	text(10.1,-.5,'Af @njharbo og @hhsievertsen. Senest opdateret:'+tid)
	plt.grid()
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
	plt.ylabel('Sandsynlighed, i procent')
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
	  			d=617-float(row[0])
	  	# save time
	  		b=row[1]
			h=d+(float((24-float(b[:2]))*60+60-float(b[2:4])))/1440
			time.append(h)
			lasttime=h
		except:
			continue
		try:
			llr_ssh_1=1/float(row[2])/(1/float(row[3])+1/float(row[2]))
		except:
			llr_ssh_1=np.nan
		try:
			llr_ssh_2=1/float(row[4])/(1/float(row[5])+1/float(row[4]))
		except:
			llr_ssh_2=np.nan
		try:
			llr_ssh_3=1/float(row[6])/(1/float(row[7])+1/float(row[6]))
		except:
			llr_ssh_3=np.nan
		try:
			llr_ssh_4=1/float(row[8])/(1/float(row[9])+1/float(row[8]))
		except:
			llr_ssh_4=np.nan
		try:
			hts_ssh_1=1/float(row[3])/(1/float(row[3])+1/float(row[2]))
		except:
			hts_ssh_1=np.nan
		try:
			hts_ssh_2=1/float(row[5])/(1/float(row[5])+1/float(row[4]))
		except:
			hts_ssh_2=np.nan
		try:
			hts_ssh_3=1/float(row[7])/(1/float(row[7])+1/float(row[6]))
		except:
			hts_ssh_3=np.nan
		try:
			hts_ssh_4=1/float(row[9])/(1/float(row[9])+1/float(row[8]))
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
		lastllrmean=100*np.nanmean(array_ssh_llr,0)
		lasthtsmean=100*np.nanmean(array_ssh_hts,0)
		lasthtsmeanview=round(lasthtsmean,1)
    	lastllrmeanview=round(lastllrmean,1)
    	print(array_ssh_llr)
    	print(array_ssh_hts)


	#Fan chart, probs
	matplotlib.rcParams.update({'font.size':22})
	fig=plt.figure(figsize=(20,9))
	ax=fig.add_axes([0,0,1,1])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	xlim(20,0)
	plt.xticks(np.arange(0, 20, 1.0))
	ylim(0,100)
	plt.yticks(np.arange(0, 101, 10))
	axhline(y=50,xmin=0,xmax=20,color='0.75')
	plt.fill_between(time, hts_ssh_max, hts_ssh_min,color=(0.99, 0.33, 0.33), alpha=0.7)
	plt.plot(time, hts_ssh_mean, color=(0.99, 0., 0.),label="Helle Thorning-Schmidt",linewidth=4.0,) # Plot the original signal
	plt.fill_between(time, llr_ssh_max, llr_ssh_min,color=(0.4, 0.4, 0.99), alpha=0.5)
	plt.plot(time, llr_ssh_mean, color=(0.0, 0., 0.99),label="Lars Løkke Rasmussen",linewidth=4.0,) # Plot the original signal
	plt.legend(frameon=False)
	plt.ylabel('Sandsynlighed, %')
	plt.xlabel('Dage til valg')
	tid= pythontime.strftime("%Y%m%d-%H%M")
	lasttime=lasttime-.3
	text(lasttime,lasthtsmean-2,lasthtsmeanview, color='red')
	text(lasttime,lastllrmean+1,lastllrmeanview, color='blue')
	text(20,-14,'Figuren viser intervallet af implicitte sandsynligheder for at hhv. HTS og LLR vinder valget, udregnet fra 4 bookmakers odds. Se FAQ for detaljer.', size=20)
	text(10.1,-20,'Af @njharbo og @hhsievertsen. Senest opdateret:'+tid)
	plt.grid()
	savefig(name+'.png', bbox_inches='tight')
	plt.close()
	plt.clf()

		#Mean chart, probs
	matplotlib.rcParams.update({'font.size':22})
	fig=plt.figure(figsize=(20,9))
	ax=fig.add_axes([0,0,1,1])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	xlim(20,0)
	plt.xticks(np.arange(0, 20, 1.0))
	ylim(0,100)
	plt.yticks(np.arange(0, 101, 10))
	axhline(y=50,xmin=0,xmax=20,color='0.75')
	#plt.fill_between(time, hts_ssh_max, hts_ssh_min,color=(0.99, 0.33, 0.33), alpha=0.7)
	plt.plot(time, hts_ssh_mean, color=(0.99, 0., 0.),label="Helle Thorning-Schmidt",linewidth=4.0,) # Plot the original signal
	#plt.fill_between(time, llr_ssh_max, llr_ssh_min,color=(0.4, 0.4, 0.99), alpha=0.5)
	plt.plot(time, llr_ssh_mean, color=(0.0, 0., 0.99),label="Lars Løkke Rasmussen",linewidth=4.0,) # Plot the original signal
	plt.legend(frameon=False)
	plt.ylabel('Sandsynlighed, %')
	plt.xlabel('Dage til valg')
	tid= pythontime.strftime("%Y%m%d-%H%M")
	lasttime=lasttime-.3
	text(lasttime,lasthtsmean+1,lasthtsmeanview, color='red')
	text(lasttime,lastllrmean-2,lastllrmeanview, color='blue')
	text(20,-14,'Figuren viser den gennemsnitlige implicitte sandsynlighed for at hhv. HTS og LLR vinder valget, udregnet fra 4 bookmakers odds. Se FAQ for detaljer.', size=20)
	text(10.1,-20,'Af @njharbo og @hhsievertsen. Senest opdateret:'+tid)
	plt.grid()
	savefig(name+'2.png', bbox_inches='tight')
	plt.close()
	plt.clf()

		# produce graphs
makefig("betfair",3,2)
makefig("danskespil",5,4)
makefig("unibet",7,6)
makefig("nordicbet",9,8)
spangraph("spangraph")
