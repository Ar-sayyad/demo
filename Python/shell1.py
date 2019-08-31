Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> items=["bread","pasta","fruits","chips"]
>>> items
['bread', 'pasta', 'fruits', 'chips']
>>> food=["bread","pasta","fruits"]
>>> bathroom=["shampoo","soap"]
>>> items=food+bathroom
>>> items
['bread', 'pasta', 'fruits', 'shampoo', 'soap']
>>> food
['bread', 'pasta', 'fruits']
>>> len(items)
5
>>> "bread" in items
True
>>> "soda" in items
False
>>> 
=============================== RESTART: Shell ===============================
>>> 4==4
True
>>> 4!=5
True
>>> 4!=4
False
>>> 2>3
False
>>> 2>1
True
>>> 2>=2
True
>>> 
>>> 
>>> 3>2 and 4>1
True
>>> 32>23 or 4>2
True
>>> 12>15 or 1>0
True
>>> 12>15 or 2>3
False
>>> exp = [2340,2500,2100,3100,2980]
>>> exp
[2340, 2500, 2100, 3100, 2980]
>>> 
>>> 
>>> 
>>> d={"tom":1235648955,"rob":2356465633,"joe":3546821344}
>>> d
{'tom': 1235648955, 'rob': 2356465633, 'joe': 3546821344}
>>> d["tom"]
1235648955
>>> d["sa"]=55468656565
>>> d
{'tom': 1235648955, 'rob': 2356465633, 'joe': 3546821344, 'sa': 55468656565}
>>> d
{'tom': 1235648955, 'rob': 2356465633, 'joe': 3546821344, 'sa': 55468656565}
>>> del d["sa"]
>>> d
{'tom': 1235648955, 'rob': 2356465633, 'joe': 3546821344}
>>> for key in d
SyntaxError: invalid syntax
>>> for key in d:
	print("key:",key,"value:",d[key])

	
key: tom value: 1235648955
key: rob value: 2356465633
key: joe value: 3546821344
>>> for k,v in d.items();
SyntaxError: invalid syntax
>>> for k,v in d.items():
	print("key:",key,"value:",v)

	
key: joe value: 1235648955
key: joe value: 2356465633
key: joe value: 3546821344
>>> 
>>> 
>>> "tom" in d
True
>>> d
{'tom': 1235648955, 'rob': 2356465633, 'joe': 3546821344}
>>> 
d
{'tom': 1235648955, 'rob': 2356465633, 'joe': 3546821344}
>>> 
>>> d.clear()
>>> d
{}
>>> point = (5,9)
>>> point[0]
5
>>> point[1]
9
>>> point[0]=50
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    point[0]=50
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 

>>> 
>>> import math
>>> math.sqrt(16)
4.0
>>> math.pow(2,5)
32.0
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.pi
3.141592653589793
>>> math.log10(100)
2.0
>>> math.log10(1000)
3.0
>>> math.floor(2.5)
2
>>> 
>>> 
>>> 
>>> import calender
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> import calendar
>>> cal = calendar.month(2019,6)
>>> print(cal)
     June 2019
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30

>>> calendar.islear(2019)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    calendar.islear(2019)
AttributeError: module 'calendar' has no attribute 'islear'
>>> calendar.isleap(2019)
False
>>> dir(calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthlen', 'monthrange', 'nextmonth', 'prcal', 'prevmonth', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
>>> 
=============================== RESTART: Shell ===============================
>>> f = open("d://Python//data//book.txt","r")
>>> s=f.read()
>>> s
'{"tom": {"name": "tom", "address": "1 red street, NY", "phone": 9856263256}, "bob": {"name": "bob", "address": "1 green street, NY", "phone": 8855220124}}'
>>> import json
>>> json.loads(s)
{'tom': {'name': 'tom', 'address': '1 red street, NY', 'phone': 9856263256}, 'bob': {'name': 'bob', 'address': '1 green street, NY', 'phone': 8855220124}}
>>> book=json.loads(s)
>>> book
{'tom': {'name': 'tom', 'address': '1 red street, NY', 'phone': 9856263256}, 'bob': {'name': 'bob', 'address': '1 green street, NY', 'phone': 8855220124}}
>>> type(book)
<class 'dict'>
>>> book['bob]
	 
SyntaxError: EOL while scanning string literal
>>> book['bob']
	 
{'name': 'bob', 'address': '1 green street, NY', 'phone': 8855220124}
>>> book['bob']['phone']
	 
8855220124
>>> for person in book:
	 print(book[person])

	 
{'name': 'tom', 'address': '1 red street, NY', 'phone': 9856263256}
{'name': 'bob', 'address': '1 green street, NY', 'phone': 8855220124}
>>> 
=============================== RESTART: Shell ===============================
>>> __name__
	 
'__main__'
>>> 
=============================== RESTART: Shell ===============================
>>> 

>>> 'abc'+2
	 
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    'abc'+2
TypeError: can only concatenate str (not "int") to str
>>> 
=============================== RESTART: Shell ===============================
>>> a = ["hey","bro","you'r","awesome"]
	 
>>> for i in a
	 
SyntaxError: invalid syntax
>>> for i in a:
	 print(i)

	 
hey
bro
you'r
awesome
>>> dir(a)
	 
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> itr = iter(a)
	 
>>> itr
	 
<list_iterator object at 0x03B8D470>
>>> next(itr)
	 
'hey'
>>> itr = reversed(a)
	 
>>> next(itr)
	 
'awesome'
>>> next(itr)
	 
"you'r"
>>> 
=============================== RESTART: Shell ===============================
>>> def remote_control_next():
	 yield "CNN"
	 yield "ESPN"

	 
>>> itr = remote_control_next()
	 
>>> itr
	 
<generator object remote_control_next at 0x037F9270>
>>> next(itr)
	 
'CNN'
>>> next(itr)
	 
'ESPN'
>>> for c in remote_control_next():
	 print(c)

	 
CNN
ESPN
>>> 
=============================== RESTART: Shell ===============================
>>> numbers = [1,2,3,4,5,6,7,8,9]
	 
>>> even=[]
	 
>>> for i in numbers:
	 if i%2==0:
		 even.append(i)

	 
>>> even
	 
[2, 4, 6, 8]
>>> even = [i for i in numbers if i%2==0]
	 
>>> even
	 
[2, 4, 6, 8]
>>> sqres = [i*i for i in numbers]
	 
>>> sqres
	 
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
	 
>>> 
	 
>>> s = set([1,2,3,4,2,5,3,1,2])
	 
>>> s
	 
{1, 2, 3, 4, 5}
>>> even ={i for i in numbers if i%2==0}
	 
>>> even
	 
{8, 2, 4, 6}
>>> even ={i for i in s if i%2==0}
	 
>>> even
	 
{2, 4}
>>> 
=============================== RESTART: Shell ===============================
>>> cities ["mumbai","newyork","paris"]
	 
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    cities ["mumbai","newyork","paris"]
NameError: name 'cities' is not defined
>>> cities =["mumbai","newyork","paris"]
	 
>>> countries = ["India","USA","France"]
	 
>>> z=zip(cities,countries)
	 
>>> z
	 
<zip object at 0x03295B48>
>>> for a in z:
	 print(a)

	 
('mumbai', 'India')
('newyork', 'USA')
('paris', 'France')
>>> d = {city:country for city, country in zip(cities,countries)}
	 
>>> d
	 
{'mumbai': 'India', 'newyork': 'USA', 'paris': 'France'}
>>> 
=============================== RESTART: Shell ===============================
>>> #sets
	 
>>> basket = {"orange","apple","mango","apple","orange"}
	 
>>> type(basket)
	 
<class 'set'>
>>> basket
	 
{'orange', 'mango', 'apple'}
>>> a = set()
	 
>>> a.add("mango")
	 
>>> a.add("tomato")
	 
>>> a
	 
{'tomato', 'mango'}
>>> a={}
	 
>>> a
	 
{}
>>> type(a)
	 
<class 'dict'>
>>> a={"mango"}
	 
>>> type(a)
	 
<class 'set'>
>>> basket[0]
	 
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    basket[0]
TypeError: 'set' object does not support indexing
>>> a[0]
	 
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    a[0]
TypeError: 'set' object does not support indexing
>>> 
	 
>>> numbers=[1,2,3,45,6,8,5,1,2,3]
	 
>>> unique_numbers=set(numbers)
	 
>>> unique_numbers
	 
{1, 2, 3, 5, 6, 8, 45}
>>> unique_numbers.add(77)
	 
>>> unique_numbers
	 
{1, 2, 3, 5, 6, 8, 45, 77}
>>> fs = frozenset(numbers)
	 
>>> fs
	 
frozenset({1, 2, 3, 5, 6, 8, 45})
>>> fs.add(55)
	 
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    fs.add(55)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 

>>> x= {"a","b","c"}
	 
>>> "a" in x
	 
True
>>> for i in x
	 
SyntaxError: invalid syntax
>>> for i in x:
	 print(i)

	 
b
a
c
>>> y={"a","g","h"}
	 
>>> x
	 
{'b', 'a', 'c'}
>>> y
	 
{'a', 'g', 'h'}
>>> x|y
	 
{'b', 'a', 'g', 'h', 'c'}
>>> x&y
	 
{'a'}
>>> x-y
	 
{'b', 'c'}
>>> x<y
	 
False
>>> x={"h","g"}
	 
>>> x<y
	 
True
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy as np
	 
>>> a = np.array([1,2,3])
	 
>>> a
	 
array([1, 2, 3])
>>> a[0]
	 
1
>>> a1=np.array([1,2,3])
	 
>>> a2=np.array([4,5,6])
	 
>>> a1+a2
	 
array([5, 7, 9])
>>> a2-a1
	 
array([3, 3, 3])
>>> a1*a2
	 
array([ 4, 10, 18])
>>> array([ 4, 10, 18])
	 
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    array([ 4, 10, 18])
NameError: name 'array' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy as np
	 
>>> a =np.array([5,6,7])
	 
>>> a[0]
	 
5
>>> a=np.array([1,2],[3,4],[5,6])
	 
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    a=np.array([1,2],[3,4],[5,6])
ValueError: only 2 non-keyword arguments accepted
>>> a=np.array([[1,2],[3,4],[5,6]])
	 
>>> a.ndim
	 
2
>>> a.itemsize
	 
4
>>> a.dtype
	 
dtype('int32')
>>> a=np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
	 
>>> a
	 
array([[1., 2.],
       [3., 4.],
       [5., 6.]])
>>> 
	 
>>> 
	 
>>> 
	 
>>> 
	 
>>> a.size
	 
6
>>> a
	 
array([[1., 2.],
       [3., 4.],
       [5., 6.]])
>>> a.shape
	 
(3, 2)
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy as np
	 
>>> np.zeros((3,4))
	 
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones(4,3))
SyntaxError: invalid syntax
>>> np.ones((4,3))
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
>>> l=range(5)
>>> l
range(0, 5)
>>> np.arange(0,5)
array([0, 1, 2, 3, 4])
>>> np.arange(0,5,2)
array([0, 2, 4])
>>> 

>>> np.linspace(1,5,10)
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
>>> np.linspace(1,5,5)
array([1., 2., 3., 4., 5.])
>>> np.linspace(1,5,12)
array([1.        , 1.36363636, 1.72727273, 2.09090909, 2.45454545,
       2.81818182, 3.18181818, 3.54545455, 3.90909091, 4.27272727,
       4.63636364, 5.        ])
>>> a= np.array([[1,2],[3,4],[5,6]])
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> a.reshape(2,3)
array([[1, 2, 3],
       [4, 5, 6]])
>>> a.reshape(6,3)
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    a.reshape(6,3)
ValueError: cannot reshape array of size 6 into shape (6,3)
>>> a.reshape(6,1)
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
>>> a.ravel()
array([1, 2, 3, 4, 5, 6])
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> 

>>> 
>>> 
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> a.min()
1
>>> a.max()
6
>>> a.sum()
21
>>> a.sum(axis=0)
array([ 9, 12])
>>> a.sum(axis=1)
array([ 3,  7, 11])
>>> 

>>> a.sqrt(2)
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    a.sqrt(2)
AttributeError: 'numpy.ndarray' object has no attribute 'sqrt'
>>> np.sqrt(a)
array([[1.        , 1.41421356],
       [1.73205081, 2.        ],
       [2.23606798, 2.44948974]])
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> np.std(a)
1.707825127659933
>>> 
=============================== RESTART: Shell ===============================
>>> 
import numpy as np
>>> a =np.array([[1,1],[0,1]])
>>> a
array([[1, 1],
       [0, 1]])
>>> a =np.array([[1,2],[3,4]])
>>> b =np.array([[5,6],[7,8]])
>>> a+b
array([[ 6,  8],
       [10, 12]])
>>> a_b
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    a_b
NameError: name 'a_b' is not defined
>>> a-b
array([[-4, -4],
       [-4, -4]])
>>> b-a
array([[4, 4],
       [4, 4]])
>>> a*b
array([[ 5, 12],
       [21, 32]])
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy as np
>>> n=[6,7,8]
>>> n[0:2]
[6, 7]
>>> n[-1]
8
>>> a=np.array([6,7,8])
>>> a[0:2]
array([6, 7])
>>> a[-1]
8
>>> b =np.array([[5,6,3],[7,8,9]])
>>> b
array([[5, 6, 3],
       [7, 8, 9]])
>>> a[1,2]
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    a[1,2]
IndexError: too many indices for array
>>> b[1,2]
9
>>> b[0:2,2]
array([3, 9])
>>> b[-1]
array([7, 8, 9])
>>> a[:,1:2]
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    a[:,1:2]
IndexError: too many indices for array
>>> b[:,1:2]
array([[6],
       [8]])
>>> a=np.array([[6,7,8],[1,2,3],[5,2,8]])
>>> a
array([[6, 7, 8],
       [1, 2, 3],
       [5, 2, 8]])
>>> for row in a:
	print(row)

	
[6 7 8]
[1 2 3]
[5 2 8]
>>> for cell in a.flat:
	print(cell)

	
6
7
8
1
2
3
5
2
8
>>> 
>>> 
a=
SyntaxError: invalid syntax
>>> 
>>> a=np.arange(6).reshape(3,2)
>>> b=np.arange(6,12).reshape(3,2)
>>> a
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> b
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
>>> np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
>>> np.vstack(a,b)
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    np.vstack(a,b)
TypeError: vstack() takes 1 positional argument but 2 were given
>>> np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
>>> np.hstack((a,b))
array([[ 0,  1,  6,  7],
       [ 2,  3,  8,  9],
       [ 4,  5, 10, 11]])
>>> 

>>> 
>>> a=np.arange(30).reshape(2,15)
>>> a
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
>>> np.hsplit(a,3)
[array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])]
>>> result=np.hsplit(a,3)
>>> result[0]
array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]])
>>> result[2]
array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])
>>> r=np.vsplit(a,2)
>>> r[0]
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])
>>> r[1]
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
>>> 

>>> 
>>> a=np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b=a>4
>>> b
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> b=a > 4
>>> b
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> a[b]
array([ 5,  6,  7,  8,  9, 10, 11])
>>> a[b]=-1
>>> a
array([[ 0,  1,  2,  3],
       [ 4, -1, -1, -1],
       [-1, -1, -1, -1]])
>>> 
=============================== RESTART: Shell ===============================
>>> import pandas
>>> 
>>> conda env list
SyntaxError: invalid syntax
>>> 
