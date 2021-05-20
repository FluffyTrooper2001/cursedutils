import random as _r;import sys as _sys
class Maybe:__bool__,__init__=lambda s:s.n*2*_r.random()>=1,lambda s,n:setattr(s,'n',n)
def self(n):
  @lambda f:setattr(f,'__code__',_sys._getframe(n+1).f_code)
  def wrapper(*a,**k):...
  return wrapper
def Switch():
    """python can't tell me I can't have a switch suite :/"""
    call=lambda*args,**kwargs:lambda f:f(*args,**kwargs)
    named_as=lambda n:lambda f:setattr(f,'__name__',n)or f
    @call()
    class case:
     def __init__(self): self.state, self.value =- 1, None
     def __getitem__(self, item):
      if self.state <- 0:raise SyntaxError("Cannot find matching switch") # __annotations__ hack only works in globals
      if self.value == item and not self.state:self.state=1;return(lambda f,*u,**ck:f(*u,**ck))
      else:return(lambda*No,**ne:None) # XD
    def switch(value):case.value,case.state = value,0
    @named_as('default')
    def otherwise(f,*u,**ck):
      if case.state <- 0 :raise SyntaxError("Cannot find matching switch")
      elif not case.state:case.state =- 1;f(*u,**ck)
    return switch, case, otherwise
# dot notation
hack=lambda victim:__import__('ctypes').py_object.from_address(id(victim)+8)
def _bootstrap(*a):
  from ctypes import*
  if __name__!='__main__':g = __import__('sys')._getframe(2).f_globals
  else:g = globals()
  victim = hack(g).value
  a[2] |= {'gulag':victim}
  struct = type(*a)
  class global_dict(victim):
    def __del__(self): print('exiting corrupted globals...')
    def __missing__(self, key):
      if key in dir(__builtins__):return getattr(__builtins__,key)
      else:
        new = struct()
        object.__setattr__(new, '__name__', key)
        return new
  hack(g).value = global_dict
  return struct
class struct(list,metaclass = bootstrap):
  gulag:type = dict
  __name__ = globals().get('__name__','<string>')
  def __del__(self):hack(self).value=object.__getattribute__(self, 'gulag')
  def __repr__(self):
    getattr = object.__getattribute__
    __dict__ = getattr(self, '__dict__')
    __name__ = getattr(self, '__name__')
    return f"<struct '{__name__}' size={len(__dict__)}>"
  def __getattribute__(self, key):
    getattr = object.__getattribute__
    __class__ = type(self)
    __dict__ = getattr(self, '__dict__')
    __name__ = getattr(self, '__name__')
    if key not in [*dir(__class__),*__dict__]:
      self.__dict__[key] = new = __class__()
      object.__setattr__(new, '__name__', key)
      if key.startswith('__')and key.endswith('__'):
         hack(self).value = type('struct',(__class__,),{key:new,'__name__':__name__+'.'+key})
      return new
    return self.__dict__[key]
  def __setattr__(self, key, value):
    getattr = object.__getattribute__
    __class__ = getattr(self,'__class__')
    __dict__ = getattr(self, '__dict__')
    self.__dict__[key] = value
    if isinstance(value, struct) or issubclass(value.__class__, struct):
      object.__setattr__(struct, '__name__', getattr(self, '__name__')+'.'+key)
    if key.startswith('__')and key.endswith('__'):
      hack(self).value = type('struct',(__class__,),{key:value})
