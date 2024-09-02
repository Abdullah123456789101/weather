# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
yearStart = int(input("Start årstal: "))
monthStart=int(input("Start måned: "))
dayStart=int(input("Start dag: "))

yearEnd = int(input("Slut årstal: "))
monthEnd=int(input("Slut måned: "))
dayEnd=int(input("Slut dag: "))
# Set time period
start = datetime(yearStart, monthStart, dayStart)
end = datetime(yearEnd, monthEnd, dayEnd)

# Create Point for Vancouver, BC
location = Point(49.2497, -123.1193, 70)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()