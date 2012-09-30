import urllib2
import json
import sys

def etsyAPICall(type, search):
    if type == "":
        URL = "http://openapi.etsy.com/v2/private/listings/active?&api_key=f0zll6x1q1bislf7w0dgodg4"
    else:
        URL = "http://openapi.etsy.com/v2/private/listings/active?limit=1000000&offset=0&" + type + "=" + search + "&api_key=f0zll6x1q1bislf7w0dgodg4"
    responce = urllib2.urlopen(URL)
    doc = json.loads(responce.read())
    return doc['count']

