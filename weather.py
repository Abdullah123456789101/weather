# https://github.com/meteostat/meteostat-python?tab=readme-ov-file
# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
import pandas as pd

place_df = pd.read_csv("place.csv")

coordinates = list(zip(place_df['latitude'], place_df['longtitude'], place_df['altitude']))

yearStart = int(input("Start årstal: "))
monthStart=int(input("Start måned: "))
dayStart=int(input("Start dag: "))

yearEnd = int(input("Slut årstal: "))
monthEnd=int(input("Slut måned: "))
dayEnd=int(input("Slut dag: "))
# Set time period
start = datetime(yearStart, monthStart, dayStart)
end = datetime(yearEnd, monthEnd, dayEnd)

# Create Point from coordinates in csv file
location = Point=coordinates

# Get daily data from date interval
data = Daily(location,start,end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()
