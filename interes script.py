#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:28:15 2018

@author: laiunce
"""

from pytrends.request import TrendReq
import datetime
from datetime import datetime, timedelta

def convierte_datetime(datetime):
    return datetime - timedelta(hours=3)


fecha_hora ='20180313 22:05:00'
rango= 2
kw_list = ["reparacion total"]
Pais='AR'

pytrends = TrendReq()
#se le agregan 3 horas por diferencia argentina con server
datetimeobject = datetime.strptime(fecha_hora,'%Y%m%d %H:%M:%S') + timedelta(hours=3)
deltatiempo =  timedelta(hours=rango)
fecha_hora_delta_sum = datetimeobject +deltatiempo
fecha_hora_delta_res = datetimeobject -deltatiempo
time_range = str(fecha_hora_delta_res.isoformat())[:13]+' '+str(fecha_hora_delta_sum.isoformat())[:13]
pytrends.build_payload(kw_list, cat=0, timeframe= time_range, geo=Pais, gprop='')
p=pytrends.interest_over_time()

#Modifica indices
p['indice'] =p.index
p.index = p.apply(lambda row: convierte_datetime(row['indice']), axis=1)
p.drop('indice', inplace=True, axis=1)









