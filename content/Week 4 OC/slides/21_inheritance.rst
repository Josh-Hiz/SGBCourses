Inheritance
===========

To teach you about another testing framework for Python, we must first turn our attention to another OOP concept: **inheritance**.

In Python, every class is declared as extending some base class (except for ``object``, which has no base class). When you extend a class, your extension (the **subclass**) inherits all of the methods of the **superclass**.

To get a feel for why that might be a good thing, let's think about *logging*. It's a common activity to want to record how a program is running. While it's possible to just use ``print`` calls throughout, that ends up being brittle and hard to work with. So it makes sense to have an explicit notion of a 'logger'. Let's build a simple one:

.. runner:: 

    import time

    class Logger(object):
        def format(self, msg):
            return msg

        def emit(self, msg):
            print(msg)
        
        def log(self, msg):
            self.emit(self.format(msg))

    def doit(logger, l):
        logger.log('starting a big job')
        for x in l:
            logger.log(f'working on {x}')
            time.sleep(1)
        logger.log('done')

    doit(Logger(), [1,2,3])

Suppose we wanted to take our existing logger and have a timestamp on each log. Inheritance makes that easy: we can make a ``TimeLogger`` by extending ``Logger``.

.. runner:: 

    import time

    class Logger(object):
        def format(self, msg):
            return msg

        def emit(self, msg):
            print(msg)
        
        def log(self, msg):
            self.emit(self.format(msg))

    class TimeLogger(Logger):
        def format(self, msg):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            return f'[{timestamp}] {msg}'

    def doit(logger, l):
        logger.log('starting a big job')
        for x in l:
            logger.log(f'working on {x}')
            time.sleep(1)
        logger.log('done')

    doit(Logger(), [1,2,3])
    doit(TimeLogger(), [1,2,3])

Or maybe we'd rather simply count the number of messages logged. We could make a *different* subclass of ``Logger`` that counted as it ran:

.. runner::

    import time

    class Logger(object):
        def format(self, msg):
            return msg

        def emit(self, msg):
            print(msg)
        
        def log(self, msg):
            self.emit(self.format(msg))

    class TimeLogger(Logger):
        def format(self, msg):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            return f'[{timestamp}] {msg}'

    class CountingLogger(Logger):
        def __init__(self):
            self.__count = 0

        def format(self, msg):
            return f'[{self.__count}] {msg}'
            
        def emit(self, msg):
            self.__count += 1

            super().emit(msg)

    def doit(logger, l):
        logger.log('starting a big job')
        for x in l:
            logger.log(f'working on {x}')
            time.sleep(1)
        logger.log('done')

    doit(Logger(), [1,2,3])
    doit(TimeLogger(), [1,2,3])
    doit(CountingLogger(), [1,2,3])

It's worth remarking on ``super()`` in ``CountingLogger``, which says, "now run the method of my super class (i.e., ``Logger``)". Here ``CountingLogger`` increases its count in ``emit`` to that it doesn't ever double count things, i.e., if ``format`` were called more than once for each emit, say. Both ``CountingLogger`` and ``TimeLogger`` **inherit** ``Logger.log``, i.e., without saying anything, each of these classes had a function ``log`` that *called the appropriate methods of the subclass*. That is, when ``doit`` calls ``logger.log`` on the ``TimeLogger``, the ``Logger.log`` implementation will use ``TimeLogger.format``, because ``self`` is ``TimeLogger``. This phenomenon is called **dynamic dispatch**.

In **dynamic dispatch**, the receiver of a method determines which method implementation is called. Each time, it starts at the receiver's actual type, search that type first and then searching through the base classes. `The exact details of Python method resolution order are very complex <https://www.python.org/download/releases/2.3/mro/>`_.

Fortunately, it's not that important to know all of the details (most of the time). Very often, you can figure out what you need about a class in a library by looking at it and its superclasses. Typically, documentation will guide you well here.

Subclasses
----------

You can ask questions about inheritance using the ``issubclass`` function. For example:

.. runner:: 

    import time

    class Logger(object):
        def format(self, msg):
            return msg

        def emit(self, msg):
            print(msg)
        
        def log(self, msg):
            self.emit(self.format(msg))

    class TimeLogger(Logger):
        def format(self, msg):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            return f'[{timestamp}] {msg}'

    class CountingLogger(Logger):
        def __init__(self):
            self.__count = 0

        def format(self, msg):
            return f'[{self.__count}] {msg}'
            
        def emit(self, msg):
            self.__count += 1

            super().emit(msg)

    print(issubclass(CountingLogger, Logger))
    print(issubclass(CountingLogger, TimeLogger))

    cl = CountingLogger()
    print(isinstance(cl, Logger))

If ``issubclass(A, B)`` and ``isinstance(x, A)``, then ``isinstance(x, B)`` will be true, also.