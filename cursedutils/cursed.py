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
def Switch():
    """python can't tell me I can't have a switch suite :/"""
    call=lambda*args,**kwargs:lambda f:f(*args,**kwargs)
    named_as=lambda n:lambda f:setattr(f,'__name__',n)or f
    @call()
    class case:
     def __init__(self): self.state, self.value = -1, None
     def __getitem__(self, item):
      if self.state <=- 1:  raise SyntaxError("Cannot find matching switch") # __annotations__ hack only works in globals
      if self.value == item and not self.state: self.state=1; return(lambda f,*u,**ck:f(*u,**ck))
      else:                 return(lambda *No, **ne:None) # XD
    def switch(value):case.value,case.state = value,0
    @named_as('default') # just for you XD.
    def otherwise(f,*u,**ck):
      if case.state <- 0 :  raise SyntaxError("Cannot find matching switch")
      elif not case.state:  case.state =- 1; f(*u,**ck)
    return switch, case, otherwise #   ^ this is deliberate. XD
