'''
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 4     	10% - Pandas Data Interpretation
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# The dataset used was collected from the following website:
# https://www.sciencedirect.com/science/article/pii/S2352340918315191

# read the CSV file
dataset = pd.read_csv('hotel_bookings.csv')

# Will ensure that all columns are displayed
pd.set_option('display.max_columns', None) 

# prints out the top 5 values for the datasef
print(dataset.head())

# checking the dataset shape
print(dataset.shape)
# (119390, 32)


# prints out names of columns
print(dataset.columns)

# This tells us which variables are object, int64 and float 64. This would mean that 
# some of the object variables might have to be changed into a categorical variables and int64 to float64 
# depending on our analysis.
print(dataset.info())
# dtypes: float64(4), int64(16), object(12)

# checking for counts data and gives Mean, Sd and quartiles for all columns
print(dataset.describe())

# checking for missing data
pd.isna(dataset)
# not very useful as it is not possible to see all the columns

# checking for missing data
print('Nan in each columns' , dataset.isna().sum(), sep='\n')
# This means that there are missing (NULL) values in 4 columns: (4) children, 
# (488) country, (16340) agent and (112593)company

# Dropping company variables due to the fact that it has the most amount of data missing
dataset.drop('company',axis=1,inplace=True)

# Looking for all the unique values in all the columns
column = dataset.columns
for i in column:
    print('\n',i,'\n',dataset[i].unique(),'\n','-'*80)
  
    
# making object into categorical variables
dataset['hotel'] = dataset['hotel'].astype('category')
dataset['arrival_date_month'] = dataset['arrival_date_month'].astype('category')
dataset['meal'] = dataset['meal'].astype('category')
dataset['country'] = dataset['country'].astype('category')
dataset['market_segment'] = dataset['market_segment'].astype('category')
dataset['distribution_channel'] = dataset['distribution_channel'].astype('category')
dataset['reserved_room_type'] = dataset['reserved_room_type'].astype('category')
dataset['assigned_room_type'] = dataset['assigned_room_type'].astype('category')
dataset['deposit_type'] = dataset['deposit_type'].astype('category')
dataset['customer_type'] = dataset['customer_type'].astype('category')
dataset['reservation_status'] = dataset['reservation_status'].astype('category')

# checking data to check that all objects have been changed to categorical variables.
dataset.info()
# dtypes: category(11), float64(4), int64(16), object(1)
# all obejcts have been succesfully changed.


dataset['arrival_date_month'].dtype
# CategoricalDtype(categories=['April', 'August', 'December', 'February', 'January', 'July',
# 'June', 'March', 'May', 'November', 'October', 'September'],
# ordered=False)

dataset['arrival_date_month'].unique()
# Length: 12
# Categories (12, object): [July, August, September, October, ..., March, April, May, June]

# Reordering months so that it starts with 'January' and proceed in the correct order
dataset['arrival_date_month'] = dataset['arrival_date_month'].cat.reorder_categories(['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
# Length: 12
# Categories (12, object): [January < February < March < April ... September < October < November < December]

dataset.groupby('arrival_date_month').size()
# arrival_date_month
# January       5929
# February      8068
# March         9794
# April        11089
# May          11791
# June         10939
# July         12661
# August       13877
# September    10508
# October      11160
# November      6794
# December      6780
# dtype: int64

# Graph examining number of Reservations for each month
plt.figure(figsize = (12, 8))
sns.countplot(x='arrival_date_month', data = dataset, palette = 'terrain', order = dataset['arrival_date_month'].value_counts().index)
plt.xticks(rotation = 90)
plt.title('Number of Reservation for Each Month', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Month', fontsize = 14)
plt.show()
print('It is clear that August, July and May are the Top 3 months for travel')
print('The winter months are the three least popular months for travel.')


# =============================================================================
# Converting 'reservation_status_date' to datetime
# =============================================================================

def time_conv(x):
    return datetime.datetime.strptime(x,'%Y-%m-%d').date()

dataset['reservation_status_date'] = dataset['reservation_status_date'].apply(lambda x : time_conv(x))

# =============================================================================
# Creating a new variable of the total number of guests per Reservation
# and examing the new variable
# =============================================================================

dataset['total_guests'] = dataset['adults']+ dataset['children']+ dataset['babies']

# viewing most common group type
dataset.groupby(['total_guests']).size().sort_values(ascending=False)
# total_guests
# 2.0     82048
# 1.0     22581
# 3.0     10494
# 4.0      3929
# 0.0       180
# 5.0       137
# 26.0        5
# 27.0        2
# 20.0        2
# 12.0        2
# 10.0        2
# 55.0        1
# 50.0        1
# 40.0        1
# 6.0         1
# dtype: int64

dataset['total_guests'].describe()
# count    119386.000000
# mean          1.968229
# std           0.722400
# min           0.000000
# 25%           2.000000
# 50%           2.000000
# 75%           2.000000
# max          55.000000
# Name: total_guests, dtype: float64
# This means that on average that people go in tw

# creating a graph for the number of people with a histogram
plt.figure(figsize = (12, 8))
sns.countplot(x = 'total_guests', data = dataset,palette = 'terrain',order = dataset['total_guests'].value_counts().head(15).index)
plt.xticks(rotation = 90)
plt.title('Number of Guests (Adults, Children, Babies)', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Number of Guests', fontsize = 14)
plt.show()
print('The trend shows that majority of reservations are for two people.')
print('The second highest trend is for just one person. It can be presumed that this are solo travelers.')


# =============================================================================
# Creating a new variable of the number of night stayed
# and examing the new variable
# =============================================================================
# getting total number of nights stayed (weekend and weekdays)
dataset['total_nights'] = dataset['stays_in_weekend_nights'] + dataset['stays_in_week_nights']

# viewing the most common length of stay
dataset.groupby(['total_nights']).size().sort_values(ascending=False)
# total_nights_stayed
# 2     27643
# 3     27076
# 1      21020
# 4     17383
# 7      8655
# 5      7784
# 6      3857
# 8      1161
# 10     1139
# 14      916
# 9       841

dataset['total_nights'].describe()
# count    119390.000000
# mean          3.427900
# std           2.557439
# min           0.000000
# 25%           2.000000
# 50%           3.000000
# 75%           4.000000
# max          69.000000
# Name: total_nights, dtype: float64

# Examining the length of stay with a histogram
plt.figure(figsize = (12, 8))
sns.countplot(x = 'total_nights', data = dataset, palette = 'terrain', order = dataset['total_nights'].value_counts().head(20).index)
plt.xticks(rotation = 90)
plt.title('Number of Nights Per Reservation', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Number of Nights', fontsize = 14)
plt.show()
print('The trend shows that majority of reservations stay for two or three night.')
print('It can be presumed that this is reflected by people going away by Friday, Saturday and Sunday.')

# =============================================================================
# Examining countries
# Splitting by countries and then data merging top 10 for analysis
# =============================================================================
dataset['country'].unique()
# Examining the most populat countries
dataset.groupby(['country']).size().sort_values(ascending=False)
# Top 5 countries for the bookings 
# PRT    48590
# GBR    12129
# FRA    10415
# ESP     8568
# DEU     7287

# Creating a table 
dataset.groupby(['country']).size().sort_values(ascending=False).head(25)
# country
# PRT    48590
# GBR    12129
# FRA    10415
# ESP     8568
# DEU     7287
# ITA     3766
# IRL     3375
# BEL     2342
# BRA     2224
# NLD     2104
# USA     2097
# CHE     1730
# CN      1279
# AUT     1263
# SWE     1024
# CHN      999
# POL      919
# ISR      669
# RUS      632
# NOR      607
# ROU      500
# FIN      447
# DNK      435
# AUS      426
# AGO      362
#dtype: int64

# Examines the top 25 countries that make a reservation
plt.figure(figsize = (12, 8))
sns.countplot(x = 'country', data = dataset, palette = 'viridis', order = dataset['country'].value_counts().head(20).index)
plt.xticks(rotation = 90)
plt.title('Breakdown of Top 25 Countries', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Top 25 Countries', fontsize = 14)
plt.show()
print('Graphs shows that majority of reservations are made for Portugal.')
print('However, there is a big drop to the second most popular country.')
print('The bars slowly decrease after the second most popular country.')

# Top 1 - PRT from the dataset
data_prt = dataset[dataset.country == 'PRT']

# Top 2 -  GBR from the dataset
data_gbr = dataset[dataset.country == 'GBR']

# Top 3- FRA from the dataset
data_fra = dataset[dataset.country == 'FRA']

# Top 4- ESP from the dataset
data_esp = dataset[dataset.country == 'ESP']

# Top 5- DEU from the dataset
data_deu = dataset[dataset.country == 'DEU']

# Top 6 - ITA from the dataset
data_ita = dataset[dataset.country == 'ITA']

# Top 7 - IRL from the dataset
data_irl = dataset[dataset.country == 'IRL']

# Top 8 - BEL from the dataset
data_bel = dataset[dataset.country == 'BEL']

# Top 9-BRA from the dataset
data_bra = dataset[dataset.country == 'BRA']

# Top 10
data_nld = dataset[dataset.country == 'NLD']


# Combining the data to create a dataset with just the top 10 countries
data_top10 = pd.concat([data_fra, data_gbr, data_prt, data_deu, data_esp,
                        data_ita,data_irl, data_bel, data_bra, data_nld]).reset_index(drop=True)

# creates a pie chart of the Top 10 countries 
fig = plt.figure(figsize = (20,10))
labels = data_top10['country'].value_counts().index.tolist()
sizes = data_top10['country'].value_counts().tolist()
plt.pie(sizes, labels = labels, autopct = '%1.1f%%',
        shadow = False, startangle = 30)
plt.title('The Breakdown of Top 10 Countries', fontdict = None, position = [0.48,1], size = 'xx-large')
plt.show()
print('This graph shows the percentage of reservations in each country.')

# Checking missing data
print('Nan in each columns' , data_top10.isna().sum())
# Missing data: agent                             14708
# Missing data: children                              4

# Checking unique labels in country
data_top10['country'].unique
# Name: country, Length: 100800, dtype: category
# Categories (177, object): [ABW, AGO, AIA, ALB, ..., VNM, ZAF, ZMB, ZWE]>

# Resetting the categories - to give the varaiables the right amount of levels
data_top10['country'] = data_top10['country'].cat.set_categories(['GBR', 'FRA', 'ESP', 'DEU', 'ITA', 
                                                                  'IRL', 'BEL', 'BRA', 'NLD', 'PRT'])
# Name: country, Length: 100800, dtype: category
# Categories (10, object): [GBR, FRA, ESP, DEU, ..., BEL, BRA, NLD, PRT]>

    
# Getting how many check-outs, cancelations and no-shows are in each country
data_top10.groupby('country')['reservation_status'].value_counts()

# creating a graph based on Top 10 and Reservation Status
reservation_countries = data_top10.groupby(['country','reservation_status']).lead_time.count()

# shows the table
print(reservation_countries)

# creates a graph
plt.figure(figsize = (12, 8))
sns.barplot(x = 'country', y = 'lead_time', hue = 'reservation_status', data = reservation_countries.reset_index(), palette = ['red', 'green', 'orange'])
plt.title('Reservation Status for Each Country', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Top 10 Countries', fontsize = 14)
L=plt.legend()
L.get_texts()[0].set_text('Canceled')
L.get_texts()[1].set_text('Check-Out')
L.get_texts()[2].set_text('No-Show')
plt.show()
print('It is clear that although Portugal has the most number of reservations.')
print('Unfortunately, Portugal has more cancelations than check-outs. ')
# From the graph, it is clear to see that PRT makes the most reservations, 
# but also more people making cancelations than people checking out of a hotel.

# =============================================================================
# Examining Popular Months in Each Year 
# =============================================================================
# creating the data 
data_top10['arrival_year_month'] =   data_top10['arrival_date_month'].astype(str) + "  " + data_top10['arrival_date_year'].astype(str)

# examining the table
print(data_top10['arrival_year_month'].value_counts())

# draw a graph 
plt.figure(figsize = (12, 8))
ax = sns.countplot(x = "arrival_year_month", data = data_top10, palette = "terrain")
plt.title('Number of Reservations by Most Popular Months and Years', fontsize = 16)
plt.xlabel('Month/Year', fontsize = 14)
plt.ylabel('Total Count', fontsize = 14)
plt.xticks(rotation = 90)
plt.show
print('This graph shows trand reservations by month and year.')
print('It is clear that there is a high number of reservations every year during spring and summer.')
print('As expected, there are reservations decrease in winder months every year.')
print('Furthermore, there has been a more number of reservations every year.')

# =============================================================================
# 
# =============================================================================

# Creating a graph 
is_cancel_month = data_top10.groupby(['arrival_date_month','is_canceled']).lead_time.count()

# prints a table
is_cancel_month 

# Breakdown of Reservations by MONTH For TOP 10 Countries
plt.figure(figsize = (12, 8))
sns.barplot(x = 'arrival_date_month', y = 'lead_time', hue = 'is_canceled', 
            data = is_cancel_month.reset_index(), palette = ['green', 'red'])
plt.title('Number of Cancelations and Check-Outs  for Each Month for Top 10 Countries', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Month', fontsize = 14)
L=plt.legend()
L.get_texts()[0].set_text('Check-out')
L.get_texts()[1].set_text('Canceled')
plt.xticks(rotation = 90)
plt.show()

# Breakdown of Reservations by MONTH/YEAR For Top 10 Countries
plt.figure(figsize = (12, 8))
sns.countplot(x = "arrival_year_month",  hue = 'is_canceled', data = data_top10, palette = ['green', 'red'])
plt.title('Number of Cancelations and Check-Outs  for Each Month and Year for Top 10 Countries', fontsize = 16)
plt.xlabel('Month and Year', fontsize = 14)
plt.ylabel('Total Count', fontsize = 14)
plt.xticks(rotation = 90)
L=plt.legend()
L.get_texts()[0].set_text('Check-out')
L.get_texts()[1].set_text('Canceled')
plt.xticks(rotation = 90)
plt.show()

# =============================================================================
# EXAMING CANCELATIONS IN PORTUGAL
# Because Portugal has more cancelations than check-outs, we decided to look at Portugal
# to see which months the cancelations are happening.
# =============================================================================

# changing index for Portugal
data_prt.reset_index(drop=True)

is_cancel_month_PRT = data_prt.groupby(['arrival_date_month','is_canceled']).lead_time.count()

# Breakdown of Reservations by MONTH For Portugal
plt.figure(figsize = (12, 8))
sns.barplot(x = 'arrival_date_month', y = 'lead_time', hue = 'is_canceled', data = is_cancel_month_PRT.reset_index(), palette = ['green', 'red'])
plt.title('Number of Cancelations for Each Month in Portugal', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Month', fontsize = 14)
L=plt.legend()
L.get_texts()[0].set_text('Check-Out')
L.get_texts()[1].set_text('Canceled')
plt.xticks(rotation = 90)
plt.show()
print('There is a more cancelation than check-outs during the spring and summer months in Portugal.')
print('This trend is also visible for September and October.')
print('However, there are more check-outs than cancelations in November, December, January, February and March')


## Creating a variable to insert into Portugal
data_prt['arrival_year_month_prt'] =   data_prt['arrival_date_month'].astype(str) + "  " + data_prt['arrival_date_year'].astype(str)

# creating the table for MONTH/YEAR for Portugal
is_cancel_year_month_PRT = data_prt.groupby(['arrival_year_month_prt','is_canceled']).lead_time.count()

# prints the table
print(is_cancel_year_month_PRT)

# Creating a bar chart for Reservations in Portugal for Month and Year
plt.figure(figsize = (12, 8))
sns.countplot(x = "arrival_year_month_prt",  hue = 'is_canceled', data = data_prt, palette = ['green', 'red'])
plt.title('Number of Cancelations and Check-Outs  for Each Month and Year for Portugal')
plt.xlabel('Month and Year')
plt.ylabel('Total Count')
plt.xticks(rotation = 90)
L=plt.legend()
L.get_texts()[0].set_text('Check-out')
L.get_texts()[1].set_text('Canceled')
plt.xticks(rotation = 90)
plt.show()
print('There are to be a lot of cancelations around spring and summer in all three years.')


# =============================================================================
# Splitting the data into cancelations or not cancelations
# =============================================================================
# splitting data on cancellations
# retrieving everyone who has NOT cancelled their reservation  
no_cancelations  = data_top10[data_top10['reservation_status'].isin(['Check-Out'])]

all_cancelations  = data_top10[data_top10['reservation_status'].isin(['Canceled', 'No-Show'])]

no_cancelations.groupby('hotel')['reservation_status'].value_counts()
# hotel         reservation_status
# City Hotel    Check-Out             30784
# Resort Hotel  Check-Out             23974
# Name: reservation_status, dtype: int64

all_cancelations.groupby('hotel')['reservation_status'].value_counts()
# hotel         reservation_status
# City Hotel    Canceled              26922
#              No-Show                 676
# Resort Hotel  Canceled               9853
#              No-Show                 273
# Name: reservation_status, dtype: int64

#creates graph
fig = plt.figure(figsize = (20, 10))
labels = data_top10['reservation_status'].value_counts().index.tolist()
sizes = data_top10['reservation_status'].value_counts().tolist()
plt.pie(sizes, labels = labels, autopct = '%1.1f%%',
        shadow = False, startangle = 30)
plt.title('Breakdown of Reservation Status (Top 10 Countries)', fontdict = None, position= [0.48, 1], size = 'xx-large')
plt.show()
# 61.2% of people check out of the hotel
# 37.9% cancel
# 0.9% of people No-Show
print('Less 2/3 of reservations get fulfilled. Nearly 40% of reservations are canceled or there is a no-show.')

fig = plt.figure(figsize = (20,10))
labels = all_cancelations['country'].value_counts().index.tolist()
sizes = all_cancelations['country'].value_counts().tolist()
plt.pie(sizes, labels = labels, autopct = '%1.1f%%',
        shadow = False, startangle = 30)
plt.title('The Breakdown of Cancelations by Top 10 Countries', fontdict=None, position= [0.48,1], size = 'xx-large')
plt.show()

# =============================================================================
# Pivot table
# =============================================================================

#checking the number of total_nights spent for each hotel and country
df1 = pd.DataFrame({'A': data_top10['hotel'],
                   'B': data_top10['total_nights'],
                   'C': data_top10['country']})
    
pd.pivot_table(df1, values='B', index=['C'], columns=['A'])


#checking the number of total_guests spent for each hotel and country
df2 = pd.DataFrame({'A': data_top10['hotel'],
                   'B': data_top10['total_guests'],
                   'C': data_top10['country']})
    
pd.pivot_table(df2, values='B', index=['C'], columns=['A'])


#checking the number of total_guests spent for each hotel , country and reservation status
df3 = pd.DataFrame({'A': data_top10['hotel'],
                   'B': data_top10['total_guests'],
                   'C': data_top10['is_canceled'],
                   'D': data_top10['country']})
    
pd.pivot_table(df3, values='B', index=['D','C'], columns=['A'])


# =============================================================================
# 
# =============================================================================

data_top10.groupby('is_canceled')['reservation_status'].value_counts()
# is_canceled  reservation_status
# 0            Check-Out             61643
# 1            Canceled              38205
#              No-Show                 952
# Name: reservation_status, dtype: int64

data_top10.groupby('hotel')['reservation_status'].value_counts()
# hotel         reservation_status
# City Hotel    Check-Out             36676
#               Canceled              28212
#               No-Show                 680
# Resort Hotel  Check-Out             24967
#               Canceled               9993
#               No-Show                 272
# Name: reservation_status, dtype: int64

# Number of people at the different types of hotel
df = pd.DataFrame(data_top10, columns = ['hotel', 'adults','children', 'babies', 'total_guests'])
print(df)

df.groupby('hotel')['adults','children', 'babies', 'total_guests'].sum()
#              adults  children  babies  total_guests
# hotel                                               
# City Hotel    121200    5368.0     337      126896.0
# Resort Hotel   65698    4208.0     499       70405.0


# =============================================================================
# ADR - Average Daily Rate
# =============================================================================
print('The highest value is: ', dataset['adr'].max())
# The highest value is :  5400.0

print('The lowest value is: ', dataset['adr'].min())
# The lowest value is :  -6.38

# normalize price per night (adr):
data_top10['adr_pp'] = (data_top10['adr'] / data_top10['total_guests'])

# only actual guests
data_top10_guests = data_top10.loc[data_top10['is_canceled'] == 0] # 

# price for the hotel at different months
plt.figure(figsize = (12, 8))
sns.boxplot(x = 'arrival_date_month',
            y = 'adr_pp',
            data = data_top10_guests, 
            fliersize = 0)
plt.title('Price of Room per Person per Night for Each Month (Top 10)', fontsize = 16)
plt.xlabel('Months', fontsize = 14)
plt.ylabel('Price [EUR]', fontsize = 14)
plt.xticks(rotation = 90)
plt.ylim(0, 150)
plt.show()
# Graph shows that the price per person per night differ for each month.
# Shows that there are not that much of a difference between the prices in each month


# price for the hotel at different months
plt.figure(figsize = (12, 8))
sns.boxplot(x = 'country',
            y = 'adr_pp',
            data = data_top10_guests, 
            fliersize = 0)
plt.title('Price of Room per Person per Night for Each Country (Top 10)', fontsize = 16)
plt.xlabel('Countries', fontsize = 14)
plt.ylabel('Price [EUR]', fontsize = 14)
plt.xticks(rotation = 90)
plt.ylim(0,150)
plt.show()
print('Graph shows that there is just a small difference in price between country.')
print('Although, in a previous graph, we saw that there were more cancelations and no-shows in Portugal')
print('than any other country, it is clear that the price is not the reason why.')


data_top10_guests.groupby('country')['adr_pp'].describe()

# =============================================================================
# Examining Different Meal Plans on Reservation Status
# =============================================================================
data_top10['meal'].value_counts()
#BB           77824
#HB           13297
#SC            7781
#Undefined     1115
#FB             783
#Name: meal, dtype: int64


# Drawing a pie chart
fig = plt.figure(figsize = (20,10))
labels = data_top10['meal'].value_counts().index.tolist()
sizes = data_top10['meal'].value_counts().tolist()
plt.pie(sizes, labels = labels, autopct = '%1.1f%%',
        shadow = False, startangle = 30)
plt.title('The Breakdown of different types of hotels', fontdict=None, position= [0.48,1], size = 'xx-large')
plt.show()
# BB    77.2%
# HB    13.2%
# SC    7.7%
# Undefined    1.1%
# FB    0.8%


# creating a graph based on Top 10 and Reservation Status
reservation_meals = data_top10.groupby(['reservation_status','meal']).lead_time.count()

# shows the table
print(reservation_meals)

# creates a graph
plt.figure(figsize = (12, 8))
sns.barplot(x = 'meal', y = 'lead_time', hue = 'reservation_status', data = reservation_meals.reset_index(), palette = ['red', 'green', 'orange'])
plt.title('Breakdown of Reservation Status by Meal Type', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Meal Type', fontsize = 14)
L=plt.legend()
L.get_texts()[0].set_text('Canceled')
L.get_texts()[1].set_text('Check-Out')
L.get_texts()[2].set_text('No-Show')
plt.show()


# =============================================================================
# Checking whether the Reserved Room and Assigned Room Match via Boolean
# =============================================================================
# Checking unique valuables in each category
data_top10['reserved_room_type'].unique()
# 'C' 'A' 'D' 'E' 'G' 'F' 'H' 'L' 'P' 'B'

data_top10['assigned_room_type'].unique()
# 'C' 'A' 'D' 'E' 'G' 'F' 'I' 'B' 'H' 'P' 'L' 'K'

# Extending lables in reserved_room_type for the boolean to work
data_top10['reserved_room_type'] = data_top10['reserved_room_type'].cat.set_categories(['C', 'A', 'D', 'E', 'G', 'F', 'I', 'B', 'H', 'P', 'L', 'K'])

# checking which reservations were assigned a different room type
data_top10['data_boolean'] = data_top10['reserved_room_type'] == data_top10['assigned_room_type']

#checking the boolean worked
print(data_top10['data_boolean'])

# Counting boolean
data_top10.data_boolean.value_counts()
#True     88010
#False    12790
#Name: data_boolean, dtype: int64

fig = plt.figure(figsize = (20,10))
labels = data_top10['data_boolean'].value_counts().index.tolist()
sizes = data_top10['data_boolean'].value_counts().tolist()
plt.pie(sizes, labels = labels, autopct = '%1.1f%%',
        shadow = False, startangle =30)
plt.title('Matching the Reserved Room and Assigned Room', fontdict = None, position= [0.48,1], size = 'xx-large')
plt.show()
# True: 87.3%
# False: 12.7%


#Creating a graph for the boolean
boolean_countries = data_top10.groupby(['country','data_boolean']).lead_time.count()

#print table 
print(boolean_countries)

# draw a graph
plt.figure(figsize = (12, 8))
sns.barplot(x = 'country', y = 'lead_time', hue = 'data_boolean', data = boolean_countries.reset_index(), palette = ['red', 'green'])
plt.title('Matching Expectations and Reality by Country', fontsize = 14)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Top 10 Countries', fontsize = 14)
L=plt.legend()
L.get_texts()[0].set_text('Mismatch')
L.get_texts()[1].set_text('Match')
print('This graph examines whether the reserved room and assigned room matched.')

# =============================================================================
# Checking whether there are repeated cancelations
# =============================================================================
data_top10['previous_cancellations'].unique()
# array([ 0, 13,  1, 11,  2,  3, 26, 25,  4, 24, 19,  5, 21,  6, 14],
#      dtype=int64)

## Using previous made functions
# all_cancelations  = data_top10[data_top10['reservation_status'].isin(['Canceled', 'No-Show'])]
# all_cancelations['previous_cancellations'].value_counts()



#creates graph
plt.figure(figsize = (12, 8))
sns.countplot(x = 'previous_cancellations', data = previous_cancel, palette = 'terrain', 
              order = all_cancelations['previous_cancellations'].value_counts().index)
plt.xticks(rotation = 90)
plt.title('Number of Previous Cancellations', fontsize = 16)
plt.ylabel('count', fontsize = 14)
plt.xlabel('Number of Previous Cancellations', fontsize = 14)
plt.show()


previous_cancel = all_cancelations[all_cancelations['previous_cancellations'] > 1]


# =============================================================================
# Save the Dataset in a new CSV as we have new columns 
# (total_number_nights, total_people, adr_pp and data_boolean)
# =============================================================================
data_top10.to_csv('data_top10.csv')