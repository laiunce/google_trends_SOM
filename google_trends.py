#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:28:15 2018

@author: laiunce
"""



#################################################################################################################
### START 0° BLOCK  >>>>>  Libraries

# Import libaries
from pytrends.request import TrendReq
import datetime
import json
import time
from pytrends.request import TrendReq
from datetime import datetime, timedelta

### END 0° BLOCK  <<<<<   Libraries
#################################################################################################################




#################################################################################################################
### START 1° BLOCK  >>>>>  FUNCTION DEFINITION

# This function converts the time retrieved from the server time to local time (google trends have 3 hours of difference from Argentina).
# If you want to analyse google interest at 4 pm in argentina,it correspond to 7pm in google trends server time 
# so you have to make the conversion adding 3 hours, consult the API and then you call this function to
# reconvert server time to Argentina time and then be able to join with other sources or analyse it
def convierte_datetime(datetime):
    return datetime - timedelta(hours=3)


### END 1° BLOCK  <<<<<  FUNCTION DEFINITION
#################################################################################################################





#################################################################################################################
### START 2° BLOCK >>>>>   Parameters definitions

#fecha_hora in YYYYMMMDDD HH:MM:SS (year month day hour minute second time format)
#is the time in wich you want to analyse the google trends data
fecha_hora ='20180710 16:00:00'
# delta is the amount of time of the time windows before and after fecha_hora
# example, if you set the analysis at 20180710 16:00:00 and a delta (in hours) of 1, google trends will retrieve data
# from 15:00:00 hs to 17:00:00 hs (3pm to 5 pm) is 24 hs format
delta= 1
#kw_list is the words, in this case only one, but you can change it
# example kw_list = ["elvive","sedal"]
kw_list = ["elvive"]

### END 2° BLOCK  >>>>>   Parameters definitions
#################################################################################################################




#################################################################################################################
### START 3° BLOCK >>>>>  API Call

#here start the magic, it simulate an API calling this library
pytrends = TrendReq()
### we add 3 hours of differente from argentina and the server
datetimeobject = datetime.strptime(fecha_hora,'%Y%m%d %H:%M:%S') + timedelta(hours=3)
#define the timerange in the API call to make the windows -delta and +delta
deltatiempo =  timedelta(hours=delta)
fecha_hora_delta_sum = datetimeobject +deltatiempo
fecha_hora_delta_res = datetimeobject -deltatiempo
time_range = str(fecha_hora_delta_res.isoformat())[:13]+' '+str(fecha_hora_delta_sum.isoformat())[:13]
#we call google trends based on definition, list of words, timerange, geo (in this case argentina) 
pytrends.build_payload(kw_list, cat=0, timeframe= time_range, geo='AR', gprop='')
p=pytrends.interest_over_time()
#we create a column with the dates
p['indice'] =p.index

#we apply the convertion of hours calling the function
p['fechahora'] = p.apply(lambda row: convierte_datetime(row['indice']), axis=1)

#note that the wider the timewindow is, the wider is the timerange retrieves.
#consulting only 3 hours will retrieve minute by minute
#consulting 24 hours will retrieve timeranges by 8 minutes


### END 3° BLOCK  >>>>>   API Call
#################################################################################################################





#################################################################################################################
### START 4° BLOCK  >>>>>  Data Analysis

print(p)

### END 4° BLOCK  >>>>>   Data Analysis
#################################################################################################################











