# -*- coding: utf-8 -*-
import random

__author__ = 'Eric Larson'
__email__ = 'eric@ionrock.org'
__version__ = '0.1.2'

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
NUMS = '0123456789'
DELIMITERS = ' -_.,'
CHARS = ALPHA + NUMS
CHARS_WITH_CAPS = ALPHA.upper() + CHARS
CHARS_WITH_DELIMITERS = CHARS + DELIMITERS


def randstr(length=7, chars=CHARS):
    return ''.join(random.choice(chars) for i in range(length))
