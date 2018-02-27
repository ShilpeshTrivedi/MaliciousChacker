from cybercrimetracker.cybercrimeTrackerAPI import cybercrimeTrackerAPI
import sys
import json
import time

print '\n\n'
print '\t*********************************'
print '\t* |\ /|         .-              *'      
print '\t* | v |        (                *'
print '\t* |   |alicious `-hecker        *'
print '\t*                               *'
print '\t* \tAuther @ShilpeshTrivedi *'
print '\t*********************************'
print '\n\n'

try:
    file_open = raw_input(' Enter File Name: - ')
    take=open(file_open,'r')
    print '\n'
    file = open('cybercrime-tracker.net.csv','a') 
    file.write('URL,Signature')
    file.write('\n')
    for lists in take:
        try:
            query = ''.join(lists.splitlines())
            temp=json.dumps(cybercrimeTrackerAPI().search(query))
        
            try:
                time.sleep(1)
                print ' [+] '+query + " Found As -> " + json.dumps(cybercrimeTrackerAPI().search(query)[0]['type'])
                file.write(query+','+json.dumps(cybercrimeTrackerAPI().search(query)[0]['type']))
                file.write('\n')
            except:
                print ' [-] '+query + " is not found on cybercrime-tracker.net :("
                file.write(query+',No Result Found')
                file.write('\n')
        except KeyboardInterrupt:
            print "\n Program hasbeen halted Ctrl + C Pressed"
            print '\n\n Open cybercrime-tracker.net.csv file for result'
            exit()
    file.close()
    print '\n\n Open cybercrime-tracker.net.csv file for result'
except IOError:
    print '\nThere is no file like '+ file_open

