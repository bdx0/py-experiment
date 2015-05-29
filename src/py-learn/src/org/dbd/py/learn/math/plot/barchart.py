import pygal  # First import pygal

import json
import urllib2

bar_chart = pygal.Bar()
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])


# construct our API URL with type parameter set to 'alltimesum'
apiurl = 'http://mcsafetyfeed.org/api/counts.php?type=alltimesum'

# retrieve the JSON object via the API URL
data = json.load(urllib2.urlopen(apiurl))

# the count array will hold a list of daily counts, the label array will hold our x-axis labels
counts = []
labels = []

# using PyGal, create a line chart
line_chart = pygal.Line()

# iterate through the returned JSON array and pull out the counts and the incident type labels
for d in data:
    counts.append(int(d["count"]))
    labels.append(d["date"].encode("utf8"))  # PyGal no like uni-code ...

# set the title of our chart to something intelligent
line_chart.title = 'Public Safety Incidents per Day'

# set our x-axis labels, as well as the values to be shown on the graph
line_chart.x_labels = labels
line_chart.add('Total Incidents', counts)

# make sure you tip your local wizard after calling this function ....
line_chart.render_in_browser()
