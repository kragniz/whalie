import time
import whalie
whalie.halieise()

def long_thing():
    print 'starting long thing'
    time.sleep(4)
    print 'ended long thing'

while long_thing():
    time.sleep(0.5)
    print 'doing something'

print 'ended program'
