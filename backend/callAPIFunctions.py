import process

def findAPIType(api, type, search):
    if api == "etsy":
        if type == "all":
            return process.etsyAPICall("","")
        else:
            return process.etsyAPICall(type, search)
    
    if api == "tumblr":
        return "tumblr is not implemented"
    