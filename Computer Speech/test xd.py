Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = ['jay', 'alex', 'tom']
>>> [x for x in a]
['jay', 'alex', 'tom']
>>> [jay for x in a]

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    [jay for x in a]
NameError: name 'jay' is not defined
>>> [x for jay in a]
['jay', 'jay', 'jay']
>>> [x for jaysss in a]
['jay', 'jay', 'jay']
>>> [x for alex in a]
['jay', 'jay', 'jay']
>>> a.insert(1, 'brad')
>>> a
['jay', 'brad', 'alex', 'tom']
>>> ['brad' for x in a]
['brad', 'brad', 'brad', 'brad']
>>> [x for b in a]
['tom', 'tom', 'tom', 'tom']
>>> x = 0
>>> b = 0
>>> [x for b in a]
[0, 0, 0, 0]
>>> ================================ RESTART ================================
>>> a = ['bunny', 'yom', 'zee']
>>> [ x for x in a if x =='yom':
  
SyntaxError: invalid syntax
>>> [ x for x in a if x =='yom']
['yom']
>>> a.append('yom')
>>> a
['bunny', 'yom', 'zee', 'yom']
>>> [ x for x in a if x =='yom']
['yom', 'yom']
>>> [ x for x in a if x =='yoms']
[]
>>> b  = a[:]
>>> c = [1,2,3,4]
>>> [x+1 for x in c]
[2, 3, 4, 5]
>>> x+1 for x in c
SyntaxError: invalid syntax
>>> 
