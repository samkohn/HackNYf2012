from temboo.Library.Twitter.Search.SearchFilter import SearchFilter
from temboo.core.session import TembooSession
import process
import pymongo
import math
import random

def findAPIType(api, type, search):
    if api == "etsy":
        if type == "all":
            returnObject = compareSize(process.etsyAPICall("",""))
            return returnObject
        else:
            returnObject = compareSize(process.etsyAPICall(type, search))
            return returnObject
    
    # govtrack
    # elif api == "govtrack":
    	# choreo = None;
    	# inputs = None;
    	
    	# if "role" in type:
    		# choreo = Role(session)
    		# inputs = choreo.new_input_set()

    		# if "party" in type:
    			# inputs.set_Party(search)
    		# elif "state" in type:
    			# inputs.set_State(search)
    	# elif type == "person/?gender":
    		# choreo = Person(session)
    		# inputs = choreo.new_input_set()
    		# inputs.set_Gender(search)
		
		# elif type == "vote_voter/?person":
			# choreo = VoteAndVoter(session)
			# inputs = choreo.new_input_set()
			# inputs.set_Person(search)
			
   		# inputs.set_Limit(5000)
   		# results = choreo.execute_with_results(inputs)
   		# count = results['meta']['total_count']
        # returnObject = compareSize(process.etsyAPICall("",""))
        # return returnObject
    
    if api == "tumblr":
        return "tumblr is not implemented"
    
def compareSize(size):
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
    
    # Find order of magnitude of the number given to the function
    if size != 0:
        sizeOOMExp = math.floor(math.log(size,10))
        sizeLowerLimit = math.pow(10, sizeOOMExp)
    else:
        sizeLowerLimit = 0
        
    # Determine which objects are the same order of magnitude
    matchedObjects = []
    for col in collection.find():
        compSize = col['comparisonValue']
        #print compSize
        if (compSize >= sizeLowerLimit) & (compSize <= sizeLowerLimit*10):
            matchedObjects = matchedObjects + [col]
        
    #print matchedObjects
    #print len(matchedObjects)
    if len(matchedObjects) != 0:
        matchedObjectIndex = random.randrange(0,len(matchedObjects))
        returnObject = matchedObjects[matchedObjectIndex]
    else:
        matchedObjectIndex = 5
        returnObject = collection.find()[matchedObjectIndex]
    
    returnObject['factor'] = float(size)/returnObject['comparisonValue']
    returnObject['value'] = size
    # print "Testing Division"
    # print returnObject['comparisonValue']
    # print size
    # print float(size)/returnObject['comparisonValue']
    # compVal = returnObject['comparisonValue']
    # print size / compVal
    # divVal = size / compVal
    # print divVal
    
    del returnObject['_id']
    print returnObject
    return returnObject