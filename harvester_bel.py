'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "N9QcAaqvVL1cwIF4zVdL5z5YT"
csecret = "46rgLrkgAVHFHL5D8KR6iMOOB6SemUXEal0DdZjukCvb96Gpqy"
atoken = "1012062494737747970-8waKLtXj0OZLAIzMPdROAp5zDvoZqa"
asecret = "gLQYinHbOTsd8IidUoeLE1NLWoa17cw9qjnBpuSRBqdcX"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 
 
#if len(sys.argv)!=3:
#    sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
#    sys.exit()
 
#URL = sys.argv[1]
#db_name = sys.argv[2]
URL = 'localhost' 
db_name = 'belgicat'
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
 
twitterStream.filter(locations=[2.27,49.49,6.58,51.87])  #belgica
