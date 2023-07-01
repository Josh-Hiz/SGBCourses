Finding your way around
=======================

A lot of programming is experimentation: you know what you need to do in general, but you don't exactly how each of the parts will fit them together. For example, you might be writing a calendar tool and want to ask questions about how long it's been since an irregularly recurring event happened. The principle here is not hard, but you'll have to look carefully at ``datetime`` (or whatever library you're using) to determine how to execute your plan.

Exploration in the REPL is a great way to figure out what you want to do---the REPL and its libraries are a large part of why Python is such a successful language!

The first tool you need for exploratory programming is ``dir``. The ``dir`` function can tell you what's in scope, what definitions are in a module, and what methods and fields are in a class. The ``help`` function is a useful adjunct: it'll tell you more about a given definition. Here's an example session exploring the ``time`` module:

.. code-block:: 

    >>> dir()
    ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
    >>> import time
    >>> dir(time)
    ['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']
    >>> help(time.time)
    Help on built-in function time in module time:

    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.
    (END)

You can use it to explore classes, too. Recall the ``csv`` module we used when working with data.

.. code-block:: 

    >>> import csv
    >>> dir(csv)
    ['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']
    >>> help(csv.DictReader)
    Help on class DictReader in module csv:

    class DictReader(builtins.object)
        |  DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
        |  
        |  Methods defined here:
        |  
        |  __init__(self, f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
        |      Initialize self.  See help(type(self)) for accurate signature.
        |  
        |  __iter__(self)
        |  
        |  __next__(self)
        |  
        |  ----------------------------------------------------------------------
        |  Data descriptors defined here:
        |  
        |  __dict__
        |      dictionary for instance variables (if defined)
        |  
        |  __weakref__
        |      list of weak references to the object (if defined)
        |  
        |  fieldnames
    (END)
    >>> >>> d = csv.DictReader(open("/Users/mgree/cs515/hw08/nyschools.csv"))
    >>> dir(d)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_fieldnames', 'dialect', 'fieldnames', 'line_num', 'reader', 'restkey', 'restval']
    >>> d.fieldnames
    ['district', 'year', 'total', 'prek', 'kindergarten', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'asian', 'black', 'hispanic', 'multiple', 'white', 'disabilities', 'ell', 'poverty', 'eni']

Notice how we can progressively find and work with the tools we have. Once you've played around with ``dir`` and ``help``, you can stop experimenting and start trying to write your code.

The pager: navigating the help screen
-------------------------------------

When you run ``help(x)``, the Python displays the help information for ``x`` using the *pager*, a system utility for looking at text that lets you move backwards and forwards. The default pager is typically a tool called ``less``; you might enjoy `reading its documentation <https://www.man7.org/linux/man-pages/man1/less.1.html>`_. The key thing to know is that the spacebar moves you down, ``b`` moves you up, and ``q`` exits.