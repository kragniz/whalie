import time
import whalie
whalie.halieise()

def long_thing():
    print 'starting long thing'
    time.sleep(10)
    print 'ended long thing'

def f():
    while long_thing():
        while another_long_thing():
            pass
        print 'doing something'
        time.sleep(0.2)

while long_thing():
    print 'doing something'
    time.sleep(0.2)

print 'ended program'
