import unittest

def div(a, b):
    try:
        c = a/b
        return c
    except Exception:
        raise IOError()
    

