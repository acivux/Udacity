__author__ = 'jannie.vanniekerk'

from media import Movie
import inspect

class_name = Movie.__name__
module_name = Movie.__module__
methods = "\r\n\t".join([str(x[0]+" - "+x[1].__doc__) for x in inspect.getmembers(Movie, inspect.ismethod)])

say_hello = """
Hello,

My name is """+class_name+""".
I am a class living in a module called '"""+module_name+"""', which is a Python file called """+module_name+""".py.

I contain the following methods:
	"""+methods+"""\r\n\r\nGood bye!"""

print say_hello


