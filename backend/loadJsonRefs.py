import json
import sys
import pymongo

def processRefs():
    # Connect to mongo
    connect = pymongo.Connection("localhost")
    db = connect.hackNYF2012
    authSuccess = db.authenticate("hackNY","hackNYF2012")
    if authSuccess == False:
        print "Could not connect to mongoDB"
        exit(0)
    else:
        print "MongoDB auth success"
    collection = db.references
    
    # Open file and insert into mongo
    f = open("references.json")
    refData = json.loads(f.read())
    refData = refData['items']
    for data in refData:
        #print data
        collection.insert(data)
    
    #test = {'test': 'test'}
    #collection.insert(test)
    # shows back the test 
    #collection.find_one()

# It refuses to auto execute... I have no fucking clue why...
# Just run inside python instead
def main():
    print "in main"
    processRefs()
    print "finished process refs"