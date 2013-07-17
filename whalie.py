from threading import Thread
from functools import wraps
import sys
import re
import time

def halieise():
    source = sys.argv[0]
    code = open(source).read()
    code = re.sub('(import whalie)|(.+\.halieise.+)', '', code)
    exec(code)
    sys.exit()

def async(func, *args, **kwargs):
    @wraps(func)
    def async_func(*args, **kwargs):
        f = Thread(target = func,
                   args = args,
                   kwargs = kwargs)
        f.start()
        return f
    return lambda: async_func(*args, **kwargs)

def check_if_done(f, done):
    res = f()
    done.append(1)
    return res

if __name__ == '__main__':
    '''
    whalie long_operation():
        print 'sleeping for a bit'
        time.sleep(0.5)
'''

    def long_operation(*args, **kwargs):
        print '>>>>>>'
        time.sleep(2)
        print '>>>>>> done'

    def loop():
        x = 0
        r = []
        f = async(lambda: check_if_done(lambda: long_operation(23, do=23), r))
        f()
        while not r:
            x += 1
            time.sleep(0.1)
            print 'sleeping for a bit'
    loop()
