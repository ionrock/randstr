# -*- coding: utf-8 -*-
import random

__author__ = 'Eric Larson'
__email__ = 'eric@ionrock.org'
__version__ = '0.1.1'


CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'


def randstr(length=7, chars=CHARS):
    return ''.join(random.choice(chars) for i in range(length))
