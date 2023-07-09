Blacking out checkers
=====================

A 2D list ``checker`` is declared as

.. code-block::

    checker = [[(255,0,0), (255,255,255), (255,0,0), (255,255,255), (255,0,0)],
               [(255,255,255), (255,0,0), (255,255,255), (255,0,0), (255,255,255)],
               [(255,0,0), (255,255,255), (255,0,0), (255,255,255), (255,0,0)]]

which represents this image:

.. image:: /assets/images/cs515/Week3/redcheck.png
    :align: center

Write nested for loops to modify checker to look as follows:

.. image:: /assets/images/cs515/Week3/redcheck_black.png
    :align: center

(Hint: use ``range``.)

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge11/task.py

    checker = [[(255,0,0), (255,255,255), (255,0,0), (255,255,255), (255,0,0)],
           [(255,255,255), (255,0,0), (255,255,255), (255,0,0), (255,255,255)],
           [(255,0,0), (255,255,255), (255,0,0), (255,255,255), (255,0,0)]]

    # black out square as described above. use nested for loops!