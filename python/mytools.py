"""
These are a few helpful functions that I wrote in CS212 on Udacity with Peter Norvig.  
I'll probably add to them as time goes on. 
"""

from functools import wraps


def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    
    @wraps(memo)
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f