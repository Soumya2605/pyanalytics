# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:34:44 2020

@author: Soumya Swaminath
"""


#%%importing libraries
import pandas as pd


#%%importing csv file
data=pd.read_csv('denco.csv')
data.head()
data.columns

#%% most loyal Customers
loyal = data['custname'].value_counts()
print("Top 10 customers by number of transactions:\n \n", loyal.head(10))


#%% customers who contribute the most to their revenue
#revenuetot : the total revenue per customer
revenuetot = data.groupby(['custname'])['revenue'].sum().reset_index()
revenuetot
#sort revenuetot in descending order
toprev = revenuetot.sort_values(by ='revenue', ascending = 0) 
print("Top 10 customers by total revenue:\n \n", toprev.head(10))


#%%Part numbers who bring in significant portion of revenue
#partrevenue is the total revenue per part number
partrevenue = data.groupby(['partnum'])['revenue'].sum().reset_index()
partrevenue
#sorting partrevenue in descending order
toppart = partrevenue.sort_values(by='revenue', ascending = 0)
print("Top 10 part numbers by total revenue:\n \n", toppart.head(10))


#%%What parts have the highest profit margin?
#partmargin is the total pargin per part number
partmargin = data.groupby(['partnum'])['margin'].sum().reset_index()
partmargin
#sorting partmargin in descending order
topmargin = partmargin.sort_values(by='margin', ascending = 0)
print("Top 10 part numbers by total profit margin:\n \n", topmargin.head(10))


#%%Who are their top buying customers?
print("Top buying customer by number of transactions is:\n \n", loyal.head(1))



#%%Who are the customers who are bringing more revenue?
print("Top customer by total revenue is :\n \n", toprev.head(1))

