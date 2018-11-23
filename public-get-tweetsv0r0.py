import matplotlib.pyplot as plt
import sys
from textblob import TextBlob
import time
import twitter
reload(sys)
sys.setdefaultencoding('utf8')

tweeter = api.GetUser(screen_name=sys.argv[1]).screen_name
#pageNumber = int(sys.argv[2])
tweetLog = open(tweeter + "-tweet-log.txt","a")
timeLog= open(tweeter + "-time-log.txt","a")
idLog = open(tweeter + "-id-log.txt","a")

oldId = 1064897063870033922-1
rangeLength = int(sys.argv[2])
if(rangeLength > 199):
    print "rangeLength needs to be between 1-199 doofus!"
    rangeLength = raw_input("Enter the right rangeLength ding dong: ")
rangeLength = int(rangeLength)

timer = bool(sys.argv[3] == 'True')
sleepCounter = 0
if(timer):
    sleepCounter = 900
print sys.argv[3]
print bool(sys.argv[3] == 'True')
print timer

timerIterations = int(sys.argv[4])

for i in range(timerIterations):
    for j in range(rangeLength):
        currentTweet = api.GetUserTimeline(screen_name=tweeter, max_id=oldId, count=1)
        tweetLog.write(currentTweet[0].full_text + "\n")
        timeLog.write(currentTweet[0].created_at + "\n")
        timeLog.write(str(currentTweet[0].id) + "\n")
        
        oldId = int(currentTweet[0].id) - 1
        print oldId
        print currentTweet[0].full_text

    #print sleepCounter
    #time.sleep(sleepCounter)

tweetLog.close()
timeLog.close()
idLog.close()
