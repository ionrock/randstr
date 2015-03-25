# -*- coding: utf-8 -*-

__author__ = 'Eric Larson'
__email__ = 'eric@ionrock.org'
__version__ = '0.1.1'

import random


CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'


def randstr(length=7):
    return ''.join(random.choice(CHARS) for i in range(length))
