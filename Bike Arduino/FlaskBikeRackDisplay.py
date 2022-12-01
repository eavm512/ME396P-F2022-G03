import flask
# import time

# from Rack import Rack

app = flask.Flask(__name__)


def formateBayData(rackName):
    
    bayLocation = []
    bayStatus = []
    
    #open a file to read into memory
    f = open('rack-log.txt', 'r')
    
    #Read in the contents of the file
    contents = f.readlines()
    
    
    found = False
    
    index = 0 
    #Write a for loop to iterate 
    #through the contents of the file 
    while found == False:
        #search for rack with specific name
         #Read in the contents of the file
         firstLine = contents[0]
         # f.seek(0)
         # print("current Index:", index)
         currentLine = contents[-1-index]
         
         
         print("this is the current Line being read: ", currentLine)
         
         dividedLine = currentLine.split(";")
         
         NameOfRackOfLine = dividedLine[0]
         # print(NameOfRackOfLine)
         
         if NameOfRackOfLine == rackName:
             
             found = True
             
             
             date  = dividedLine[1].split(" ")[0]
             print("this is the Data of this rack:", date)
             
             time = dividedLine[1].split(" ")[1]
             print("this is the Time of this rack:", time, '/n')
             
             
             bayInformation = dividedLine[2]
             
             # print("this is bay information:", bayInformation)
             
             bayInformation = bayInformation.replace('{','')
             bayInformation = bayInformation.replace('}','')
             bayInformation = bayInformation.replace(' ','')
             bayInformation = bayInformation.replace('\n','')
             
             
             # print("this is bay information post Parsing:", bayInformation)
             bayInformation = bayInformation.split(",")
             
             # print("this is bay information post split:", bayInformation)
             
             
             for bay in bayInformation:
                 bayLocation.append(int(bay.split(":")[0]) + 1)
                 status = bay.split(":")[1]
                 # print (bayLocation)
                    
                 if status == 'True':
                     bayStatus.append("Bay is Full")
                 if status == 'False':
                     bayStatus.append("Bay is Empty")
         
         
         elif currentLine == firstLine:
            bayLocation = ['No bay Information Avaliable']
            bayStatus = ['No bay Information Avaliable']
            break
         else:
            index= index +1
            
         
    dataForHTML = [bayLocation,bayStatus]
    
    print ("This it the data being passed to HTML:", dataForHTML)
    return dataForHTML



@app.route('/')
def home():
  
    
    return flask.render_template("Home.html")

@app.route('/rack1')
def rack1():

     information = formateBayData('unnamed')
     return flask.render_template("rack1.html", headings = information[0], data = information[1])
    # return

@app.route('/rack2')
def rack2():

     information = formateBayData('unnamed1')
     return flask.render_template("rack2.html", headings = information[0], data = information[1])

if __name__ == '__main__':
    
    
    app.run(use_reloader = False, debug = True)

