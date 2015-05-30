import json
from urllib2 import urlopen  # python 2 syntax

from flask import Flask
import pygal
from pygal.style import DarkSolarizedStyle
# http://www.blog.pythonlibrary.org/2015/04/16/using-pygal-graphs-in-flask/

# from urllib.request import urlopen # python 3 syntax
app = Flask(__name__)
 
#----------------------------------------------------------------------
@app.route('/get')
def get_weather_data(date='20140415', state='IA', city='Ames'):
    """
    Date must be in YYYYMMDD
    """
#     api_key = 'API_KEY'
#     url = 'http://api.wunderground.com/api/{key}/history_{date}/q/{state}/{city}.json'
#     new_url = url.format(key=api_key,
#                          date=date,
#                          state=state,
#                          city=city)
#     result = urlopen(new_url)
#     js_string = result.read()
#     parsed = json.loads(js_string)
#     history = parsed['history']['observations']
#  
#     imp_temps = [float(i['tempi']) for i in history]
#     times = ['%s:%s' % (i['utcdate']['hour'], i['utcdate']['min']) for i in history]
 
    # create a bar chart
    title = 'Temps for %s, %s on %s' % (city, state, date)
    #bar_chart.render()
#     bar_chart = pygal.Bar(width=1200, height=600,
#                           explicit_size=True, title=title, style=DarkSolarizedStyle)
#     # bar_chart = pygal.StackedLine(width=1200, height=600,
#     #                      explicit_size=True, title=title, fill=True)
#  
#     bar_chart.x_labels = times
#     bar_chart.add('Temps in F', imp_temps)
    data = [
      ["Python", 30.3],
      ["Java", 22.2],
      ["C++", 13],
      ["Ruby", 10.6],
      ["Javascript", 5.2],
      ["C#", 5],
      ["C", 4.1],
      ["PHP", 3.3],
      ["Perl", 1.6],
      ["Go", 1.5],
      ["Haskell", 1.2],
      ["Scala", 1],
      ["Objective-C", 0.4],
      ["Clojure", 0.2],
      ["Bash", 0.1],
      ["Lua", 0.04],
      ["TCL", 0.03]
    ]
        

    # Make a Pygal chart
    pie_chart = pygal.Pie()
    
    # add a title
    pie_chart.title = "CodeEval Most Popular Coding Languages of 2014"
    
    # add the data
    for label, data_points in data:
        pie_chart.add(label, data_points)
    
    html = """
        <html>
             <head>
                  <title>%s</title>
             </head>
              <body>
                 %s
             </body>
        </html>
        """ % (title,  pie_chart.render())
    return html
 
@app.route('/')
def hello():
    return "<a href=\"/get\">Hello World!</a>"
 
#----------------------------------------------------------------------
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=13000)
