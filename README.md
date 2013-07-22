#Whalie - Halie Style While Loops

*Are while loops not exotic enough for you? Have you ever felt the need to
violate python in terrible ways? Are you a mechanical engineer and have
misinterpreted what a while loop actually does and want to emulate your dreams?*

If any of those apply to you, you still shouldn't use this module.

To use whalie loops, import the module and haliese your code.

```python
import whalie
whalie.halieise()
```

Now, instead of the contents of `while` loops executing while the condition is
`True`, they will now loop only while the condition is still being calculated.

#Example

```python
#test.py
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
```

```
louis@lanaya:~/git/whalie$ python test.py 
starting long thing
doing something
doing something
doing something
doing something
doing something
doing something
doing something
ended long thing
doing something
ended program
```
