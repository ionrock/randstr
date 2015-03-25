=======
randstr
=======

.. image:: https://badge.fury.io/py/randstr.png
    :target: http://badge.fury.io/py/randstr

.. image:: https://travis-ci.org/ionrock/randstr.png?branch=master
        :target: https://travis-ci.org/ionrock/randstr

.. image:: https://pypip.in/d/randstr/badge.png
        :target: https://pypi.python.org/pypi/randstr

Sometimes you just want a random string. For those times, there is `randstr`.


Usage
=====

The default is a 7 character string composed of `a-z0-9`.

.. code-block:: python

   from randstr import randstr

   print(randstr())


You can get a longer string by passing in a length argument.

.. code-block:: python

   randstr(19)



* Free software: BSD license
