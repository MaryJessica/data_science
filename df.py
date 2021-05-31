# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:23:17 2021

@author: Mary Jessica
"""

import glassdoor_scrapper as gs
import pandas as pd
path = "C:/Users/Mary Jessica/OneDrive/Desktop/DataScience/chromedriver"
df= gs.get_jobs('Data Scientist',15,False, path,15)

df.to_csv('glassdoor_jobs.csv',index=False)
