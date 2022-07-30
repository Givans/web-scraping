from random import randint
from currency_converter import CurrencyConverter
import xlrd
from scraping import scrape_data

import sqlite3
# Connecting to sqlite
conn = sqlite3.connect('bank.db')
  
# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

# creating table
# Creating table
try:
    table ="""CREATE TABLE RECORDS(date VARCHAR(255), time VARCHAR(255),price VARCHAR(255),currency VARCHAR(255), volume VARCHAR(255),tradeValue VARCHAR(255), tradeType VARCHAR(255), tradeFlag VARCHAR(255),venueOfPublication VARCHAR(255), mic VARCHAR(255),link VARCHAR(255));"""
    cursor.execute(table)

except:
    pass

# Program extracting first column
print('Software inizialised...Please wait...')

 
loc = ("csv/ConsolidatedEnergyListings.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for i in range(sheet.nrows):
    link = sheet.cell_value(i, 4)
    if link == 'url' or link == '':
        print('passing url.. no url found')
        pass
    else:
        # getting the data from the dictionary in scraping.py
        ### TODO: Change the functions and call the in a loop
        context = scrape_data(link)
        def b_date():
            try:
                date = context[list(context.keys())[0]]
            except:
                date = 'null'
            return date
        def b_time():
            try:
                time = context[list(context.keys())[1]]
            except:
                time = 'null'
            return time
        def b_price():
            try:
                price = context[list(context.keys())[2]]
            except:
                price = 'null'
            return price
        def b_currency():
            try:
                currency = context[list(context.keys())[3]]
            except:
                currency = 'null'
            return currency
        def b_volume():
            try:
                volume = context[list(context.keys())[4]]
            except:
                volume = 'null'
            return volume
        def b_tradeValue():
            try:
                tradeValue = context[list(context.keys())[5]]
            except:
                tradeValue = 'null'
            return tradeValue
        def b_tradeType():
            try:
                tradeType = context[list(context.keys())[6]]
            except:
                tradeType = 'null'
            return tradeType
        def b_tradeFlag():
            try:
                tradeFlag = context[list(context.keys())[7]]
            except:
                tradeFlag = 'null'
            return tradeFlag
        def b_venueOfPublication():
            try:
                venueOfPublication = context[list(context.keys())[8]]
            except:
                venueOfPublication = 'null'
            return venueOfPublication
        def b_mic():
            try:
                mic = context[list(context.keys())[9]]
            except:
                mic = 'null'
            return mic
        def b_link():
            try:
                link = context[list(context.keys())[10]]
            except:
                link = 'null'
            return link
        
            
        # add the data to the database
        # getting the exact values from functions

        date_b = b_date()
        time_b = b_time()
        price = b_price()
        currency = b_currency()
        volume = b_volume()
        tradeValue = b_tradeValue()
        tradeType = b_tradeType()
        tradeFlag = b_tradeFlag()
        venueOfPublication = b_venueOfPublication()
        mic = b_mic()
        link_l = b_link()

        # checking if the data already exists in the database
        
        # if data exists
        # if data does not exist
        # Preparing SQL queries to INSERT a record into the database.
        params = (date_b, time_b, price, currency, volume, tradeValue, tradeType, tradeFlag, venueOfPublication, mic, link_l)
        cursor.execute("INSERT INTO RECORDS(date, time, price, currency, volume, tradeValue, tradeType, tradeFlag, venueOfPublication, mic, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)",params)
        # Commit your changes in 
        # the database    
        conn.commit()
        print('data saved')
        
# Closing the connection
conn.close()

rate = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')


