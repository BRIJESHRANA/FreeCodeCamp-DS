# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 01:04:32 2019

@author: Brijesh Rana
"""
import logging
import pymssql
import pandas as pd
import sqlalchemy
from fbprophet import Prophet 
import pyodbc	
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from sqlalchemy import create_engine, MetaData, Table, select
from six.moves import urllib


class test:
    con1 = Employee.dbConnection()
    sql="select name FROM sys.databases where name like '%Hiranandani%'"
    dbnames1 = pd.read_sql(sql,con1)
    dbnames
    
    
    
     # logging  
  LOG = "D:/log/ccd.log"                                                     
  logging.basicConfig(filename=LOG, filemode="w", level=logging.DEBUG)  

  # console handler  
  console = logging.StreamHandler()  
  console.setLevel(logging.ERROR)  
  logging.getLogger("").addHandler(console)