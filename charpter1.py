# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Simple Statistics of California, 2010, CO, data

# <rawcell>


# <codecell>

from pandas import DataFrame,Series
import pandas as pd
import matplotlib.pylab as plt
import csv
path = '/Users/mengfantang/Desktop/PredictiveES/data/EPA_daily/CO_CA_2010.csv'
with open(path,'rb') as csvfile:
    file_reader = csv.reader(csvfile)
    records = [ row for row in file_reader]
frame = pd.read_csv(path)
frame

# <codecell>

frame['AQS_SITE_ID'].value_counts()
# the complete record should be the number of the days, 365. Missing value at each station.

# <codecell>

frame['Daily Max 8-hour CO Concentration'].value_counts().plot(kind = "bar")
plt.show()
# distribution of CO concentration of max 8 hour

# <codecell>

frame['DAILY_AQI_VALUE'].value_counts().plot(kind = "bar")
plt.show()
# daily aqi distribution

# <codecell>

frame['PERCENT_COMPLETE'].value_counts().plot(kind = "bar")
plt.show()
frame['PERCENT_COMPLETE'].value_counts()

# 

# <codecell>


