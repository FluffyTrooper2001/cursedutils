import random as _r
import sys as _sys
class Maybe:
  def __init__(self,n):self.n=n
  def __bool__(self):return self.n*2*_r.random()>=1
def self(n):
  frame=_sys._getframe(n+1)
  def wrapper(*a,**k):pass
  wrapper.__code__=frame.co_code
  return wrapper
from.import wrappers,iostreams,death
_sys.modules['cursedutils'] = type('', () ,globals())()
