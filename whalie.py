from threading import Thread
from functools import wraps
import sys
import re
import time
import hashlib

def halieise():
    source = sys.argv[0]
    code = open(source).read()
    code = re.sub('(.+\.halieise.+)', '', code)
    code = convert_loops(code)
    with open('out.py', 'w') as f:
        f.write(code)
    exec(code)
    sys.exit()

def a(func, *args, **kwargs):
    @wraps(func)
    def async_func(*args, **kwargs):
        f = Thread(target = func,
                   args = args,
                   kwargs = kwargs)
        f.start()
        return f
    return lambda: async_func(*args, **kwargs)

def c(f, done):
    res = f()
    done.append(1)
    return res

def convert_loops(code, num=0):
    newLoop = '''{i}{r} = []
{i}whalie.a(lambda: whalie.c(lambda: {command}, {r}))()
{i}whalie!loop not {r}:
{loop}
'''
    inWhile = False
    scope = 0
    contents = []
    r = False
    for i, line in enumerate(code.split('\n')):
        s =  next((i for i, c in enumerate(line) if not c.isspace()), len(line))
        if inWhile and s < scope and not r and line.strip():
            inWhile = False
            r = True
            lines = code.split('\n')
            l = lines[:b] + \
                    newLoop.format(i=' ' * (scope-1),
                        command=c,
                        r='r'+hex(num)[2:],
                        loop='\n'.join([
                            c for c in contents[1:]
                                       ])).split('\n') + lines[i:]
        if re.match('\s*while\s+.+:', line) is not None and not inWhile and not r:
            c = line.strip()[5:-1].strip()
            inWhile = True
            scope = s+1
            b = i
            contents = []
        if inWhile:
            contents.append(line)
    if r:
        return convert_loops('\n'.join(l), num+1)
    else:
        f = '_'+hashlib.md5(code).hexdigest()
        return 'def {}():\n'.format(f) + \
               re.sub(r'whalie!loop', 'while', re.sub('^',
                                                      '    ',
                                                      code,
                                                      flags=re.M)) + \
               '\n{}()'.format(f)
