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
class struct:
 gulag=type("sentinal",(),{})()
 def __init__(self,name="<struct>"):self.__name__=name
 @classmethod
 def bootstrap1(c,__g):
  try:assert __g
  except AssertionError as e:__g=e.__traceback__.tb_frame.f_back.f_globals
  @lambda f:setattr(__import__('ctypes').py_object.from_address(id(__g)+8),'value',type("dict",(dict,),{'__missing__':f}))
  def __missing__(self,key):
   try:return getattr(__builtins__,key)
   except:self[key]=c()
   return self[key]
 def __getattr__(self,v):
  try:return(f:=lambda:object.__getattribute__(self,v))()
  except AttributeError:setattr(self,v,self.__class__())
  return f()
 def __setattr__(self,n,v):
  if isinstance(v,(lambda:None).__class__):
    victim = __import__('ctypes').py_object.from_address(id(self)+8)
    victim.value = type("struct",(victim.value,),{n:v})
  elif isinstance(v,print.__class__):
    victim = __import__('ctypes').py_object.from_address(id(self)+8)
    victim.value = type("struct",(victim.value,),{n:lambda s,*a,**k:v(*a,**k)})#bound builtin behaviour
  else:object.__setattr__(self,n,v)
 __repr__=lambda s:f"<struct object {s.__name__} 1x{len(dir(self))}"
 @classmethod
 def bootstrap2(self,gl):
  try:assert gl
  except Exception as e:gl=e.__traceback__.tb_frame.f_back.f_globals
  hack=lambda o:__import__('ctypes').c_void_p.from_address(id(o)+8)
  prisoner=hack(gl).value
  self.gulag=type('atexit',(),{'__del__':lambda s:setattr(hack(gl),'value',prisoner)})()
  rename=lambda name:lambda o:setattr(o,'__name__',name)or o
  @lambda f:setattr(hack(gl),'value',type("matlabinated_globals",(prisoner,),{f.__name__:f}))
  def __missing__(self, key):
    try:return getattr(self['__builtins__'],key)
    except AttributeError:return(lambda s:self.__setitem__(key,s))(rename(key)(struct()))
  gl.update({'struct':struct})
  return gl

