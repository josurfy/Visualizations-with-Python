
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021
@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
#%% data
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)
#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
1. Have a thoughtful title
2. Have clearly labelled axes
3. Be legible
4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''
#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''
#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''
#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes
(https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/
bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''
#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''

#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''

highlight='Salt Lake' #set highlight equal it Salt Lake county

plt.figure(figsize=(10,5)) 

#define the dataframe by selecting and filtering data for Utah and grouping by the county (aka. Admin2)
df = pd.melt(covid_df[covid_df['Province_State'] == 'Utah'].drop(['iso2', 'iso3', 'code3', 'FIPS', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'], axis=1), id_vars=['Admin2'])
for Admin2, group in df.groupby('Admin2'):
    if Admin2 == highlight:
        plt.plot(group['variable'], group['value'], label=Admin2, color='yellow', linewidth=0.5)
    else:
        plt.plot(group['variable'], group['value'], label=Admin2, color='lightgray', alpha=0.5)    

#plot formatting, title, x and y axis labels and ticks and show plot
plt.title('Time Series of COVID-19 Cases by County in Utah, USA - Utah County Highlighted')
plt.xlabel('Date')
plt.xticks(group['variable'][::75], rotation=60)
plt.ylabel('Case Count')
plt.legend([highlight] )
print("VIZ 1.")
plt.show()

#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''

plt.figure(figsize=(10,5))

#define dataframe by selecting data for Utah and Florida and using groupby to select the county with the most COVID cases
df = covid_df[covid_df['Province_State'].isin(['Utah','Florida'])][['Province_State','Admin2','Combined_Key','3/9/23']]
df.loc[df.groupby('Province_State')['3/9/23'].idxmax()].plot(kind='bar', x='Combined_Key', y='3/9/23')

#plot formatting, title, x and y axis, and show plot
plt.title('Comparison Bettween Counties in FL and UT with the Most COVID-19 Cases')
plt.xlabel('County and State')
plt.ylabel('Count of COVID-19 Cases')
print("VIZ 2.")
plt.show()

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes
(https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''

#define the data frame by selecting Salt Lake County in Utah and reparamterizing the values for each date as the change in cases rather than than the total number of cases.
df = pd.melt(covid_df[(covid_df['Province_State'] == 'Utah') & (covid_df['Admin2'] == 'Salt Lake')].drop(['iso2', 'iso3', 'code3', 'FIPS', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'], axis=1), id_vars=['Admin2'])
df['change'] = df.groupby('Admin2')['value'].diff()
  
fig, ax1 = plt.subplots(figsize=(10,5))

#set plot parameters for the cumulative cases in SL county
ax1.plot(df['variable'], df['value'], label='Total Cases', color='skyblue')
ax1.set_ylabel('Total Cases')
ax1.set_xlabel('Date')

#set plot parameters for the change in cases in SL county
ax2 = ax1.twinx()
ax2.plot(df['variable'], df['change'], label=['Daily Cases'], color='orange')
ax2.set_ylabel('Daily Cases')

#create a legend with
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

#format plot, add title, format x axis and show plot
plt.title('Time Series of Total and Daily COVID-19 Cases in Salt Lake County, Utah, USA')
ax1.set_xticks(df['variable'][::75])
ax1.tick_params(axis='x', labelrotation=60)
print("VIZ 3.")
plt.show()

#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/
bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''

import numpy as np

#define the dataframe by merging 2 dataframes, one to select data from the state sum the total and the other being the original covid_df. Also creates a new column to show %case contributions for each county
state_total_df = covid_df.groupby('Province_State')['3/9/23'].sum().reset_index().rename(columns={'3/9/23': 'State_Total'})
filt_covid_df = covid_df[['Province_State', 'Admin2', '3/9/23']].rename(columns={'3/9/23': 'County_Total', 'Admin2': 'County'})
df = filt_covid_df.merge(state_total_df, on='Province_State', how='left')
df['%'] = df['County_Total']/df['State_Total']*100

#creates a list for each state in the plot (UT and AZ)
utah = tuple(df[df['Province_State'] == 'Utah']['Province_State'].unique().tolist())
arizona = tuple(df[df['Province_State'] == 'Arizona']['Province_State'].unique().tolist())

#creates a dictionary for the county % contributions for UT and AZ
upercent = df[df['Province_State'] == 'Utah'].set_index('County')['%'].to_dict()
apercent = df[df['Province_State'] == 'Arizona'].set_index('County')['%'].to_dict()

#width parameter, this comes from the matplotlib example
width = 0.5

fig, ax = plt.subplots()

#sets the bottom value equal to zero so that the bar plots begin at the y=0 level. Also plot parameters for the Utah bar chart.
bottom = np.zeros(1)
for boolean, upercent in upercent.items():
    p = ax.bar(utah, upercent, width, label=boolean, bottom=bottom)
    bottom += upercent

#resets the bottom value equal to zero so that the bar plots begin at the y=0 level. Also plot parameters for the Arizona bar chart.
bottom = np.zeros(1)
for boolean, apercent in apercent.items():
    p = ax.bar(arizona, apercent, width, label=boolean, bottom=bottom)
    bottom += apercent

#plot formatting and show plot.
ax.set_title('County Contributions (%) for Total COVID-19 Cases in Utah, USA and Arizona, USA')
ax.set_ylabel('Percent (%)')
plt.tight_layout()
print("VIZ 4.")
plt.show()
