import urllib2
import re
import os
import time
 
while 1:
 
    html_content = urllib2.urlopen('http://www.updates.collegespace.in/category/results').read() 
 
    matches = re.findall('5thSem2015', html_content);  
 
 
    if len(matches) == 0: 
       os.system("notify-send 'Result not declared yet'")
       time.sleep(900)
 
    else:
       os.system("notify-send 'Result Declared'")
       quit()
