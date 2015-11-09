# get the driving time between two locations
import json, urllib
import time
import os

home = "Bethesda, MD"
work = "McLean, VA"

def get_driving_time(origin, destination):
#    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN".format(origin,destination)
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&key=AIzaSyDxt1id7vqW3jxOb1V6X6FO5jG5s3cjsrc".format(origin,destination)
    result= json.load(urllib.urlopen(url))
    #print result
    driving_time = result['rows'][0]['elements'][0]['duration']['value']
    return driving_time/60.0
        
driving_time = 40
while driving_time > 30: 
    driving_time = get_driving_time(work, home)
    print "\nCurrent driving time is: \t", int(driving_time), " mins"
    time.sleep(60*.05) # the API limit is 2,500 per day, so be nice
       
os.system('say "Road is clear. It is time to go home!"')
print('\a')
