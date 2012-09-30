import cherrypy
import urllib
import urllib2
import json
import callAPIFunctions

class Query(object):
    def index(self, api = None, type = None, search = None):
        #returnString = "Query Hello World! Requested: API=" + api + " type=" + type + " search=" + search
        #baseURL = "http://musicalrunner.orderofmagnitude.jit.su/result/?"
        #returnQueryData = urllib.urlencode(returnQuery)
        #URL = baseURL + returnQueryData
        #urllib2.urlopen(URL)
        #return returnString
        
        # We now have the api, type and search. Pass on to python api calls
        returnQuery = callAPIFunctions.findAPIType(api, type, search)
        returnQuery['api'] = api
        
        # Define return query, format in json and return to frontend
        #returnQuery = { "api" : api , "type" : type, "search" : search }
        #returnQuery = { "api" : "etsy" , "value" : 10, "factor" : 2, "comparison" : "number of people in wyoming", "comparisonValue" : 50, "image" : "http://ec2.rjehlers.com:8080/static/hackny_logo_square.png" }
        jsonData = json.dumps(returnQuery)
        return jsonData
    index.exposed = True
    
    def default(self, *args):
        return "Query -> Invalid parameters"
    default.exposed = True

class root(object):
    query = Query()
    
    def index(self, *args):
        return "Root: Hello World!"
    index.exposed = True
    
    def default(self, *args):
        raise cherrypy.HTTPRedirect("http://musicalrunner.orderofmagnitude.jit.su/",303)
        #return "Root default method"
    default.exposed = True

cherrypy.root = root()
#cherrypy.root.query = query()

cherrypy.quickstart(root(),'','config.conf')