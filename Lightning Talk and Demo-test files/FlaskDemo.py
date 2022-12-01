import flask
import time

from Rack import Rack

app = flask.Flask(__name__)


def formateBayData(rack):
    rack1 = Rack()
    rack1.update_rack({0:True, 1:True})
    
    bayLocation = []
    status = []
    for bays in rack1.bays.items():
        
        bayLocation.append(bays[0] + 1)
        # print (bayLocation)
        
        if bays[1] == True:
            status.append("Bay is Full")
        if bays[1] == False:
            status.append("Bay is Empty")
            
    
    # status = rack1.bays.values()
    # bays = rack1.bays.keys()
    
    dataForHTML = [bayLocation,status]
    
    return dataForHTML



@app.route('/')
def home():
  
    
    return flask.render_template("Home.html")

@app.route('/rack1')
def rack1():

     information = formateBayData(rack1)
     return flask.render_template("rack1.html", headings = information[0], data = information[1])
    # return


if __name__ == '__main__':
    
    
    app.run(use_reloader = False, debug = True)

